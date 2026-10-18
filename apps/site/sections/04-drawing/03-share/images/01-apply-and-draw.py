# 01-apply-and-draw.svg
# スキーマ: SPLITTING（自分の操作 / 届いた指示）+ CENTER-PERIPHERY（apply が中心）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 380)

c.text(450, 46, "描くのは共通、送るかどうかだけが違う", scale="xl")

mine = c.node(140, 130, "自分の操作", emoji_cp="1f446", w=150, h=86)
recv = c.node(140, 290, "届いた指示", emoji_cp="1f4e5", w=150, h=86)

draw = c.sticky(320, 90, 200, 90, color="green")
c.text(draw.cx, 128, "draw", scale="lg", font="technical", fill=PALETTE["green"]["text"])
c.text(draw.cx, 156, "apply して送る", scale="sm")

apply = c.sticky(320, 250, 200, 90, color="blue")
c.text(apply.cx, 296, "apply", scale="lg", font="technical", fill=PALETTE["blue"]["text"])
c.text(apply.cx, 322, "描くだけ", scale="sm")

canvas = c.node(740, 210, "キャンバス", emoji_cp="1f5bc", w=160, h=90)

c.link(mine, draw)
c.link(recv, apply)
c.link(draw, canvas, label="描く", label_scale="sm")
c.link(apply, canvas, label="描く", label_scale="sm")
c.link(draw, apply, primary=False, label="呼ぶ", label_scale="sm")

c.text(450, 366, "届いた指示を送り返さないので、往復し続けることがない", scale="sm")

c.save("01-apply-and-draw.svg")
