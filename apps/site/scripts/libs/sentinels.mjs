/**
 * LECTURE.md 中のセンチネルを、実ファイルから生成したブロックへ展開するモジュール。
 * sync-lectures.mjs から呼ばれる（`./project.zip` 差し替えと同じ「sync 時展開」方式）。
 *
 * 対応センチネル:
 *
 *   ::codeview              … コードを簡易エディタ UI で表示する。左にファイル一覧、右にコード。
 *                             既定の対象は現在レクチャーの example/（＝「このステップの完成例」）で、
 *                             このときだけ ZIP ダウンロードボタンが付く。
 *   ::codeview{path="demos/on-vs-once"}   表示するディレクトリ（レクチャーからの相対パス）。
 *                                         既定は "example"。デモには配布 ZIP が無いので
 *                                         ボタンは出ない。
 *   ::codeview{defaultFile="main.js"}     最初に開くファイル（既定は先頭）。
 *   ::codeview[見出し]{...}                ヘッダの文言を上書きする（既定は example なら
 *                                         「このステップの完成例」、それ以外は「このデモのコード」）。
 *   ::codeview{base="none"}               「前の節との差分」ビューを出さない（章の起点）。
 *   ::codeview{base="03-connect/06-deploy"}  差分の相手を明示する。省略時は example を持つ
 *                                         1 つ前の節（libs/lecture-base.mjs が決める）。
 *                                         差分は example のときだけ。デモでは無視する。
 *
 *   ::assets                … 画像・音などの素材だけを配った ZIP のダウンロードボタンを置く。
 *                             対象は現在レクチャーの example/assets/（build-downloads.mjs が
 *                             `<sec>-<lec>-assets.zip` として出力する）。
 *   ::assets[ラベル]         … ボタンの文言を上書きできる（既定は「素材をダウンロード」）。
 *
 *   ::preview               … その場で遊べるライブプレビュー（iframe）を埋め込む。
 *   ::preview{src="<sec>/<lec>"}   別レクチャーの完成例を指定できる（省略時は現在レクチャー）。
 *   ::preview{demo="<name>"}       example/ ではなく demos/<name>/ を表示する。
 *                                  1 レクチャーに複数置けるので、1 ページに何個でも埋め込める。
 *   ::preview{height="220"}        iframe の高さ（px）を上書きする（既定は CSS の 480px）。
 *   ::preview[キャプション]{...}    figcaption を付けられる。
 *
 * 生成物: エディタは `::::editor{...}` コンテナ（remark-editor.mjs が <section class="editor">
 * に変換）＋コードフェンス。プレビューは生 HTML の <figure><iframe></figure>。
 */

import { readFile } from 'node:fs/promises';
import path from 'node:path';

import { walkFiles } from './fs-walk.mjs';
import { resolveBaseLecture } from './lecture-base.mjs';
import { diffLines } from './line-diff.mjs';
import {
  assetsDownloadUrlFor,
  downloadUrlFor,
  exampleDirOf,
  previewUrlFor,
} from './naming.mjs';
import { ROOT } from './paths.mjs';

const CODEVIEW_RE = /^::codeview(?:\[([^\]]*)\])?(?:\{([^}]*)\})?\s*$/;
const PREVIEW_RE = /^::preview(?:\[([^\]]*)\])?(?:\{([^}]*)\})?\s*$/;
const ASSETS_RE = /^::assets(?:\[([^\]]*)\])?(?:\{([^}]*)\})?\s*$/;

// ::codeview{path="..."} の既定値。ここだけが配布 ZIP を持つ。
const EXAMPLE_DIR = 'example';

const IGNORE_DIRS = new Set(['node_modules', '.git']);
const IGNORE_NAMES = new Set(['.DS_Store']);

// エディタに全文表示する（＝学習者が書く）コードの拡張子。
const CODE_EXT = new Map([
  ['.html', 'html'],
  ['.js', 'js'],
  ['.css', 'css'],
  ['.json', 'json'],
]);

// ファイル一覧の並び順（この順に先頭へ寄せる。残りは名前順）。
const PRIORITY = ['index.html', 'main.js'];

function sortFiles(rels) {
  return rels.slice().sort((a, b) => {
    const ai = PRIORITY.indexOf(a);
    const bi = PRIORITY.indexOf(b);
    if (ai !== -1 || bi !== -1) {
      if (ai === -1) return 1;
      if (bi === -1) return -1;
      return ai - bi;
    }
    return a.localeCompare(b);
  });
}

/** `key="value"` 形式のディレクティブ属性文字列を { key: value } に。 */
function parseAttrs(s) {
  const attrs = {};
  if (!s) return attrs;
  const re = /(\w+)\s*=\s*"([^"]*)"/g;
  let m;
  while ((m = re.exec(s))) attrs[m[1]] = m[2];
  return attrs;
}

/**
 * `path="..."` を正規化する。レクチャーディレクトリの外に出る指定は無効（null）。
 * 先頭・末尾の `/` は落とし、`example` / `demos/on-vs-once` の形にそろえる。
 */
function normalizeCodePath(input) {
  const rel = String(input ?? EXAMPLE_DIR)
    .trim()
    .replace(/^\/+|\/+$/g, '');
  if (!rel) return EXAMPLE_DIR;
  if (rel.split('/').some((seg) => seg === '..' || seg === '.')) return null;
  return rel;
}

/** 読めなければ null を返す readFile（差分の旧側は無いことがある）。 */
async function readIfExists(abs) {
  try {
    return await readFile(abs, 'utf8');
  } catch (e) {
    if (e.code === 'ENOENT') return null;
    throw e;
  }
}

/**
 * 1 ファイル分のコードフェンスを out に積む。「完成例」と「前の節との差分」の 2 本を出し、
 * remark-editor.mjs が data-file / data-view を見てペインに振り分ける。
 *
 * meta に付ける Expressive Code 向けの指定:
 *   frame="none"        … EC が「先頭付近のファイル名っぽいコメント」を拾って
 *                         その行を消してしまうのを止める（行番号が 1 行ずれる）。
 *   lang=<元の言語>      … text-markers が useDiffSyntax を立て、元の言語の
 *                         ハイライトを保ったまま `+` / `-` 行に色が付く。
 *   startLineNumber / startNewLineNumber … ec-line-numbers.mjs の旧/新 2 列のガター。
 */
async function pushFileFences(out, { rel, lang, content, baseAbs, where }) {
  out.push(
    '```' + lang + ' data-file="' + rel + '" data-view="code" frame="none"',
  );
  out.push(content);
  out.push('```');

  if (!baseAbs) return;
  const before = await readIfExists(path.join(baseAbs, ...rel.split('/')));
  const { lines, added, removed } = diffLines(
    before === null ? [] : before.replace(/\n+$/, '').split('\n'),
    content.split('\n'),
  );
  // 前の節から変えていないファイルは差分フェンスを出さない。
  // remark-editor.mjs が「変えていません」の一言に差し替える。
  if (added === 0 && removed === 0) return;
  if (before === null) {
    console.log(`[sentinels] ${where}/${rel} is new in this lecture`);
  }
  out.push(
    '```diff data-file="' +
      rel +
      '" data-view="diff" frame="none"' +
      ` lang=${lang} startLineNumber=1 startNewLineNumber=1`,
  );
  out.push(lines.join('\n'));
  out.push('```');
}

/**
 * コードのあるディレクトリから、簡易エディタ UI ブロック（Markdown）を作る。
 * ディレクトリが無い／コードファイルが 1 つも無ければ null。
 * zipUrl は配布 ZIP がある場合だけ渡す（デモには無い）。
 * baseAbs / baseLabel は差分ビューを出すときだけ渡す。
 */
async function buildEditorBlock({
  srcAbs,
  baseAbs,
  baseLabel,
  zipUrl,
  defaultFile,
  title,
  where,
}) {
  let all;
  try {
    all = await walkFiles(srcAbs, {
      ignoreDirs: IGNORE_DIRS,
      ignoreNames: IGNORE_NAMES,
    });
  } catch (e) {
    if (e.code === 'ENOENT') return null;
    throw e;
  }
  const codeFiles = sortFiles(
    all.filter((rel) => CODE_EXT.has(path.extname(rel).toLowerCase())),
  );
  if (codeFiles.length === 0) return null;

  // base 側にしか無いファイル（この節で消したファイル）はタブが無いので差分に出せない。
  // 黙って落とすと気づけないので警告だけ出す。
  if (baseAbs) {
    const baseFiles = await walkFiles(baseAbs, {
      ignoreDirs: IGNORE_DIRS,
      ignoreNames: IGNORE_NAMES,
    });
    for (const rel of baseFiles) {
      if (!CODE_EXT.has(path.extname(rel).toLowerCase())) continue;
      if (codeFiles.includes(rel)) continue;
      console.warn(
        `[sentinels] ${baseLabel} has ${rel} but ${where} does not (dropped from the diff)`,
      );
    }
  }

  const out = [];
  const zipAttr = zipUrl ? ` zip="${zipUrl}"` : '';
  const openAttr = defaultFile ? ` open="${defaultFile}"` : '';
  const diffAttr = baseAbs ? ` diff="${baseLabel}"` : '';
  out.push(`::::editor{title="${title}"${zipAttr}${openAttr}${diffAttr}}`);
  for (const rel of codeFiles) {
    const lang = CODE_EXT.get(path.extname(rel).toLowerCase());
    const content = (
      await readFile(path.join(srcAbs, ...rel.split('/')), 'utf8')
    ).replace(/\n+$/, '');
    await pushFileFences(out, { rel, lang, content, baseAbs, where });
  }
  out.push('::::');
  return out.join('\n');
}

/**
 * 素材 ZIP のダウンロードボタンの生 HTML を作る。空行を含めない（HTML ブロックを壊さないため）。
 * 何が入っているかが分かるよう、ファイル名も並べる。assets/ が無いレクチャーでは null。
 */
async function buildAssetsBlock({ exampleAbs, sec, lec, base, label }) {
  const assetsAbs = path.join(exampleAbs, 'assets');
  let files;
  try {
    files = await walkFiles(assetsAbs, {
      ignoreDirs: IGNORE_DIRS,
      ignoreNames: IGNORE_NAMES,
    });
  } catch (e) {
    if (e.code === 'ENOENT') return null;
    throw e;
  }
  if (files.length === 0) return null;

  const url = assetsDownloadUrlFor(base, sec, lec);
  const list = files
    .sort()
    .map((rel) => `<code>${rel}</code>`)
    .join('、');
  return (
    `<div class="assets-download">` +
    `<a class="download-button" href="${url}" download>` +
    `<span class="download-button__icon" aria-hidden="true"></span>` +
    `<span class="download-button__label">${label || '素材をダウンロード'}</span>` +
    `</a>` +
    `<p class="assets-download__files">中身（${files.length} ファイル）: ${list}` +
    `<br />解凍してできる <code>assets/</code> を <code>app/</code> の中に置いてください。</p>` +
    `</div>`
  );
}

/** ライブプレビュー（iframe）の生 HTML を作る。空行を含めない（HTML ブロックを壊さないため）。 */
function buildPreviewBlock({ base, sec, lec, demo, caption, height }) {
  const src = previewUrlFor(base, sec, lec, demo);
  const cap = caption
    ? `<figcaption class="lecture-preview__caption">${caption}</figcaption>`
    : '';
  // 高さは CSS（.lecture-preview__frame）の既定 480px を inline style で上書きする。
  const style = /^\d+$/.test(String(height ?? ''))
    ? ` style="height:${height}px"`
    : '';
  return (
    `<figure class="lecture-preview">` +
    `<div class="lecture-preview__bar">` +
    `<button type="button" class="lecture-preview__reload" title="プレビューを再読み込み">↻ 再読み込み</button>` +
    `</div>` +
    `<iframe class="lecture-preview__frame" src="${src}" title="ライブプレビュー" loading="lazy"${style}></iframe>` +
    cap +
    `</figure>`
  );
}

/**
 * 本文中の `::codeview` / `::assets` / `::preview` センチネルを展開する。
 * current = { sec, lec }（このレクチャー）。lecture 以外の docs では素通しする。
 *
 * base はサイトの公開パス接頭辞（`/web-rtc-handson`）。差分の相手のレクチャーは
 * baseLectureRel と呼んで区別する（名前が紛らわしいので混同しないこと）。
 * lectureRel / exampleLectures は差分ビューの相手を決めるために使う。
 */
export async function expandSentinels(
  body,
  { lectureAbsDir, lectureRel, exampleLectures = [], sec, lec, base },
) {
  if (!sec || !lec) return body;
  const exampleAbs = path.join(lectureAbsDir, EXAMPLE_DIR);
  const where = `sections/${sec}/${lec}`;

  const lines = body.split('\n');
  const out = [];
  for (const line of lines) {
    const cv = line.match(CODEVIEW_RE);
    if (cv) {
      const attrs = parseAttrs(cv[2]);
      const rel = normalizeCodePath(attrs.path);
      if (!rel) {
        console.warn(
          `[sentinels] ::codeview has an invalid path="${attrs.path}" in ${where} (skipped)`,
        );
        continue;
      }
      const isExample = rel === EXAMPLE_DIR;
      // 差分ビューを出すのは完成例だけ。デモには「前の節」が無い。
      let baseLectureRel = null;
      if (isExample) {
        baseLectureRel = resolveBaseLecture(
          exampleLectures,
          lectureRel,
          attrs.base,
          where,
        );
      } else if (attrs.base) {
        console.warn(
          `[sentinels] ::codeview{path="${rel}"} ignores base="${attrs.base}" in ${where}`,
        );
      }
      const block = await buildEditorBlock({
        srcAbs: path.join(lectureAbsDir, ...rel.split('/')),
        baseAbs: baseLectureRel
          ? path.join(ROOT, ...exampleDirOf(baseLectureRel).split('/'))
          : null,
        baseLabel: baseLectureRel
          ? baseLectureRel.replace(/^sections\//, '')
          : null,
        // 配布 ZIP があるのは example/ だけ（build-downloads.mjs の対象）。
        zipUrl: isExample ? downloadUrlFor(base, sec, lec) : null,
        defaultFile: attrs.defaultFile,
        title: cv[1]
          ? cv[1].trim()
          : isExample
            ? 'このステップの完成例'
            : 'このデモのコード',
        where,
      });
      if (block) {
        out.push(block);
        continue;
      }
      console.warn(
        `[sentinels] ::codeview but no code in ${where}/${rel} (skipped)`,
      );
      continue;
    }
    const as = line.match(ASSETS_RE);
    if (as) {
      const label = as[1] ? as[1].trim() : '';
      const block = await buildAssetsBlock({
        exampleAbs,
        sec,
        lec,
        base,
        label,
      });
      if (block) {
        out.push(block);
        continue;
      }
      console.warn(
        `[sentinels] ::assets but no example/assets in ${where} (skipped)`,
      );
      continue;
    }
    const pv = line.match(PREVIEW_RE);
    if (pv) {
      const caption = pv[1] ? pv[1].trim() : '';
      const attrs = parseAttrs(pv[2]);
      let tSec = sec;
      let tLec = lec;
      if (attrs.src) {
        const parts = attrs.src.split('/');
        if (parts.length === 2) {
          tSec = parts[0];
          tLec = parts[1];
        }
      }
      out.push(
        buildPreviewBlock({
          base,
          sec: tSec,
          lec: tLec,
          demo: attrs.demo,
          caption,
          height: attrs.height,
        }),
      );
      continue;
    }
    out.push(line);
  }
  return out.join('\n');
}
