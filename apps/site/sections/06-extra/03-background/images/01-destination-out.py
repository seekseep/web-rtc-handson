# 01-destination-out.svg
# スキーマ: COUNTERFORCE（白で覆う／透明にする の対比）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

def scene(c, x, y):
    """ミニキャンバス（空と地面）を描く。左上 (x, y)、大きさ 300x116。"""
    c.raw(f'<rect x="{x}" y="{y}" width="300" height="116" rx="8" fill="#bfe6ff"/>')
    c.raw(f'<rect x="{x}" y="{y+66}" width="300" height="50" fill="#b7e3a4"/>')
    c.raw(f'<circle cx="{x+248}" cy="{y+34}" r="20" fill="#ffe08a"/>')
    c.raw(f'<rect x="{x}" y="{y}" width="300" height="116" rx="8" fill="none" '
          f'stroke="#cbd5e1" stroke-width="2"/>')

c = Canvas(900, 384)
c.text(450, 50, "「白く塗る」と「消す」は、別のこと", scale="xl")

c.sticky(50, 84, 380, 240, color="red")
c.text(240, 122, "白で塗る", scale="lg", fill=PALETTE["red"]["text"])
scene(c, 90, 148)
c.raw('<path d="M110 236 Q 170 178 228 218 T 326 190" fill="none" '
      'stroke="#333333" stroke-width="5" stroke-linecap="round"/>')
c.raw('<line x1="110" y1="212" x2="370" y2="212" stroke="#ffffff" '
      'stroke-width="34" stroke-linecap="round"/>')
c.text(240, 300, "背景まで白い帯で隠れる", scale="sm", fill=PALETTE["red"]["text"])

c.sticky(470, 84, 380, 240, color="green")
c.text(660, 122, "透明にする", scale="lg", fill=PALETTE["green"]["text"])
scene(c, 510, 148)
c.raw('<path d="M530 236 Q 590 178 626 200" fill="none" '
      'stroke="#333333" stroke-width="5" stroke-linecap="round"/>')
c.raw('<path d="M700 202 Q 716 196 746 190" fill="none" '
      'stroke="#333333" stroke-width="5" stroke-linecap="round"/>')
c.text(660, 300, "線だけ消えて、背景は残る", scale="sm", fill=PALETTE["green"]["text"])

c.text(450, 356, "背景が白一色でなくなった瞬間に、この違いが表に出る", scale="sm")

c.save("01-destination-out.svg")
