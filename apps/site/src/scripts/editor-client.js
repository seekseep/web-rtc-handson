// 簡易エディタ UI（remark-editor.mjs が生成する `.editor`）の切り替え。
//   - 左のファイルボタン … 対応するコードペインだけを表示する
//   - ヘッダの差分ボタン … 「完成例」と「前の節との差分」を行き来する
//   - ヘッダの全画面     … 画面いっぱいに広げる（Esc で戻る）
// `.editor` が無いページでは何もしない。全ページの <head> に inline 注入される。
(function () {
  function activate(editor, file) {
    editor.querySelectorAll('.editor__file').forEach(function (btn) {
      btn.classList.toggle('is-active', btn.dataset.file === file);
    });
    editor.querySelectorAll('.editor__pane').forEach(function (pane) {
      pane.classList.toggle('is-active', pane.dataset.file === file);
    });
  }

  // どのペインを出すかは CSS 側（.editor[data-view] × .editor__pane[data-view]）が決める。
  function activateView(editor, view) {
    editor.dataset.view = view;
    var btn = editor.querySelector('.editor__diff');
    if (!btn) return;
    var on = view === 'diff';
    btn.classList.toggle('is-active', on);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
  }

  // 全画面のあいだ、元の位置を覚えておく目印（同時に開けるのは 1 つだけ）。
  var restoreMark = null;

  // 全画面はブラウザの Fullscreen API ではなく、画面を覆うオーバーレイで出す。
  // iOS Safari は video 以外の requestFullscreen を持たないので、挙動を 1 つに絞る。
  //
  // ただし Starlight のレイアウトには container-type を持つ祖先があり、その中では
  // position: fixed がビューポートではなく祖先を基準にしてしまう。全画面のあいだだけ
  // body 直下へ移して、戻す場所をコメントノードで覚えておく。
  function setFullscreen(editor, on) {
    if (on) {
      restoreMark = document.createComment('editor');
      editor.parentNode.insertBefore(restoreMark, editor);
      document.body.appendChild(editor);
    } else if (restoreMark) {
      restoreMark.parentNode.insertBefore(editor, restoreMark);
      restoreMark.parentNode.removeChild(restoreMark);
      restoreMark = null;
    }
    editor.classList.toggle('is-fullscreen', on);
    document.body.classList.toggle('is-editor-fullscreen', on);
    var btn = editor.querySelector('.editor__fullscreen');
    if (btn) {
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      btn.textContent = on ? 'もどす' : '全画面';
    }
  }

  // Esc で閉じたときだけ、押していたボタンにフォーカスを戻す（クリックなら既にそこに居る）。
  function closeFullscreen(focusButton) {
    var open = document.querySelector('.editor.is-fullscreen');
    if (!open) return;
    setFullscreen(open, false);
    if (!focusButton) return;
    var btn = open.querySelector('.editor__fullscreen');
    if (btn) btn.focus();
  }

  function setup() {
    document.querySelectorAll('.editor').forEach(function (editor) {
      editor.querySelectorAll('.editor__file').forEach(function (btn) {
        btn.addEventListener('click', function () {
          activate(editor, btn.dataset.file);
        });
      });
      var diff = editor.querySelector('.editor__diff');
      if (diff) {
        diff.addEventListener('click', function () {
          activateView(
            editor,
            editor.dataset.view === 'diff' ? 'code' : 'diff',
          );
        });
      }
      var full = editor.querySelector('.editor__fullscreen');
      if (full) {
        full.addEventListener('click', function () {
          var on = !editor.classList.contains('is-fullscreen');
          // 開いているものがあれば閉じてから開く（1 ページに 2 つ置く節がある）。
          closeFullscreen(false);
          if (on) setFullscreen(editor, true);
        });
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeFullscreen(true);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setup);
  } else {
    setup();
  }
})();
