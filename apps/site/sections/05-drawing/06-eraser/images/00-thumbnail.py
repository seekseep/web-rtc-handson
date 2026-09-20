# 00-thumbnail.svg
# スキーマ: BLOCKAGE（白い帯が下の線を覆い隠す）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "けしごむは、白くて太いペン", scale="xl")

c.raw('<rect x="150" y="100" width="600" height="140" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>')
c.raw('<path d="M180 210 Q 300 110 420 200 T 720 150" fill="none" stroke="#3b82f6" stroke-width="7" stroke-linecap="round"/>')
c.raw('<line x1="360" y1="120" x2="360" y2="225" stroke="#ffffff" stroke-width="46" stroke-linecap="round"/>')
c.emoji("1f9fd", 332, 60, 56)
c.text(450, 272, "消しているのではなく、背景と同じ白で上塗りしている", scale="sm")

c.save("00-thumbnail.svg")
