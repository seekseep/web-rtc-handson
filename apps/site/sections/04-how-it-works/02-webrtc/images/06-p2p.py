# 06-p2p.svg
# スキーマ: SPLITTING（2 つの関係を左右に並べる）+ BALANCE（右は対等）
# 「頼む人と答える人」から「対等な 2 人」へ、役割の非対称が消えることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 320)

c.text(480, 50, "頼む人と答える人か、対等な 2 人か", scale="xl")

# --- いつもの Web -------------------------------------------------------
c.sticky(48, 86, 404, 192, color="gray")
c.text(250, 126, "いつもの Web", scale="lg", fill=PALETTE["gray"]["text"])

br = c.node(158, 192, "", emoji_cp="1f310", w=64, h=56)
c.text(158, 234, "ブラウザ", scale="sm")
sv = c.node(346, 192, "", emoji_cp="1f5a5", w=64, h=56)
c.text(346, 234, "サーバー", scale="sm")

c.link(br, sv, label="お願い", label_scale="sm", offset=20)
c.link(sv, br, label="返事", label_scale="sm", offset=20, primary=False)

c.text(250, 262, "始めるのは、いつもブラウザの側", scale="sm")

c.raw('<line x1="480" y1="96" x2="480" y2="268" '
      'stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6 6"/>')

# --- P2P ----------------------------------------------------------------
c.sticky(508, 86, 404, 192, color="green")
c.text(710, 126, "P2P", scale="lg", fill=PALETTE["green"]["text"])

p1 = c.node(616, 192, "", emoji_cp="1f310", w=64, h=56)
c.text(616, 234, "ピア", scale="sm")
p2 = c.node(804, 192, "", emoji_cp="1f310", w=64, h=56)
c.text(804, 234, "ピア", scale="sm")

c.link(p1, p2, both=True)

c.text(710, 262, "どちらも同じ立場", scale="sm", fill=PALETTE["green"]["text"])

c.text(480, 306, "WebRTC は、右をブラウザの上でやるための技術", scale="sm")

c.save("06-p2p.svg")
