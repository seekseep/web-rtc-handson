# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（色を指示に含めて送る）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "色は、描いた人が決める", scale="xl")

dots = [c.ellipse(110 + i * 52, 150, 22, 22, color=col)
        for i, col in enumerate(["red", "orange", "green", "blue", "purple"])]
c.text(214, 210, "選ぶのは自分", scale="sm")
msg = c.sticky(390, 118, 250, 66, color="yellow")
c.text(515, 158, "{ color: '#e5484d' }", scale="sm", font="technical", fill=PALETTE["yellow"]["text"])
you = c.node(780, 150, "相手", emoji_cp="1f4bb", w=110, h=76)

c.link(dots[-1], msg)
c.link(msg, you, label="送る", label_scale="sm")
c.text(450, 268, "指示に色を入れるから、両方の画面が同じ絵になる", scale="sm")

c.save("00-thumbnail.svg")
