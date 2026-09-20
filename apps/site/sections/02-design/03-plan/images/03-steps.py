# 03-steps.svg
# スキーマ: SOURCE-PATH-GOAL（3 段のステップ）
# 03 章・04 章・05 章に対応させ、この教材の進み方そのものを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1080, 370)
c.text(540, 46, "3 つの段にわけて作る", scale="xl")

step1 = c.node(200, 200, "相手の画面が光る", shape="sticky", color="blue", w=280, h=110)
step2 = c.node(540, 200, "しくみを理解する", shape="sticky", color="yellow", w=280, h=110)
step3 = c.node(880, 200, "お絵かきを完成させる", shape="sticky", color="green", w=280, h=110)

c.link(step1, step2)
c.link(step2, step3)

c.text(200, 128, "03 章", scale="sm", fill=PALETTE["blue"]["text"])
c.text(540, 128, "04 章", scale="sm", fill=PALETTE["yellow"]["text"])
c.text(880, 128, "05 章", scale="sm", fill=PALETTE["green"]["text"])

c.text(540, 320, "小さな成功を積み重ねて、最後のアプリにたどり着く", scale="sm")

c.save("03-steps.svg")
