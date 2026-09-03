# 00-thumbnail.svg
# スキーマ: SCALE（通る通信量の差）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 348)
c.text(450, 50, "TURN だけ、通信がまるごと通る", scale="xl")

rows = [
    ("PeerServer", "最初のひと声だけ", 3, "teal", 96),
    ("STUN", "住所を教えるだけ", 3, "blue", 168),
    ("TURN", "描いた線が全部", 26, "orange", 240),
]
for name, note, width, color, y in rows:
    c.sticky(50, y, 800, 60, color=color, rx=12)
    c.text(84, y + 38, name, scale="lg", align="left",
           fill=PALETTE[color]["text"], font="technical")
    c.raw(f'<line x1="330" y1="{y+30}" x2="620" y2="{y+30}" stroke="{PALETTE[color]["border"]}" '
          f'stroke-width="{width}" stroke-linecap="round"/>')
    c.text(836, y + 38, note, scale="sm", align="right")

c.text(450, 334, "中継した通信量が、そのまま費用になる", scale="sm")

c.save("00-thumbnail.svg")
