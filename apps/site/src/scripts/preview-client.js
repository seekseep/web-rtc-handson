// `::preview` のライブプレビュー（sentinels.mjs が生成する `.lecture-preview`）の
// 「↻ 再読み込み」ボタン。押すと iframe を読み直し、ゲームを最初からやり直せる。
// あわせて、明暗の切り替えをデモの iframe に届ける。
// `.lecture-preview` が無いページでは何もしない。全ページの <head> に inline 注入される。
(function () {
  function reload(iframe) {
    // src を入れ直すことで確実に読み直す（location.reload はタイミングで空振りするため）。
    var src = iframe.getAttribute('src');
    iframe.setAttribute('src', src);
  }

  function setup() {
    document.querySelectorAll('.lecture-preview').forEach(function (fig) {
      var btn = fig.querySelector('.lecture-preview__reload');
      var iframe = fig.querySelector('.lecture-preview__frame');
      if (!btn || !iframe) return;
      btn.addEventListener('click', function () {
        reload(iframe);
      });
    });
  }

  // 解説用デモ（`<lec>/demos/`）の明暗をページに合わせる。デモは開くときに
  // こちらの data-theme を自分で読むので、ここでは開いたあとの切り替えだけ届ける。
  // data-theme を持たない iframe（完成サンプルなど）は明暗に対応していないので触らない。
  function syncTheme() {
    var theme = document.documentElement.dataset.theme;
    document.querySelectorAll('.lecture-preview__frame').forEach(function (iframe) {
      var doc = iframe.contentDocument;
      if (doc && doc.documentElement.hasAttribute('data-theme')) {
        doc.documentElement.dataset.theme = theme;
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setup);
  } else {
    setup();
  }

  new MutationObserver(syncTheme).observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-theme'],
  });
})();
