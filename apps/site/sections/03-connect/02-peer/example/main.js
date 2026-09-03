// 画面の部品を取っておく
const hostButton = document.querySelector('#host');
const guestButton = document.querySelector('#guest');
const statusText = document.querySelector('#status');
const myCircle = document.querySelector('#my-circle');
const peerCircle = document.querySelector('#peer-circle');
const lightButton = document.querySelector('#light');

// つながった相手との通り道。まだつながっていないので null。
let conn = null;

// PeerJS Cloud で名乗る名前。いまは決め打ちにしておく。
// PeerJS Cloud は世界中の人と共有しているので、'test' のままだと
// 同じことをしている人とぶつかる。自分の名前などに書き換えて使うこと。
const ROOM = 'webrtc-handson-test';

// へやをつくる側（ホスト）。ROOM を自分の名前として名乗り、誰かが来るのを待つ。
hostButton.addEventListener('click', function () {
  const peer = new Peer(ROOM);

  peer.on('open', function () {
    statusText.textContent = 'あいてを待っています…';
  });

  peer.on('connection', function (newConn) {
    conn = newConn;
    conn.on('open', ready);
  });

  peer.on('error', showError);
});

// へやにはいる側（ゲスト）。名前は名乗らず、ROOM の相手に向かってつなぎに行く。
guestButton.addEventListener('click', function () {
  const peer = new Peer();

  peer.on('open', function () {
    conn = peer.connect(ROOM);
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
}

lightButton.addEventListener('click', function () {
  // 0〜359 のどれかの色相。押すたびに違う色になる。
  const color = 'hsl(' + Math.floor(Math.random() * 360) + ', 90%, 60%)';

  myCircle.style.background = color;
});
