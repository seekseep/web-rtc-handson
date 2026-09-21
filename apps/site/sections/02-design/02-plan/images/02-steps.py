# 02-steps.svg
# スキーマ: SOURCE-PATH-GOAL + SCALE（小さな完成を 3 段積み重ねる）
# お絵かきアプリを、それぞれ単体で動く 3 つの段に分けたことを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1080, 380)
c.text(540, 46, "3 つの段に分けて作る", scale="xl")

step1 = c.node(200, 210, "スタンプを置く", shape="sticky", color="blue", w=280, h=110)
step2 = c.node(540, 210, "相手に送る", shape="sticky", color="yellow", w=280, h=110)
step3 = c.node(880, 210, "線を描く", shape="sticky", color="green", w=280, h=110)

c.link(step1, step2)
c.link(step2, step3)

c.text(200, 138, "自分の画面だけ", scale="sm", fill=PALETTE["blue"]["text"])
c.text(540, 138, "リアルタイム通信", scale="sm", fill=PALETTE["yellow"]["text"])
c.text(880, 138, "お絵かきらしく", scale="sm", fill=PALETTE["green"]["text"])

c.text(540, 330, "どの段でも、いったん動くところまで作ってから次に進む", scale="sm")

c.save("02-steps.svg")
