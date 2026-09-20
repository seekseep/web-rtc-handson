# 00-thumbnail.svg
# スキーマ: SCALE（動く状態を 1 段ずつ積み上げる）
# 「一気に作らず、毎回動く状態で終わる」を階段で見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 360)
c.text(480, 46, "動く状態を、1 段ずつ積む", scale="xl")

steps = [
    (130, 262, "光る", "1f4a1"),  # 💡
    (300, 226, "2 つにする", "1f4a1"),  # 💡
    (470, 190, "つなぐ", "1f517"),  # 🔗
    (640, 154, "描く", "1f5bc"),  # 🖼️
    (810, 118, "2 台で", "1f4f1"),  # 📱
]

nodes = []
for cx, cy, label, cp in steps:
    nodes.append(c.node(cx, cy, label, emoji_cp=cp, w=120, h=80))

for a, b in zip(nodes, nodes[1:]):
    c.link(a, b, primary=False)

c.text(480, 344, "どの段でも、そこで止めれば動くものが手元に残る", scale="sm")

c.save("00-thumbnail.svg")
