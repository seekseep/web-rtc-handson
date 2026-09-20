# 07-roadmap.svg
# スキーマ: SOURCE-PATH-GOAL × 2 段（03 章の 6 節と 05 章の 8 節を、1 本の道として）
# 「1 節 = 1 つの動く状態」で、14 個の小さな段に割ってあることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1180, 390)
c.text(590, 46, "14 の節は、14 個の「動く状態」", scale="xl")

c.text(80, 104, "03 章", scale="lg", fill=PALETTE["blue"]["text"], align="left")
c.text(190, 104, "ボタンで光る", scale="sm", align="left")

row1 = ["ライト", "色が変わる", "2 つになる", "つながる", "色が届く", "2 台で動く"]
nodes1 = []
for i, label in enumerate(row1):
    nodes1.append(
        c.node(122 + i * 187, 158, label, shape="sticky", color="blue", w=124, h=54)
    )
for a, b in zip(nodes1, nodes1[1:]):
    c.link(a, b, primary=False)

c.text(80, 250, "05 章", scale="lg", fill=PALETTE["green"]["text"], align="left")
c.text(190, 250, "お絵かき", scale="sm", align="left")

row2 = ["スタンプ", "つなぐ", "届く", "線", "色", "けしごむ", "ぜんぶ消す", "公開"]
nodes2 = []
for i, label in enumerate(row2):
    nodes2.append(
        c.node(118 + i * 134, 304, label, shape="sticky", color="green", w=116, h=54)
    )
for a, b in zip(nodes2, nodes2[1:]):
    c.link(a, b, primary=False)

c.text(590, 368, "前の節に 1 つだけ足す。足したら必ず動かして確かめる", scale="sm")

c.save("07-roadmap.svg")
