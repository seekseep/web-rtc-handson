// 画面の部品を取っておく
const wordInput = document.querySelector('#word');
const hostButton = document.querySelector('#host');
const guestButton = document.querySelector('#guest');
const statusText = document.querySelector('#status');
const clearButton = document.querySelector('#clear');
const canvas = document.querySelector('#canvas');
const ctx = canvas.getContext('2d');

// つながっている相手ぜんぶ。1 対 1 のときの conn を、そのまま配列にしたもの。
const conns = [];

// いま選んでいる道具と色とスタンプ
let tool = 'pen';
let color = '#333333';
let stamp = '🐱';

// これまでに描いた指示をぜんぶ覚えておく
const history = [];

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

  // 何人でも入ってこられる。1 人来るたびに connection が呼ばれる。
  peer.on('connection', function (conn) {
    conn.on('open', function () {
      ready(conn);
    });
  });

  peer.on('error', showError);
});

// へやにはいる側（ゲスト）。名前は名乗らず、あいことばの相手に向かってつなぎに行く。
guestButton.addEventListener('click', function () {
  const peer = new Peer();

  peer.on('open', function () {
    const conn = peer.connect(roomId(wordInput.value));
    conn.on('open', function () {
      ready(conn);
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

// つながった相手を 1 人ぶん受け持つ。ホストでもゲストでも中身は同じ。
function ready(conn) {
  conns.push(conn);
  showCount();

  conn.on('close', function () {
    // 切れた相手を一覧から外す。
    // indexOf が -1 のときに splice すると別の相手が消えるので、必ず確かめる。
    const index = conns.indexOf(conn);
    if (index !== -1) {
      conns.splice(index, 1);
    }
    showCount();
  });

  conn.on('data', function (data) {
    apply(data);
    remember(data);
    // 届いた指示を、送ってきた本人いがいの全員にも配る。
    // これでホストが中継役になり、ゲスト同士の絵もそろう。
    send(data, conn);
  });

  // これまでの絵を、あとから来たこの相手にも見せる
  history.forEach(function (data) {
    conn.send(data);
  });
}

function showCount() {
  statusText.textContent =
    conns.length === 0
      ? 'ぜんいん切れました'
      : conns.length + ' 人とつながっています';
}

// つながっている全員に送る。except に渡した相手だけは飛ばす
// （送ってきた本人に、同じものを送り返さないため）。
function send(data, except) {
  conns.forEach(function (conn) {
    if (conn !== except) {
      conn.send(data);
    }
  });
}

// 自分が出した指示も、届いた指示も、ぜんぶ覚えておく。
// あとから入ってきた人には、この記録をまとめて送る。
function remember(data) {
  if (data.type === 'clear') {
    history.length = 0;
  } else {
    history.push(data);
  }
}

// 指示のとおりにキャンバスへ描く。
// 自分が出した指示も、相手から届いた指示も、かならずここを通る。
function apply(data) {
  if (data.type === 'line') {
    drawLine(data.x1, data.y1, data.x2, data.y2, data.color, data.width);
  }
  if (data.type === 'stamp') {
    drawStamp(data.x, data.y, data.emoji);
  }
  if (data.type === 'clear') {
    clearCanvas();
  }
}

// 自分のキャンバスに描いてから、同じ指示を「つながっている全員」に送る。
// 相手が 0 人でも、send は何もしないだけなので、そのまま呼んでよい。
function draw(data) {
  apply(data);
  remember(data);
  send(data, null);
}

function drawLine(x1, y1, x2, y2, lineColor, lineWidth) {
  ctx.strokeStyle = lineColor;
  ctx.lineWidth = lineWidth;
  ctx.lineCap = 'round';
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
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

// canvas は 800x600 のまま、空いている場所に合わせて縮めて表示している。
// クリックされた位置は「画面上の px」なので、縮めた比率で割って
// 800x600 の中での座標に戻す。これをやらないと 2 台で線がズレる。
function positionOf(event) {
  const rect = canvas.getBoundingClientRect();

  return {
    x: ((event.clientX - rect.left) / rect.width) * canvas.width,
    y: ((event.clientY - rect.top) / rect.height) * canvas.height,
  };
}

// 直前のペン先の位置。線は「前の点から今の点まで」をつなげて描く。
let last = null;

canvas.addEventListener('pointerdown', function (event) {
  const pos = positionOf(event);

  if (tool === 'stamp') {
    draw({ type: 'stamp', x: pos.x, y: pos.y, emoji: stamp });
    return;
  }

  last = pos;
});

canvas.addEventListener('pointermove', function (event) {
  if (last === null) return;

  const pos = positionOf(event);

  draw({
    type: 'line',
    x1: last.x,
    y1: last.y,
    x2: pos.x,
    y2: pos.y,
    // けしごむは「背景と同じ白い色で、太く描くペン」として作る
    color: tool === 'eraser' ? '#ffffff' : color,
    width: tool === 'eraser' ? 40 : 4,
  });

  last = pos;
});

canvas.addEventListener('pointerup', function () {
  last = null;
});

canvas.addEventListener('pointerleave', function () {
  last = null;
});

document.querySelectorAll('.tool').forEach(function (button) {
  button.addEventListener('click', function () {
    tool = button.dataset.tool;
    select(button, '.tool, .stamp');
  });
});

document.querySelectorAll('.stamp').forEach(function (button) {
  button.addEventListener('click', function () {
    tool = 'stamp';
    stamp = button.dataset.stamp;
    select(button, '.tool, .stamp');
  });
});

document.querySelectorAll('.color').forEach(function (button) {
  // ボタンの見た目の色を data-color から流し込む
  button.style.background = button.dataset.color;

  button.addEventListener('click', function () {
    color = button.dataset.color;
    select(button, '.color');
  });
});

clearButton.addEventListener('click', function () {
  draw({ type: 'clear' });
});

// 同じ仲間のボタンから選択の印を外して、押されたものだけに付ける
function select(button, group) {
  document.querySelectorAll(group).forEach(function (other) {
    other.classList.remove('selected');
  });
  button.classList.add('selected');
}

clearCanvas();
