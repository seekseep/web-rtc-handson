# 01-relay.svg
# スキーマ: BLOCKAGE（直接は届かない）+ SOURCE-PATH-GOAL（迂回して中継）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 340)
c.text(450, 50, "直接届かないときは、TURN が運ぶ", scale="xl")

c.node(140, 240, "ブラウザ A", emoji_cp="1f310", label_scale="label")
c.node(760, 240, "ブラウザ B", emoji_cp="1f310", label_scale="label")

c.node(450, 126, "TURN", emoji_cp="1f4e6", label_scale="label")
c.connector(202, 206, 380, 154, label="全部", label_scale="sm")
c.connector(520, 154, 698, 206)

c.raw('<line x1="212" y1="256" x2="688" y2="256" stroke="#cbd5e1" stroke-width="3" '
      'stroke-linecap="round" stroke-dasharray="7 6"/>')
c.emoji("1f6a7", 424, 232, 52)
c.text(450, 320, "TURN を通ったときは、もう直接つながっていない", scale="sm")

c.save("01-relay.svg")
