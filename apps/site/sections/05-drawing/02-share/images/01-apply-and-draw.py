# 01-apply-and-draw.svg
# スキーマ: SPLITTING（自分の操作 / 届いた指示）+ CENTER-PERIPHERY（apply が中心）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 380)

c.text(450, 46, "描くのは共通、送るかどうかだけが違う", scale="xl")
c.node(140, 130, "自分の操作", emoji_cp="1f446", w=150, h=86)
c.node(140, 290, "届いた指示", emoji_cp="1f4e5", w=150, h=86)
c.sticky(320, 90, 200, 90, color="green")
c.text(420, 128, "draw", scale="lg", font="technical", fill=PALETTE["green"]["text"])
c.text(420, 156, "apply して送る", scale="sm")
c.sticky(320, 250, 200, 90, color="blue")
c.text(420, 296, "apply", scale="lg", font="technical", fill=PALETTE["blue"]["text"])
c.text(420, 322, "描くだけ", scale="sm")
c.node(740, 210, "キャンバス", emoji_cp="1f5bc", w=160, h=90)
c.connector(222, 130, 312, 130)
c.connector(222, 290, 312, 290)
c.connector(528, 140, 668, 190, label="描く", label_scale="sm")
c.connector(528, 290, 668, 240, label="描く", label_scale="sm")
c.connector(420, 186, 420, 244, primary=False, label="呼ぶ", label_scale="sm")
c.text(450, 366, "届いた指示を送り返さないので、往復し続けることがない", scale="sm")

c.save("01-apply-and-draw.svg")
