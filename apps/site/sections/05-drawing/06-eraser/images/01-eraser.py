# 01-eraser.svg
# スキーマ: BLOCKAGE（白い太線が下の線を覆う）+ SCALE（太さの違い）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 360)

c.text(450, 46, "同じ line の指示で、色と太さだけを変える", scale="xl")
c.sticky(50, 84, 380, 230, color="blue")
c.text(240, 116, "ペン", scale="lg", fill=PALETTE["blue"]["text"])
c.raw('<line x1="100" y1="170" x2="380" y2="170" stroke="#333333" stroke-width="4" stroke-linecap="round"/>')
c.text(240, 208, "color: 選んだ色 / width: 4", scale="sm", font="technical")
c.raw('<rect x="90" y="234" width="300" height="60" rx="8" fill="#fff" stroke="#cbd5e1" stroke-width="2"/>')
c.raw('<path d="M110 280 Q 190 230 250 268 T 370 250" fill="none" stroke="#333333" stroke-width="5" stroke-linecap="round"/>')
c.sticky(470, 84, 380, 230, color="orange")
c.text(660, 116, "けしごむ", scale="lg", fill=PALETTE["orange"]["text"])
c.raw('<line x1="520" y1="170" x2="800" y2="170" stroke="#ffffff" stroke-width="40" stroke-linecap="round"/>')
c.raw('<line x1="520" y1="170" x2="800" y2="170" stroke="#e2e8f0" stroke-width="40" stroke-linecap="round" opacity="0.9"/>')
c.text(660, 208, "color: '#ffffff' / width: 40", scale="sm", font="technical")
c.raw('<rect x="510" y="234" width="300" height="60" rx="8" fill="#fff" stroke="#cbd5e1" stroke-width="2"/>')
c.raw('<path d="M530 280 Q 610 230 670 268 T 790 250" fill="none" stroke="#333333" stroke-width="5" stroke-linecap="round"/>')
c.raw('<line x1="640" y1="240" x2="640" y2="288" stroke="#ffffff" stroke-width="40" stroke-linecap="round"/>')
c.text(450, 344, "送る指示の種類は増えない。受け取る側は「白い太い線」としか思わない", scale="sm")

c.save("01-eraser.svg")
