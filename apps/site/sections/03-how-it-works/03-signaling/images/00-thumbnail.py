# 00-thumbnail.svg
# スキーマ: SPLITTING（つながるまで / つながったあと を並べる）
#          + SOURCE-PATH-GOAL（つながるまではサーバー経由）+ LINK（つながったあとは直接）
# 渡し合うもの（SDP と ICE candidate）を名指しして、この節で見るものを先に見せる

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 346)
c.text(480, 48, "つながるまでに、何が起きているか", scale="xl")

# --- つながるまで -------------------------------------------------------
c.sticky(48, 80, 520, 222, color="orange")
c.text(308, 112, "つながるまで", scale="lg", fill=PALETTE["orange"]["text"])

sv = c.node(308, 168, "シグナリングサーバー", emoji_cp="1f5c4", w=64, h=56,
            label_scale="sm")
a1 = c.node(128, 246, "A", emoji_cp="1f4bb", w=60, h=52, label_scale="sm")
b1 = c.node(488, 246, "B", emoji_cp="1f4bb", w=60, h=52, label_scale="sm")
c.link(a1, sv, dash="dashed", primary=False, both=True)
c.link(sv, b1, dash="dashed", primary=False, both=True)
c.text(308, 262, "SDP と ICE candidate を渡し合う", scale="sm")

# --- つながったあと -----------------------------------------------------
c.sticky(600, 80, 312, 222, color="green")
c.text(756, 112, "つながったあと", scale="lg", fill=PALETTE["green"]["text"])

a2 = c.node(668, 206, "A", emoji_cp="1f4bb", w=60, h=52, label_scale="sm")
b2 = c.node(844, 206, "B", emoji_cp="1f4bb", w=60, h=52, label_scale="sm")
c.link(a2, b2, both=True)
c.text(756, 272, "サーバーは通らない", scale="sm")

c.text(480, 330, "最初のやりとりだけ、サーバーに頼む", scale="sm")

c.save("00-thumbnail.svg")
