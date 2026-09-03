#!/usr/bin/env node
/**
 * LECTURE.md の `:::code{filepath=... offset=...}` が、example/ の実ファイルの
 * 該当行と一致しているかを検査する。
 *
 * 本文にコードを書き写している唯一の場所がこのディレクティブなので（::codeview /
 * ::preview は実ファイルから生成される）、example/ を直したときにここだけ
 * 取り残されるのを防ぐ。
 *
 * - 通常のブロック … offset 行目から、本文の内容がそのまま現れるか
 * - diff ブロック  … `+`/文脈行が newOffset から現れるか（その節の example）、
 *                    `-`/文脈行が offset から現れるか（1 つ前の節の example）
 *
 * インデントの差は無視して比較する（本文では周囲のインデントを落として書くため）。
 */

import { glob, readFile } from 'node:fs/promises';
import path from 'node:path';

import { ROOT } from './libs/paths.mjs';

const BLOCK =
  /^:::code(?:\[[^\]]*\])?\{([^}]*)\}\s*\n\n?```(\w+)\n([\s\S]*?)```\s*\n\n?:::/gm;

/** example/ を持つレクチャー（sections/<sec>/<lec>）を、教材の順に並べて返す。 */
async function lecturesWithExample() {
  const found = [];
  for await (const hit of glob('sections/*/*/example/index.html', {
    cwd: ROOT,
  })) {
    found.push(path.dirname(path.dirname(hit)));
  }
  return found.sort();
}

/** すべての LECTURE.md（sections/<sec>/<lec>）を教材の順に並べて返す。 */
async function allLectures() {
  const found = [];
  for await (const hit of glob('sections/*/*/LECTURE.md', { cwd: ROOT })) {
    found.push(path.dirname(hit));
  }
  return found.sort();
}

async function readLines(rel) {
  try {
    return (await readFile(path.join(ROOT, rel), 'utf8')).split('\n');
  } catch {
    return null;
  }
}

/** lines が actual の offset 行目から現れるか。ズレていれば最初の食い違いを返す。 */
function firstMismatch(actual, lines, offset) {
  const want = [...lines];
  while (want.length && want.at(-1).trim() === '') want.pop();

  for (const [i, line] of want.entries()) {
    const lineNumber = offset + i;
    const got = actual[lineNumber - 1] ?? '<EOF>';
    if (got.trim() !== line.trim()) {
      return { lineNumber, want: line.trim(), got: got.trim() };
    }
  }
  return null;
}

const withExample = await lecturesWithExample();
const problems = [];
let checked = 0;

for (const lectureRel of await allLectures()) {
  const md = await readLines(path.join(lectureRel, 'LECTURE.md'));
  if (!md) continue;

  // 差分の「旧」側は、example を持つ節のうち 1 つ前のもの（章はまたぐ）
  const index = withExample.indexOf(lectureRel);
  const previousRel = index > 0 ? withExample[index - 1] : null;

  for (const m of md.join('\n').matchAll(BLOCK)) {
    const attrs = Object.fromEntries(
      [...m[1].matchAll(/(\w+)=([^\s}]+)/g)].map(([, k, v]) => [k, v]),
    );
    if (!attrs.filepath || !attrs.offset) continue;

    const code = m[3].replace(/\n$/, '').split('\n');
    const targets =
      m[2] === 'diff'
        ? [
            {
              rel: lectureRel,
              lines: code
                .filter((l) => !l.startsWith('-'))
                .map((l) => l.slice(1)),
              offset: Number(attrs.newOffset ?? attrs.offset),
              kind: 'newOffset',
            },
            {
              rel: previousRel,
              lines: code
                .filter((l) => !l.startsWith('+'))
                .map((l) => l.slice(1)),
              offset: Number(attrs.offset),
              kind: 'offset（1 つ前の節）',
            },
          ]
        : [
            {
              rel: lectureRel,
              lines: code,
              offset: Number(attrs.offset),
              kind: 'offset',
            },
          ];

    for (const target of targets) {
      if (!target.rel) continue;
      const file = path.join(target.rel, 'example', attrs.filepath);
      const actual = await readLines(file);
      if (!actual) {
        problems.push(`${lectureRel}  ${attrs.filepath} … ${file} が無い`);
        continue;
      }
      checked += 1;
      const bad = firstMismatch(actual, target.lines, target.offset);
      if (bad) {
        problems.push(
          `${lectureRel}  ${attrs.filepath} ${target.kind}=${target.offset}\n` +
            `    ${bad.lineNumber} 行目 本文: ${bad.want.slice(0, 70)}\n` +
            `             実物: ${bad.got.slice(0, 70)}`,
        );
      }
    }
  }
}

if (problems.length) {
  console.error('[check-lectures] 本文の :::code と example/ がズレています\n');
  console.error(problems.join('\n'));
  console.error(`\n${checked} ブロック中 ${problems.length} 件`);
  process.exit(1);
}

console.log(`[check-lectures] ${checked} ブロック すべて example/ と一致`);
