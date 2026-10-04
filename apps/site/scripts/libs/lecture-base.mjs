/**
 * 「この節の example の、1 つ前はどれか」を決めるモジュール。
 *
 * 差分の旧側（`::codeview` の差分ビュー、`:::code{... newOffset=N}` の `-` 行）は、
 * 既定では「example を持つ節を教材順に並べたときの 1 つ前」＝章をまたぐ。
 * ただし章の切り替わりではアプリが別物になる（05-drawing/01-canvas の 1 つ前は
 * 03-connect/06-deploy のライトアプリ）ので、LECTURE.md 側で上書きできるようにする:
 *
 *   ::codeview{base="none"}                  … 差分を出さない（章の起点）
 *   ::codeview{base="03-connect/06-deploy"}  … 明示指定
 *
 * sync-lectures（libs/sentinels.mjs）と check-lectures.mjs が同じ答えを見るために、
 * 解決はこのモジュールに一本化する。
 */

import { glob } from 'node:fs/promises';
import path from 'node:path';

import { ROOT } from './paths.mjs';

// 行頭から行末までが `::codeview` 単独行であること（sentinels.mjs の CODEVIEW_RE と同じ形）。
const CODEVIEW_LINE_RE = /^::codeview(?:\[[^\]]*\])?(?:\{([^}]*)\})?\s*$/gm;
// `key="value"`（sentinels.mjs の parseAttrs と同じ形。循環 import を避けて持つ）。
const ATTR_RE = /(\w+)\s*=\s*"([^"]*)"/g;

/** example/ を持つレクチャー（`sections/<sec>/<lec>`）を、教材の順に並べて返す。 */
export async function lecturesWithExample() {
  const found = [];
  for await (const hit of glob('sections/*/*/example/index.html', {
    cwd: ROOT,
  })) {
    const rel = hit.split(path.sep).join('/');
    found.push(path.posix.dirname(path.posix.dirname(rel)));
  }
  return found.sort();
}

/**
 * LECTURE.md 本文から、example の `::codeview` が指定した base 属性を読む。
 * `path=` 付き（demos のコード表示）は完成例ではないので対象外。指定が無ければ undefined。
 */
export function readCodeviewBase(body) {
  for (const m of body.matchAll(CODEVIEW_LINE_RE)) {
    const attrs = {};
    for (const a of (m[1] || '').matchAll(ATTR_RE)) attrs[a[1]] = a[2];
    if (attrs.path && attrs.path !== 'example') continue;
    if (attrs.base) return attrs.base;
  }
  return undefined;
}

/**
 * 差分の旧側になるレクチャー（`sections/<sec>/<lec>`）を返す。無ければ null。
 *
 * @param {string[]} ordered    lecturesWithExample() の戻り値
 * @param {string}   lectureRel `sections/<sec>/<lec>`
 * @param {string=}  baseAttr   `::codeview{base="..."}` の値（未指定なら 1 つ前の節）
 * @param {string=}  where      警告に出す場所
 * @returns {string|null}
 */
export function resolveBaseLecture(ordered, lectureRel, baseAttr, where) {
  if (baseAttr === 'none') return null;
  if (baseAttr) {
    const rel =
      'sections/' +
      baseAttr.replace(/^\/+|\/+$/g, '').replace(/^sections\//, '');
    if (ordered.includes(rel)) return rel;
    console.warn(
      `[lecture-base] base="${baseAttr}" has no example/ (${where || lectureRel})`,
    );
    return null;
  }
  const index = ordered.indexOf(lectureRel);
  return index > 0 ? ordered[index - 1] : null;
}
