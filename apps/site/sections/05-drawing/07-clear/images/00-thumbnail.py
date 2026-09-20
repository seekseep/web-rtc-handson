# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL + SPLITTING（1 回のクリックが両方の画面を白紙にする）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 320)
c.text(450, 46, "1 回のクリックで、両方の画面が白紙になる", scale="xl")

c.sticky(70, 92, 180, 56, color="gray")
c.text(160, 124, "ぜんぶ消す", scale="md", fill=PALETTE["gray"]["text"])

c.connector(258, 120, 368, 120)

c.sticky(380, 92, 230, 56, color="yellow")
c.text(495, 124, "{ type: 'clear' }", scale="md", font="technical", fill=PALETTE["yellow"]["text"])

c.connector(450, 158, 300, 194)
c.connector(560, 158, 690, 194)

c.raw('<rect x="170" y="200" width="230" height="76" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>')
c.text(285, 296, "じぶんの画面", scale="sm")
c.raw('<rect x="580" y="200" width="230" height="76" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>')
c.text(695, 296, "あいての画面", scale="sm")

c.save("00-thumbnail.svg")
