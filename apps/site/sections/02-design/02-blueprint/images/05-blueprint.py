# 05-blueprint.svg
# スキーマ: SOURCE-PATH-GOAL + SPLITTING（手 → 指示 → 2 つの画面へ分岐）
# 「自分の画面も、相手の画面も、同じ指示を同じ関数で描く」を 1 枚にする

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(980, 360)
c.text(490, 46, "決めたことを 1 枚にすると、これだけ", scale="xl")

hand = c.node(100, 180, "指を動かす", emoji_cp="1f590", w=130, h=88)  # 🖐️
order = c.node(320, 180, "指示にする", shape="sticky", color="yellow", w=150, h=88)

mine = c.node(580, 106, "自分の画面", emoji_cp="1f5bc", w=130, h=86)  # 🖼️
wire = c.node(580, 262, "相手へ送る", emoji_cp="1f4e1", w=130, h=86)  # 📡
theirs = c.node(830, 262, "相手の画面", emoji_cp="1f5bc", w=130, h=86)  # 🖼️

c.link(hand, order)
c.link(order, mine, label="描く")
c.link(order, wire, label="送る")
c.link(wire, theirs, label="描く")

c.text(490, 336, "同じ指示を同じやり方で描くから、2 つの画面は必ず同じ絵になる", scale="sm")

c.save("05-blueprint.svg")
