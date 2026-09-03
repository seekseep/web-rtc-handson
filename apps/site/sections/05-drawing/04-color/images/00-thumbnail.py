# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（色を指示に含めて送る）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "色は、描いた人が決める", scale="xl")

for i, col in enumerate(["red", "orange", "green", "blue", "purple"]):
    c.ellipse(110 + i * 52, 150, 22, 22, color=col)
c.text(214, 210, "選ぶのは自分", scale="sm")
c.sticky(390, 118, 250, 66, color="yellow")
c.text(515, 158, "{ color: '#e5484d' }", scale="sm", font="technical", fill=PALETTE["yellow"]["text"])
c.node(780, 150, "あいて", emoji_cp="1f310", w=110, h=76)
c.connector(340, 150, 382, 150)
c.connector(648, 150, 726, 150, label="送る", label_scale="sm")
c.text(450, 268, "指示に色を入れるから、両方の画面が同じ絵になる", scale="sm")

c.save("00-thumbnail.svg")
