# 00-thumbnail.svg
# スキーマ: SCALE（太さの段階）+ SOURCE-PATH-GOAL（指示に載って相手へ）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 300)
c.text(450, 50, "太さは、もう指示の中に入っていた", scale="xl")

c.sticky(50, 88, 360, 156, color="blue")
c.text(230, 118, "自分の画面", scale="md", fill=PALETTE["blue"]["text"])
for y, w in ((152, 4), (184, 12), (222, 28)):
    c.raw(f'<line x1="96" y1="{y}" x2="364" y2="{y}" stroke="#333333" '
          f'stroke-width="{w}" stroke-linecap="round"/>')

c.connector(424, 164, 486, 164, label="width", label_scale="sm", label_dy=-16)

c.sticky(500, 88, 350, 156, color="green")
c.text(675, 118, "相手の画面", scale="md", fill=PALETTE["green"]["text"])
for y, w in ((152, 4), (184, 12), (222, 28)):
    c.raw(f'<line x1="546" y1="{y}" x2="804" y2="{y}" stroke="#333333" '
          f'stroke-width="{w}" stroke-linecap="round"/>')

c.text(450, 282, "受け取る側のコードは 1 行も直らない", scale="sm")

c.save("00-thumbnail.svg")
