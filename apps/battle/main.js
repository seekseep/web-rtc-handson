// 画面の部品を取っておく
const wordInput = document.querySelector('#word');
const hostButton = document.querySelector('#host');
const guestButton = document.querySelector('#guest');
const statusText = document.querySelector('#status');
const myScoreText = document.querySelector('#my-score');
const yourScoreText = document.querySelector('#your-score');
const inkBar = document.querySelector('#ink-bar');
const timeText = document.querySelector('#time');
const overlay = document.querySelector('#overlay');
const overlayText = document.querySelector('#overlay-text');
const overlayNote = document.querySelector('#overlay-note');
const readyButton = document.querySelector('#ready');
const canvas = document.querySelector('#canvas');
const ctx = canvas.getContext('2d');

// つながった相手との通り道。まだつながっていないので null。
let conn = null;

// 「へやをつくる」か「へやにはいる」を押したか。押したあとはまだつながっていなくても
// 案内の文を「待っています」に変えたいので、conn とは別に持っておく。
let joined = false;

// 盤面のマス目。800x600 を 20px 四方で割ると 40x30 = 1200 マスになる。
// 1 マスが全体の 0.083%、ペン 1 回（3x3 マス）で 0.75% 取れる、という細かさ。
const CELL = 20;
const COLS = 40;
const ROWS = 30;
const COUNT = COLS * ROWS;

// マスには色ではなく「だれのものか」を入れる。こうすると数えるのが楽になる。
const EMPTY = 0;
const HOST = 1;
const GUEST = 2;

// 盤面そのもの。お絵かきアプリの history（指示の記録）の代わりに、
// 「いまどうなっているか」だけを持つ。占有率もここから数える。
const grid = new Array(COUNT).fill(EMPTY);

// 自分がホストかゲストか。つながるまで決まらない。
let me = EMPTY;

// インク。塗ると減り、手を離している間だけ回復する。
// 満タンから一気に 200 マス塗れるので、早めに手を離せるほど有利になる。
const INK_MAX = 100;
const INK_PER_CELL = 0.5;
const INK_RECOVER = 30;
const INK_RESTART = 30;
let ink = INK_MAX;
let inkEmpty = false;

// 試合の進み方。'idle'（待ち）→ 'count'（3・2・1）→ 'play'（60 秒）→ 'result'
const COUNT_MS = 3000;
const MATCH_MS = 60000;
let phase = 'idle';

// カウントダウンと試合の「終わる時刻」。setInterval を数えた回数で時間を測ると、
// 裏にまわったタブでは呼ばれる回数が減ってズレる。時刻を持って毎回引き算する。
let phaseEndsAt = 0;
let tickedAt = Date.now();

// じゅんびOK を押したかどうか。start を出すかどうかはホストだけが決める。
let hostReady = false;
let guestReady = false;

// 直前のペン先の位置。null なら「いま塗っていない」＝インクが回復する。
let last = null;
let activePointer = null;

// あいことばから、PeerJS Cloud で名乗る名前を作る。
// PeerJS Cloud は世界中の人と共有しているので「test」のような短い名前は
// すでに誰かに使われている。長めの前置きを付けてぶつかりにくくする。
function roomId(word) {
  return 'webrtc-handson-battle-' + word;
}

// へやをつくる側（ホスト）。あいことばを自分の名前として名乗り、誰かが来るのを待つ。
hostButton.addEventListener('click', function () {
  joined = true;
  const peer = new Peer(roomId(wordInput.value));

  peer.on('open', function () {
    statusText.textContent = 'あいてを待っています…';
  });

  peer.on('connection', function (newConn) {
    // このゲームはふたりちょうど。3 人目に入られると盤面の持ち主が増えてしまうので、
    // 先に来たひとりだけを相手にする。
    if (conn !== null) {
      newConn.close();
      return;
    }

    conn = newConn;
    conn.on('open', function () {
      ready(HOST);
    });
  });

  peer.on('error', showError);
});

// へやにはいる側（ゲスト）。名前は名乗らず、あいことばの相手に向かってつなぎに行く。
guestButton.addEventListener('click', function () {
  joined = true;
  const peer = new Peer();

  peer.on('open', function () {
    conn = peer.connect(roomId(wordInput.value));
    conn.on('open', function () {
      ready(GUEST);
    });
  });

  peer.on('error', showError);
});

// PeerJS から届くエラーを、日本語のことばにして出す。
// err.type にどんなエラーかが入っている。
function showError(err) {
  if (err.type === 'unavailable-id') {
    statusText.textContent =
      'そのあいことばは使われています。別のあいことばにするか「へやにはいる」を押してください';
  } else if (err.type === 'peer-unavailable') {
    statusText.textContent =
      'そのあいことばのへやが見つかりません。相手が「へやをつくる」を押したか確かめてください';
  } else {
    statusText.textContent = 'つながりませんでした（' + err.type + '）';
  }
}

// ホストでもゲストでも、つながったあとにやることは同じ。
// 違うのは「自分がどちらの色か」だけ。
function ready(role) {
  me = role;
  statusText.textContent = 'つながりました';

  // つなぎ直したときのために、じゅんびの印はここで戻す
  hostReady = false;
  guestReady = false;

  // 自分とあいての色を点数に流し込む（インクゲージは showHud が塗る）
  myScoreText.style.color = colorOf(me);
  yourScoreText.style.color = colorOf(other(me));

  conn.on('close', function () {
    statusText.textContent = 'せつだんされました';
    conn = null;

    // 試合中に切れたら、そこまでの盤面で締める。
    // ホストの end がもう来ないので、待ちっぱなしで固まらないようにする。
    if (phase === 'count' || phase === 'play') {
      apply({ type: 'end', grid: grid });
    } else {
      showOverlay();
    }
  });

  // 相手から届いた指示も、自分が出した指示と同じ apply に通す。
  conn.on('data', apply);

  showHud();
  showOverlay();
}

// 指示のとおりに自分の画面を変える。
// 自分が出した指示も、相手から届いた指示も、かならずここを通る。
function apply(data) {
  if (data.type === 'ready') {
    // 「だれが押したか」を指示に入れてあるので、自分が出しても相手から届いても
    // 同じように扱える。向きを気にしなくていい。
    if (data.by === HOST) {
      hostReady = true;
    }
    if (data.by === GUEST) {
      guestReady = true;
    }
    startIfBothReady();
  }

  if (data.type === 'start') {
    startMatch();
  }

  if (data.type === 'paint') {
    paintCells(data.cells, data.by);
  }

  if (data.type === 'end') {
    finishMatch(data.grid);
  }

  showHud();
  showOverlay();
}

// 自分の画面に当ててから、同じ指示を相手にも送る。
// 「当てる」と「送る」を必ずセットにするので、2 つの画面が同じ動きになる。
// お絵かきアプリと違って history には貯めない。試合の途中から入ってくる人がいないので、
// 指示を取っておく理由がない（いまの盤面は grid が持っている）。
function draw(data) {
  apply(data);

  if (conn) {
    conn.send(data);
  }
}

// 開始を決めるのはホストだけ。ふたりが別々に「そろった」と判断すると、
// 始まった時刻がずれて、のこり時間も食い違う。
function startIfBothReady() {
  if (me !== HOST) return;
  if (hostReady === false || guestReady === false) return;

  draw({ type: 'start' });
}

// 3・2・1 を出してから 60 秒。ホストもゲストも同じ手順を踏む。
// 「何時に始める」と時刻を送る手もあるが、2 台の時計は数秒ずれていることがあるので、
// 自分の時計だけで測れるように「合図が届いてから数える」形にしている。
function startMatch() {
  clearBoard();
  ink = INK_MAX;
  inkEmpty = false;
  stopPainting();
  hostReady = false;
  guestReady = false;
  phase = 'count';
  phaseEndsAt = Date.now() + COUNT_MS;
}

// 試合を終わらせる。board はホストの盤面。
// ふたりが同じマスをほぼ同時に塗ると、自分の塗りを先に自分の盤面へ当てているぶんだけ、
// ホストとゲストで持ち主が入れかわる。指示が順番どおり全部届いていてもズレる。
// どちらが正かを決めないと結果が食い違うので、審判であるホストの盤面をそのまま配って、
// 絵と数字の両方をそろえる。
function finishMatch(board) {
  for (let i = 0; i < COUNT; i++) {
    grid[i] = board[i];
  }
  redrawBoard();

  phase = 'result';
  stopPainting();
}

// マスの持ち主を owner にして、そのマスだけ塗り直す。
// 盤面ぜんぶを描き直さないので、1 回あたり数マスぶんの fillRect で済む。
function paintCells(cells, owner) {
  ctx.fillStyle = colorOf(owner);

  for (let i = 0; i < cells.length; i++) {
    const index = cells[i];
    grid[index] = owner;
    // 番号 1 つから場所を出す。index = row * COLS + col の逆算。
    ctx.fillRect(
      (index % COLS) * CELL,
      Math.floor(index / COLS) * CELL,
      CELL,
      CELL,
    );
  }
}

// from から to まで、ペンが通ったマスの番号を集める。ここでは塗らない。
// すでに自分の色のマスは取らない。塗り直してもインクの無駄なので、
// 自分の陣地をなぞっているあいだは 1 通も送らずに済む。
function takeCells(from, to, limit) {
  const cells = [];
  // このイベントで拾ったマスの目印。同じマスを二度数えないため。
  const picked = {};

  const dx = to.x - from.x;
  const dy = to.y - from.y;
  const distance = Math.sqrt(dx * dx + dy * dy);
  // マス半分（10px）ずつ進む。これより粗いと、速く動かしたときに穴があく。
  const steps = Math.max(1, Math.ceil(distance / (CELL / 2)));

  for (let s = 0; s <= steps; s++) {
    const centerCol = Math.floor((from.x + (dx * s) / steps) / CELL);
    const centerRow = Math.floor((from.y + (dy * s) / steps) / CELL);

    // ペンの太さは 3x3 マス（60x60 px）
    for (let r = centerRow - 1; r <= centerRow + 1; r++) {
      for (let c = centerCol - 1; c <= centerCol + 1; c++) {
        // 盤面の外は捨てる。これをしないと c が -1 のときに
        // index が 1 つ上の行の右端に回り込んで、反対側が塗れてしまう。
        if (c < 0 || c >= COLS || r < 0 || r >= ROWS) continue;

        const index = r * COLS + c;
        if (picked[index]) continue;
        if (grid[index] === me) continue;
        if (cells.length >= limit) return cells;

        picked[index] = true;
        cells.push(index);
      }
    }
  }

  return cells;
}

// from から to までを自分の色で塗る。インクが足りるぶんだけ。
function paint(from, to) {
  if (canPaint() === false) return;

  // いま何マスまで塗れるか。1 マスで INK_PER_CELL だけ減る。
  const limit = Math.floor(ink / INK_PER_CELL);
  const cells = takeCells(from, to, limit);

  // 1 マスも取れなかったとき（ぜんぶ自分の色だった）は何も送らない。
  // 塗っていないのに通信だけ起きるのを防ぐ。
  if (cells.length === 0) return;

  ink -= cells.length * INK_PER_CELL;

  if (ink < INK_PER_CELL) {
    // 空になった。しきい値まで回復するまで塗れない。
    // これが無いと、0 のあたりで 1 マスずつ塗り続けられて駆け引きが消える。
    ink = 0;
    inkEmpty = true;
  }

  draw({ type: 'paint', by: me, cells: cells });
}

function canPaint() {
  return phase === 'play' && inkEmpty === false && ink >= INK_PER_CELL;
}

// canvas は 800x600 のまま、空いている場所に合わせて縮めて表示している。
// さわられた位置は「画面上の px」なので、縮めた比率で割って
// 800x600 の中での座標に戻す。これをやらないと 2 台でマス目がズレる。
function positionOf(event) {
  const rect = canvas.getBoundingClientRect();

  return {
    x: ((event.clientX - rect.left) / rect.width) * canvas.width,
    y: ((event.clientY - rect.top) / rect.height) * canvas.height,
  };
}

canvas.addEventListener('pointerdown', function (event) {
  if (phase !== 'play') return;
  // 指が 2 本のったときは、先にのったほうだけを見る
  if (activePointer !== null) return;

  activePointer = event.pointerId;
  // 指やマウスが盤面の外へ出ても pointerup を受け取れるようにする。
  // これが無いと「離したのに塗りっぱなし」になって、インクが永久に回復しない。
  canvas.setPointerCapture(event.pointerId);

  last = positionOf(event);
  // 押しただけでも 1 回ぶん塗る
  paint(last, last);
});

canvas.addEventListener('pointermove', function (event) {
  if (last === null) return;
  if (event.pointerId !== activePointer) return;

  const pos = positionOf(event);
  paint(last, pos);
  last = pos;
});

function stopPainting() {
  activePointer = null;
  last = null;
}

canvas.addEventListener('pointerup', stopPainting);
// スマホでピンチなどに割り込まれると、pointerup ではなく pointercancel が来る
canvas.addEventListener('pointercancel', stopPainting);
// ページの外でマウスを離すと、どちらも来ないことがある。その保険。
window.addEventListener('blur', stopPainting);

readyButton.addEventListener('click', function () {
  // 「じゅんびOK」も「もういちど」も、やることは同じ。
  // どちらから押してもよく、ふたりそろったところでホストが start を出す。
  if (conn === null) return;
  if (phase === 'count' || phase === 'play') return;
  if (myReady()) return;

  draw({ type: 'ready', by: me });
});

// 0.1 秒ごとに、インクの回復・のこり時間・占有率を見直す。
// requestAnimationFrame は使わない。動き続けるものが無く、
// 画面の書きかえは「塗ったマスだけ」で足りるため。
function tick() {
  const now = Date.now();
  // 裏にまわったタブでは setInterval が間引かれる。
  // 経過したミリ秒から計算しておけば、遅れても回復量がズレない。
  const passed = now - tickedAt;
  tickedAt = now;

  // 手を離している間だけ回復する。インクぎれのときは押したままでも回復する
  // （そうしないとロックが解けない）。
  if (last === null || inkEmpty === true) {
    ink = Math.min(INK_MAX, ink + (INK_RECOVER * passed) / 1000);
    if (inkEmpty === true && ink >= INK_RESTART) {
      inkEmpty = false;
    }
  }

  if (phase === 'count' && now >= phaseEndsAt) {
    phase = 'play';
    phaseEndsAt = now + MATCH_MS;
  }

  // 終わりを決めるのもホストだけ。ふたりが別々に締めると、締めた瞬間の盤面が違う。
  if (phase === 'play' && me === HOST && now >= phaseEndsAt) {
    draw({ type: 'end', grid: grid });
  }

  // ホストの合図が来ないとき（回線が詰まった・タブが凍った）でも、
  // 3 秒待ったら自分の盤面で締める。待ちっぱなしで固まらないようにする。
  if (phase === 'play' && me === GUEST && now >= phaseEndsAt + 3000) {
    apply({ type: 'end', grid: grid });
  }

  showHud();
  showOverlay();
}

// 点数・インク・のこり時間を、いまの状態のとおりに書きかえる。
function showHud() {
  // つながるまではどちらの色でもない。数えると白いマスが全部自分のものに
  // 見えてしまうので、0% のままにしておく。
  myScoreText.textContent =
    'あなた ' + (me === EMPTY ? 0 : percentOf(me)) + '%';
  yourScoreText.textContent =
    'あいて ' + (me === EMPTY ? 0 : percentOf(other(me))) + '%';

  inkBar.style.width = (ink / INK_MAX) * 100 + '%';
  // インクぎれは文字ではなく色で知らせる。ゲージを見たままで気づける。
  if (inkEmpty) {
    inkBar.style.background = '#e5484d';
  } else if (me === EMPTY) {
    inkBar.style.background = '#888';
  } else {
    inkBar.style.background = colorOf(me);
  }

  timeText.textContent = phase === 'play' ? secondsLeft() : '60';
}

// 盤面にかぶせる案内を、いまの状態のとおりに出し分ける。
function showOverlay() {
  // 試合中は案内を消して、盤面を全部見せる
  if (phase === 'play') {
    overlay.style.display = 'none';
    return;
  }
  overlay.style.display = 'flex';

  if (phase === 'count') {
    overlayText.textContent = secondsLeft();
    overlayNote.textContent = 'ドラッグして、ぬったマスを取り合います';
    readyButton.hidden = true;
    return;
  }

  if (phase === 'result') {
    const mine = countOf(me);
    const yours = countOf(other(me));
    overlayText.textContent =
      mine > yours
        ? 'あなたのかち'
        : mine < yours
          ? 'あいてのかち'
          : 'ひきわけ';
    overlayNote.textContent =
      'あなた ' + percentOf(me) + '% ・ あいて ' + percentOf(other(me)) + '%';
    readyButton.textContent = 'もういちど';
    // 相手が切れているあいだは、押しても始まらないので出さない
    readyButton.hidden = conn === null;
    readyButton.disabled = myReady();
    return;
  }

  // ここから下は待ちの画面。つないだかどうかで案内を変える。
  overlayText.textContent = '色塗りバトル';
  readyButton.textContent = 'じゅんびOK';

  if (me === EMPTY) {
    overlayNote.textContent = joined
      ? 'あいてを待っています…'
      : 'あいことばを決めて、ふたりでつないでください';
    readyButton.hidden = true;
    return;
  }

  readyButton.hidden = conn === null;
  readyButton.disabled = myReady();
  overlayNote.textContent = myReady()
    ? 'あいてを待っています…'
    : 'ふたりとも押したら はじまります';
}

// 盤面を白にもどす。grid と見た目は必ずセットで戻す。
// 片方だけだと、前の試合の色が残っているのに点数が 0% になる。
function clearBoard() {
  grid.fill(EMPTY);
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// grid のとおりに、盤面をまるごと描き直す。
// 使うのは試合の終わり（ホストの盤面で置きかえるとき）だけ。
function redrawBoard() {
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  for (let i = 0; i < COUNT; i++) {
    if (grid[i] === EMPTY) continue;
    ctx.fillStyle = colorOf(grid[i]);
    ctx.fillRect((i % COLS) * CELL, Math.floor(i / COLS) * CELL, CELL, CELL);
  }
}

function colorOf(owner) {
  if (owner === HOST) return '#006fee';
  if (owner === GUEST) return '#f5a524';
  return '#ffffff';
}

function other(owner) {
  return owner === HOST ? GUEST : HOST;
}

function countOf(owner) {
  let n = 0;
  for (let i = 0; i < COUNT; i++) {
    if (grid[i] === owner) n++;
  }
  return n;
}

function percentOf(owner) {
  return Math.round((countOf(owner) / COUNT) * 100);
}

function secondsLeft() {
  return Math.max(0, Math.ceil((phaseEndsAt - Date.now()) / 1000));
}

function myReady() {
  return me === HOST ? hostReady : guestReady;
}

clearBoard();
showHud();
showOverlay();

// タイマーはここで 1 本だけ張る。試合が始まるたびに張ると、
// 再戦のたびにタイマーが増えて、のこり時間が倍速で進む。
setInterval(tick, 100);
