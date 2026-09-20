# 00-thumbnail.svg
# スキーマ: LINK（相手の居場所が見える）+ SOURCE-PATH-GOAL（位置だけを送る）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 300)
c.text(450, 50, "描く前から、相手の居場所が見える", scale="xl")

c.sticky(50, 88, 360, 156, color="blue")
c.text(230, 118, "自分の画面", scale="md", fill=PALETTE["blue"]["text"])
c.raw('<path d="M100 214 Q 160 156 218 196 T 316 168" fill="none" '
      'stroke="#333333" stroke-width="5" stroke-linecap="round"/>')
c.emoji("1f58a", 300, 140, 44)

c.connector(424, 164, 486, 164, label="x, y", label_scale="sm", label_dy=-16)

c.sticky(500, 88, 350, 156, color="yellow")
c.text(675, 118, "相手の画面", scale="md", fill=PALETTE["yellow"]["text"])
c.raw('<path d="M546 214 Q 606 156 664 196 T 762 168" fill="none" '
      'stroke="#333333" stroke-width="5" stroke-linecap="round"/>')
c.raw('<circle cx="766" cy="166" r="11" fill="#ffd60a" stroke="#222" stroke-width="2.5"/>')

c.text(450, 282, "キャンバスには描かない。線が出る前に、いる場所だけが伝わる", scale="sm")

c.save("00-thumbnail.svg")
