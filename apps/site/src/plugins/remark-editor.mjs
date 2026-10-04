/**
 * `::::editor{title="..." zip="URL" open="main.js" diff="03-connect/01-light"}` コンテナ
 * ディレクティブを、簡易エディタ UI `<section class="editor">`（左=ファイル一覧・右=コード）
 * に変換する remark プラグイン。
 *
 * 属性:
 *   title … ヘッダの文言（省略時は「このステップの完成例」）
 *   zip   … ZIP ダウンロードボタンのリンク先。省略するとボタンを出さない（デモなど配布物が無い場合）
 *   open  … 最初に開くファイル名（省略時は先頭）
 *   diff  … 差分の相手（`<sec>/<lec>`）。あるときだけ「前の節との差分」ボタンを出す
 *
 * コンテナの中身は sync-lectures.mjs（libs/sentinels.mjs）が実ファイルから生成した
 * コードフェンス。各 fence の meta に `data-file="<相対パス>"` と `data-view="code|diff"` が
 * 付いていて、1 ファイルにつき「完成例」と「差分」の 2 本が来る（変えていないファイルは
 * 完成例だけ）。このプラグインは:
 *   - meta から data-file / data-view を読んで取り除く。残りは Expressive Code 宛ての
 *     指定（frame / lang / startLineNumber）なのでそのまま渡す
 *   - 左のファイル切り替えボタン、右のコードペイン（ファイル × ビュー）を組み立てる
 *   - ヘッダにビュー切り替え・全画面・ZIP ダウンロードのボタンを付ける
 * 切り替えの挙動は site/src/scripts/editor-client.js（全ページに inline 注入）。
 * 装飾は site/src/styles/editor.css。
 *
 * NOTE: 中で ZIP ボタンを自前生成するため remark-download には依存しない。
 * コンテナは 4 コロン（::::）で開く（中にコードフェンスを含むため 3 コロンでもよいが統一）。
 */

const NAME = 'editor';
const FILE_META_RE = /\s*data-file="([^"]*)"/;
const VIEW_META_RE = /\s*data-view="([^"]*)"/;
const DEFAULT_TITLE = 'このステップの完成例';

function visit(node, callback) {
  if (!node || !Array.isArray(node.children)) return;
  for (const child of node.children) {
    callback(child);
    visit(child, callback);
  }
}

function el(hName, className, children, extraProps = {}) {
  return {
    type: 'element',
    data: { hName, hProperties: { className, ...extraProps } },
    children: children || [],
  };
}

function text(value) {
  return { type: 'text', value };
}

/** remark-download と同じ見た目の ZIP ダウンロードボタンを作る。 */
function downloadButton(zipUrl) {
  return {
    type: 'element',
    data: {
      hName: 'a',
      hProperties: {
        className: ['download-button'],
        href: zipUrl,
        download: true,
      },
    },
    children: [
      el('span', ['download-button__icon'], [], { 'aria-hidden': 'true' }),
      el('span', ['download-button__label'], [text('コードをダウンロード')]),
    ],
  };
}

/** 「前の節との差分」の切り替えボタン。押した結果は .editor[data-view] に出る。 */
function diffButton(baseLabel) {
  return el(
    'button',
    ['editor__action', 'editor__diff'],
    [text('前の節との差分')],
    {
      type: 'button',
      'aria-pressed': 'false',
      title: `${baseLabel} との差分を出す`,
    },
  );
}

export default function remarkEditor() {
  return (tree) => {
    visit(tree, (node) => {
      if (node.type !== 'containerDirective') return;
      if (node.name !== NAME) return;

      const attrs = node.attributes || {};
      const zipUrl = attrs.zip;
      const baseLabel = attrs.diff;

      // コードフェンスをファイル名でまとめる（1 ファイルに完成例と差分の 2 本が来る）。
      const names = [];
      const byName = new Map();
      node.children
        .filter((c) => c.type === 'code')
        .forEach((code, i) => {
          const meta = code.meta || '';
          const fm = meta.match(FILE_META_RE);
          const vm = meta.match(VIEW_META_RE);
          const name = fm ? fm[1] : code.lang || `file${i}`;
          const view = vm && vm[1] === 'diff' ? 'diff' : 'code';
          // data-* は自前の目印なので落とす。残りは Expressive Code 宛てなので通す。
          const rest = meta
            .replace(FILE_META_RE, '')
            .replace(VIEW_META_RE, '')
            .trim();
          code.meta = rest || null;
          if (!byName.has(name)) {
            byName.set(name, {});
            names.push(name);
          }
          byName.get(name)[view] = code;
        });

      // デフォルトで開くファイル（open 属性で指定）。無ければ先頭。
      let activeIndex = attrs.open ? names.indexOf(attrs.open) : -1;
      if (activeIndex === -1) activeIndex = 0;

      const fileButtons = names.map((name, i) =>
        el(
          'button',
          ['editor__file', ...(i === activeIndex ? ['is-active'] : [])],
          [text(name)],
          {
            type: 'button',
            'data-file': name,
            // 差分ビューのとき、変えたファイルに印を付けるための目印。
            ...(baseLabel && byName.get(name).diff
              ? { 'data-changed': 'true' }
              : {}),
          },
        ),
      );

      const panes = [];
      names.forEach((name, i) => {
        const active = i === activeIndex ? ['is-active'] : [];
        const found = byName.get(name);
        if (found.code) {
          panes.push(
            el('div', ['editor__pane', ...active], [found.code], {
              'data-file': name,
              'data-view': 'code',
            }),
          );
        }
        if (!baseLabel) return;
        // 差分ペインは検索の対象から外す。前の節のコード（`-` 行）が索引に入ると、
        // 古い文字列で新しい節がヒットしてしまう。
        panes.push(
          el(
            'div',
            ['editor__pane', ...active],
            found.diff
              ? [found.diff]
              : [
                  el(
                    'p',
                    ['editor__nochange'],
                    [text('この節では、このファイルを変えていません。')],
                  ),
                ],
            {
              'data-file': name,
              'data-view': 'diff',
              'data-pagefind-ignore': 'true',
            },
          ),
        );
      });

      const headerChildren = [
        el('span', ['editor__title'], [text(attrs.title || DEFAULT_TITLE)]),
      ];
      if (baseLabel) headerChildren.push(diffButton(baseLabel));
      headerChildren.push(
        el(
          'button',
          ['editor__action', 'editor__fullscreen'],
          [text('全画面')],
          {
            type: 'button',
            'aria-pressed': 'false',
            title: '全画面で表示（Esc で戻る）',
          },
        ),
      );
      if (zipUrl) headerChildren.push(downloadButton(zipUrl));

      const header = el('div', ['editor__header'], headerChildren);
      const body = el(
        'div',
        ['editor__body'],
        [
          el('div', ['editor__files'], fileButtons),
          el('div', ['editor__code'], panes),
        ],
      );

      node.type = 'editorContainer';
      node.data = {
        hName: 'section',
        // JS が動かない環境でも完成例が見えるよう、初期ビューを HTML 側で決めておく。
        hProperties: { className: ['editor'], 'data-view': 'code' },
      };
      node.children = [header, body];
    });
  };
}
