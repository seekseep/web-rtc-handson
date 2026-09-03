# 01-coordinates.svg
# スキーマ: SCALE（見た目の大きさと中の解像度が違う）+ LINK（比率で対応づける）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 400)

c.text(450, 46, "見た目の大きさと、中の解像度は別もの", scale="xl")
c.raw('<rect x="60" y="88" width="360" height="270" rx="10" fill="#ffffff" stroke="#3b82f6" stroke-width="3"/>')
c.text(240, 118, "パソコン（見た目 800px）", scale="sm", fill=PALETTE["blue"]["text"])
c.raw('<circle cx="380" cy="200" r="9" fill="#e5484d"/>')
c.text(340, 240, "右端をクリック", scale="sm")
c.text(240, 300, "event.clientX = 780", scale="sm", font="technical")
c.text(240, 330, "→ 中の座標 780", scale="sm", font="technical")
c.raw('<rect x="520" y="88" width="180" height="270" rx="10" fill="#ffffff" stroke="#17c964" stroke-width="3"/>')
c.text(610, 118, "スマホ（見た目 350px）", scale="sm", fill=PALETTE["green"]["text"])
c.raw('<circle cx="676" cy="200" r="9" fill="#e5484d"/>')
c.text(610, 240, "同じ右端", scale="sm")
c.text(610, 300, "event.clientX = 340", scale="sm", font="technical")
c.text(610, 330, "→ そのままだと真ん中", scale="sm", font="technical")
c.sticky(730, 150, 150, 110, color="yellow")
c.text(805, 190, "見た目の割合", scale="sm", fill=PALETTE["yellow"]["text"])
c.text(805, 216, "× 800", scale="md", font="technical", fill=PALETTE["yellow"]["text"])
c.text(805, 242, "で割り戻す", scale="sm")
c.connector(706, 205, 726, 205, primary=False)

c.save("01-coordinates.svg")
