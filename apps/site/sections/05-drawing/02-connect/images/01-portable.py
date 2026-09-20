# 01-portable.svg
# スキーマ: PART-WHOLE（アプリの中身 / つなぐところ）＋ LINK（下だけが同じ）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(900, 340)
c.text(450, 46, "つなぐところは、上に載るアプリを知らない", scale="xl")

c.text(200, 96, "03 章 ライト", scale="sm")
c.text(700, 96, "05 章 お絵かき", scale="sm")

c.node(200, 152, "丸を光らせる", shape="sticky", color="blue", w=300, h=76)
c.node(700, 152, "スタンプを置く", shape="sticky", color="green", w=300, h=76)

left = c.node(200, 252, "つなぐコード", shape="sticky", color="gray", w=300, h=76)
right = c.node(700, 252, "つなぐコード", shape="sticky", color="gray", w=300, h=76)
c.link(left, right, label="まったく同じ", label_scale="sm", both=True, dash="dashed")

c.text(450, 322, "ちがうのは上だけ。だから下はそのまま挿せる", scale="sm")

c.save("01-portable.svg")
