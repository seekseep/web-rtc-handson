# 06-p2p.svg
# スキーマ: SPLITTING（2 つの経路を左右に並べる）+ SOURCE-PATH-GOAL
# 同じ「自分 → 相手」でも、真ん中にサーバーが居るか居ないかだけが違うことを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 320)

c.text(480, 50, "サーバーを通すか、直接つなぐか", scale="xl")

# --- サーバー経由 -------------------------------------------------------
c.sticky(48, 86, 404, 192, color="gray")
c.text(250, 126, "サーバー経由", scale="lg", fill=PALETTE["gray"]["text"])

a1 = c.node(130, 192, "", emoji_cp="1f4bb", w=60, h=52)
c.text(130, 234, "自分", scale="sm")
sv = c.node(250, 192, "", emoji_cp="1f5c4", w=64, h=56)
c.text(250, 234, "サーバー", scale="sm")
b1 = c.node(370, 192, "", emoji_cp="1f4bb", w=60, h=52)
c.text(370, 234, "相手", scale="sm")

c.link(a1, sv)
c.link(sv, b1)

c.text(250, 262, "相手に届くまでに、真ん中を通る", scale="sm")

c.raw('<line x1="480" y1="96" x2="480" y2="268" '
      'stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6 6"/>')

# --- P2P ----------------------------------------------------------------
c.sticky(508, 86, 404, 192, color="green")
c.text(710, 126, "P2P", scale="lg", fill=PALETTE["green"]["text"])

p1 = c.node(616, 192, "", emoji_cp="1f4bb", w=64, h=56)
c.text(616, 234, "自分", scale="sm")
p2 = c.node(804, 192, "", emoji_cp="1f4bb", w=64, h=56)
c.text(804, 234, "相手", scale="sm")

c.link(p1, p2, both=True)

c.text(710, 262, "サーバーを介さず、直接つながる", scale="sm",
       fill=PALETTE["green"]["text"])

c.text(480, 306, "WebRTC は、右を Web の上でやるための技術", scale="sm")

c.save("06-p2p.svg")
