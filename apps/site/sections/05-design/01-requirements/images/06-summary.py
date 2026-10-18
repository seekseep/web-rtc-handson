# 06-summary.svg
# スキーマ: CENTER-PERIPHERY（中心に置くものと、その外側に出すもの）
# 見た目や時間のスリルではなく、ルールで面白くすると決めたことを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(1000, 540)
c.text(500, 46, "中心に置くものを、1 つに決める", scale="xl")

core = c.node(500, 285, "ルールで\n面白くする", shape="ellipse", color="blue",
              w=260, h=150)

easy = c.node(160, 145, "難しすぎない", emoji_cp="1f9e9", w=200, h=80)  # 🧩
gap = c.node(160, 285, "スキマ時間に遊べる", emoji_cp="1f683", w=220, h=80)  # 🚃
lit = c.node(160, 425, "リテラシーを求めない", emoji_cp="1f44d", w=220, h=80)  # 👍

rich = c.node(850, 205, "豪華な見た目", shape="sticky", color="gray", w=200, h=80)
thrill = c.node(850, 365, "時間のスリル", shape="sticky", color="gray", w=200, h=80)

c.link(easy, core, primary=False)
c.link(gap, core, primary=False)
c.link(lit, core, primary=False)
c.link(core, rich, dash="dashed", primary=False, label="使わない")
c.link(core, thrill, dash="dashed", primary=False, label="使わない")

c.text(500, 522, "画像も時間もないから、盤面のルールに工夫を集める。ただし難しくしすぎない",
       scale="sm")

c.save("06-summary.svg")
