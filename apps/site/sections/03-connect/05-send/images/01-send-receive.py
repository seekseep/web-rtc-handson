# 01-send-receive.svg
# スキーマ: SOURCE-PATH-GOAL（色が流れる）+ SPLITTING（同じ出来事を 2 つの立場で見る）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 360)

c.text(450, 46, "同じ出来事を、2 つの画面がそれぞれの立場で描く", scale="xl")
c.sticky(50, 84, 350, 220, color="blue")
c.text(225, 116, "押した人の画面", scale="lg", fill=PALETTE["blue"]["text"])
c.ellipse(140, 190, 38, 38, color="orange")
c.text(140, 250, "じぶん", scale="sm")
c.ellipse(300, 190, 38, 38, color="gray")
c.text(300, 250, "あいて", scale="sm")
c.text(225, 288, "じぶんの丸が光る", scale="sm")
c.sticky(500, 84, 350, 220, color="green")
c.text(675, 116, "受け取った人の画面", scale="lg", fill=PALETTE["green"]["text"])
c.ellipse(590, 190, 38, 38, color="gray")
c.text(590, 250, "じぶん", scale="sm")
c.ellipse(750, 190, 38, 38, color="orange")
c.text(750, 250, "あいて", scale="sm")
c.text(675, 288, "あいての丸が光る", scale="sm")
c.connector(408, 190, 492, 190, label="{ color }", label_scale="sm")
c.text(450, 340, "送っているのは色だけ。どちらの丸に塗るかは受け取った側が決める", scale="sm")

c.save("01-send-receive.svg")
