# 04-steps.svg
# スキーマ: SOURCE-PATH-GOAL + SCALE（遊びの芯から 4 段で育てる）＋ PART-WHOLE（ロジックと装飾）
# ロジックを先に動かし、装飾はあとから足すことを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1120, 420)
c.text(560, 46, "遊びの芯から、4 段で育てる", scale="xl")

s1 = c.node(150, 190, "線を引いて\n判定する", shape="sticky", color="blue", w=210, h=110)
s2 = c.node(420, 190, "壁と\nスイッチ", shape="sticky", color="blue", w=210, h=110)
s3 = c.node(690, 190, "ステージ選択と\n進み具合", shape="sticky", color="yellow", w=210, h=110)
s4 = c.node(960, 190, "100 ステージ", shape="sticky", color="green", w=210, h=110)

c.link(s1, s2)
c.link(s2, s3)
c.link(s3, s4)

c.text(285, 112, "ゲームのロジック", scale="md", fill=PALETTE["blue"]["text"])

deco = c.sticky(60, 290, 1000, 62, color="gray", weight="thin", dash="dashed")
c.text(560, 328, "装飾（色・効果音・振動・画面の演出）は、ロジックが動いてからあとで足す",
       scale="md")

c.text(560, 396, "どの段でも、いったん遊べるところまで作ってから次に進む", scale="sm")

c.save("04-steps.svg")
