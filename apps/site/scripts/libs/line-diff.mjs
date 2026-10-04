/**
 * 行単位の差分（LCS）を作るモジュール。
 * `::codeview` の差分ビューが「前の節の example」と「この節の example」を比べるのに使う。
 *
 * diff パッケージを足さないのは、pnpm の構成上 apps/site から import できないため。
 * example はいちばん大きい節でも数百行なので、素朴な O(n*m) の DP で十分間に合う。
 */

/**
 * a[i..] と b[j..] の最長共通部分列の長さの表（(n+1)*(m+1) の 1 次元配列）。
 * 後ろから埋めるので、前から読み進めながら「どちらを消費するか」を決められる。
 */
function lcsTable(a, b) {
  const width = b.length + 1;
  const table = new Int32Array((a.length + 1) * width);
  for (let i = a.length - 1; i >= 0; i--) {
    for (let j = b.length - 1; j >= 0; j--) {
      table[i * width + j] =
        a[i] === b[j]
          ? table[(i + 1) * width + j + 1] + 1
          : Math.max(table[(i + 1) * width + j], table[i * width + j + 1]);
    }
  }
  return table;
}

/**
 * oldLines → newLines の差分を、先頭 1 文字がマーカーの行配列で返す。
 *   ' ' … 両方にある行   '-' … 前の節にだけある行   '+' … この節で増えた行
 *
 * 変えていない行にも必ず半角スペースを置くのは、Expressive Code の text-markers が
 * 「全行に共通する先頭の空白」を数えてから 1 文字だけ削る作りのため。マーカーの無い行が
 * 1 つでも混ざると共通の空白が 0 文字と判定され、`+` / `-` が本文に残ってしまう。
 * 同じ理由で、内容そのものが `-` / `+` で始まる行があると崩れる（今の example には無い）。
 *
 * `---` / `+++` / `@@` のような unified diff のヘッダは付けないこと。付けると
 * text-markers が「本物の diff ファイル」と判定して、着色もマーカー剥がしもやめてしまう。
 *
 * @param {string[]} oldLines 前の節の内容（行配列。改行文字は含まない）
 * @param {string[]} newLines この節の内容
 * @returns {{ lines: string[], added: number, removed: number }}
 */
export function diffLines(oldLines, newLines) {
  // 前後の一致部分は DP にかけない。節ごとの差分は数行なので、ここでほとんどが落ちる。
  let head = 0;
  while (
    head < oldLines.length &&
    head < newLines.length &&
    oldLines[head] === newLines[head]
  ) {
    head += 1;
  }
  let tail = 0;
  while (
    tail < oldLines.length - head &&
    tail < newLines.length - head &&
    oldLines[oldLines.length - 1 - tail] ===
      newLines[newLines.length - 1 - tail]
  ) {
    tail += 1;
  }

  const a = oldLines.slice(head, oldLines.length - tail);
  const b = newLines.slice(head, newLines.length - tail);
  const table = lcsTable(a, b);
  const width = b.length + 1;

  const lines = [];
  let added = 0;
  let removed = 0;

  for (let k = 0; k < head; k += 1) lines.push(' ' + oldLines[k]);

  let i = 0;
  let j = 0;
  while (i < a.length || j < b.length) {
    if (i < a.length && j < b.length && a[i] === b[j]) {
      lines.push(' ' + a[i]);
      i += 1;
      j += 1;
      continue;
    }
    // 同じ塊の中では `-` を先に出して、本文の `:::code` 差分ブロックと並びをそろえる。
    const takeOld =
      j >= b.length ||
      (i < a.length && table[(i + 1) * width + j] >= table[i * width + j + 1]);
    if (takeOld) {
      lines.push('-' + a[i]);
      i += 1;
      removed += 1;
    } else {
      lines.push('+' + b[j]);
      j += 1;
      added += 1;
    }
  }

  for (let k = newLines.length - tail; k < newLines.length; k += 1) {
    lines.push(' ' + newLines[k]);
  }

  return { lines, added, removed };
}
