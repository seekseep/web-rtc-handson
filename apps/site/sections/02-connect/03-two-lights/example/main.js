// 画面の部品を取っておく
const myCircle = document.querySelector('#my-circle');
const peerCircle = document.querySelector('#peer-circle');
const lightButton = document.querySelector('#light');
const peerLightButton = document.querySelector('#peer-light');

lightButton.addEventListener('click', function () {
  // 0〜359 のどれかの色相。押すたびに違う色になる。
  const color = 'hsl(' + Math.floor(Math.random() * 360) + ', 90%, 60%)';

  myCircle.style.background = color;
});

// 「あいて」の丸を光らせる練習用のボタン。次の節で、この係は相手にゆずる。
peerLightButton.addEventListener('click', function () {
  const color = 'hsl(' + Math.floor(Math.random() * 360) + ', 90%, 60%)';

  peerCircle.style.background = color;
});
