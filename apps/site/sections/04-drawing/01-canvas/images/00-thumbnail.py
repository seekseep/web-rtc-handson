# 00-thumbnail.svg
# スキーマ: CONTACT（クリックした点にスタンプが乗る）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "キャンバスにスタンプを置く", scale="xl")

c.sticky(300, 92, 300, 150, color="gray")
c.emoji("1f431", 400, 130, 56)
c.text(450, 222, "canvas 800 x 600", scale="sm", font="technical")
c.node(140, 165, "クリック", emoji_cp="1f446", w=120, h=80)
c.connector(212, 160, 292, 160)
c.node(760, 165, "同じ位置に", emoji_cp="1f4cd", w=140, h=80)
c.connector(608, 160, 700, 160, label="座標をそろえる", label_scale="sm")

c.save("00-thumbnail.svg")
