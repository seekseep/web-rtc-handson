# 04-instruction-map.svg
# スキーマ: CENTER-PERIPHERY + LINK（決めた 3 種類の指示に、機能がぶら下がる）
# 先に指示の形を決めたから、あとの機能が「足し算」で済むと分かるようにする

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(920, 440)
c.text(460, 46, "3 種類の指示に、あとの機能がぶら下がる", scale="xl")

line = c.node(460, 130, "line", shape="sticky", color="blue", w=150, h=68)
stamp = c.node(460, 245, "stamp", shape="sticky", color="orange", w=150, h=68)
clear = c.node(460, 360, "clear", shape="sticky", color="red", w=150, h=68)

pen = c.node(130, 110, "線を引く", emoji_cp="270f", w=120, h=84)  # ✏️
color = c.node(130, 240, "色を選ぶ", emoji_cp="1f3a8", w=120, h=84)  # 🎨
eraser = c.node(130, 366, "けしごむ", emoji_cp="1f9fd", w=120, h=84)  # 🧽

cat = c.node(790, 160, "スタンプ", emoji_cp="1f431", w=120, h=84)  # 🐱
trash = c.node(790, 330, "ぜんぶ消す", emoji_cp="1f5d1", w=130, h=84)  # 🗑️

c.link(pen, line)
c.link(color, line, label="color を足す")
c.link(eraser, line, label="白くて太い線")

c.link(cat, stamp)
c.link(trash, clear)

c.save("04-instruction-map.svg")
