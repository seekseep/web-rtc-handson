# 01-tradeoff.svg
# スキーマ: BALANCE（オリジナリティと難しさの引っぱり合い）
# 工夫を足すほど難しくなるので、要件がつり合う場所で止めることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(980, 360)
c.text(490, 46, "工夫を足すほど、難しくなる", scale="xl")

orig = c.node(170, 190, "オリジナリティ", emoji_cp="1f4a1", w=220, h=100)  # 💡
hard = c.node(810, 190, "難しさ", emoji_cp="1f9e9", w=220, h=100)  # 🧩
mid = c.node(490, 190, "要件で\n止める", shape="diamond", color="yellow", w=180, h=130)

c.link(mid, orig, label="違いが出る")
c.link(mid, hard, label="解ける人が減る")

c.text(490, 330, "「難しすぎない」「リテラシーを求めない」とぶつかる手前が、止めどころ",
       scale="sm")

c.save("01-tradeoff.svg")
