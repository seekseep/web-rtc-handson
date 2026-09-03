// 画面の部品を取っておく
const myCircle = document.querySelector('#my-circle');
const lightButton = document.querySelector('#light');

lightButton.addEventListener('click', function () {
  myCircle.style.background = '#ffd60a';
});
