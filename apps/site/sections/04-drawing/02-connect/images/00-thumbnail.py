# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（つなぐコードが 03 章から 05 章へ移る）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(900, 290)
c.text(450, 52, "つなぐコードを持ってくる", scale="xl")

light = c.node(130, 165, "03 章 ライト", emoji_cp="1f4a1", w=150, h=90)
code = c.node(450, 160, "つなぐコード", shape="sticky", color="yellow", w=230, h=92)
draw = c.node(770, 165, "05 章 お絵かき", emoji_cp="1f3a8", w=160, h=90)

c.link(light, code, primary=False)
c.link(code, draw, label="1 行も変えずに", label_scale="sm")

c.text(450, 266, "変わるのは、そこに流す中身だけ", scale="sm")

c.save("00-thumbnail.svg")
