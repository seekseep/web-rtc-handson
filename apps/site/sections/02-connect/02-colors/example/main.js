// 画面の部品を取っておく
const myCircle = document.querySelector('#my-circle');
const lightButton = document.querySelector('#light');

lightButton.addEventListener('click', function () {
  // 0〜359 のどれかの色相。押すたびに違う色になる。
  const color = 'hsl(' + Math.floor(Math.random() * 360) + ', 90%, 60%)';

  myCircle.style.background = color;
});
