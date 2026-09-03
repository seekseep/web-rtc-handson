// 画面の部品を取っておく
const wordInput = document.querySelector('#word');
const hostButton = document.querySelector('#host');
const guestButton = document.querySelector('#guest');
const statusText = document.querySelector('#status');
const canvas = document.querySelector('#canvas');
const ctx = canvas.getContext('2d');

// つながった相手との通り道。まだつながっていないので null。
let conn = null;

// いま選んでいるスタンプ
let stamp = '🐱';

// あいことばから、PeerJS Cloud で名乗る名前を作る。
// PeerJS Cloud は世界中の人と共有しているので「test」のような短い名前は
// すでに誰かに使われている。長めの前置きを付けてぶつかりにくくする。
function roomId(word) {
  return 'webrtc-handson-' + word;
}

// へやをつくる側（ホスト）。あいことばを自分の名前として名乗り、誰かが来るのを待つ。
hostButton.addEventListener('click', function () {
  const peer = new Peer(roomId(wordInput.value));

  peer.on('open', function () {
    statusText.textContent = 'あいてを待っています…';
  });

  peer.on('connection', function (newConn) {
    conn = newConn;
    conn.on('open', ready);
  });

  peer.on('error', showError);
});

// へやにはいる側（ゲスト）。名前は名乗らず、あいことばの相手に向かってつなぎに行く。
guestButton.addEventListener('click', function () {
  const peer = new Peer();

  peer.on('open', function () {
    conn = peer.connect(roomId(wordInput.value));
    conn.on('open', ready);
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
function ready() {
  statusText.textContent = 'つながりました';

  conn.on('close', function () {
    statusText.textContent = 'せつだんされました';
  });

  // 相手から届いた指示も、自分が出した指示と同じ apply に通す。
  conn.on('data', apply);
}

// 指示のとおりにキャンバスへ描く。
// 自分が出した指示も、相手から届いた指示も、かならずここを通る。
function apply(data) {
  if (data.type === 'stamp') {
    drawStamp(data.x, data.y, data.emoji);
  }
}

// 自分のキャンバスに描いてから、同じ指示を相手にも送る。
// 「描く」と「送る」を必ずセットにするので、2 つの画面が同じ絵になる。
function draw(data) {
  apply(data);

  if (conn) {
    conn.send(data);
  }
}

function drawStamp(x, y, emoji) {
  ctx.font = '48px sans-serif';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  ctx.fillText(emoji, x, y);
}

function clearCanvas() {
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// canvas は 800x600 のまま、画面幅に合わせて縮めて表示している。
// クリックされた位置は「画面上の px」なので、縮めた比率で割って
// 800x600 の中での座標に戻す。これをやらないと 2 台で線がズレる。
function positionOf(event) {
  const rect = canvas.getBoundingClientRect();

  return {
    x: ((event.clientX - rect.left) / rect.width) * canvas.width,
    y: ((event.clientY - rect.top) / rect.height) * canvas.height,
  };
}

canvas.addEventListener('pointerdown', function (event) {
  const pos = positionOf(event);

  draw({ type: 'stamp', x: pos.x, y: pos.y, emoji: stamp });
});

document.querySelectorAll('.stamp').forEach(function (button) {
  button.addEventListener('click', function () {
    stamp = button.dataset.stamp;
    select(button, '.stamp');
  });
});

// 同じ仲間のボタンから選択の印を外して、押されたものだけに付ける
function select(button, group) {
  document.querySelectorAll(group).forEach(function (other) {
    other.classList.remove('selected');
  });
  button.classList.add('selected');
}

clearCanvas();
