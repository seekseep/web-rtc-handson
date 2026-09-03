# 01-two-paths.svg
# スキーマ: SPLITTING（残るもの／残らないもので扱いを分ける）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 360)
c.text(450, 50, "残るものと、残らないもの", scale="xl")

c.sticky(50, 84, 380, 232, color="blue")
c.text(240, 124, "線・スタンプ・ぜんぶ消す", scale="lg", fill=PALETTE["blue"]["text"])
c.bullets(86, 172, [
    "draw() を通す",
    "キャンバスに描く",
    "history に貯める",
    "つながっていれば送る",
], scale="body", gap=32)

c.sticky(470, 84, 380, 232, color="yellow")
c.text(660, 124, "カーソル", scale="lg", fill=PALETTE["yellow"]["text"])
c.bullets(506, 172, [
    "draw() を通さない",
    "キャンバスに描かない",
    "history に貯めない",
    "conn.send で直接送る",
], scale="body", gap=32)

c.text(450, 344, "残らないものを history に入れると、あとから来た人に古い位置が流れる", scale="sm")

c.save("01-two-paths.svg")
