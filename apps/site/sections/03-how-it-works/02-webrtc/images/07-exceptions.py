# 07-exceptions.svg
# スキーマ: SPLITTING（サーバーが要る 2 つの場面を並べる）
# 直接つながるのは「つながったあと」の話で、両端にサーバーが残ることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 380)

c.text(480, 50, "それでも、サーバーが 0 台にはならない", scale="xl")

# --- つなぐ前 -----------------------------------------------------------
c.sticky(48, 86, 404, 244, color="gray")
c.text(250, 124, "つなぐ前", scale="lg", fill=PALETTE["gray"]["text"])

sv1 = c.node(250, 186, "シグナリング", emoji_cp="1f5c4", w=64, h=56,
             label_scale="label")
a1 = c.node(128, 280, "", emoji_cp="1f4bb", w=60, h=52)
b1 = c.node(372, 280, "", emoji_cp="1f4bb", w=60, h=52)

c.link(a1, sv1, dash="dashed", primary=False)
c.link(sv1, b1, dash="dashed", primary=False)
c.link(a1, b1, dash="dotted", primary=False, head=False)
c.emoji("274c", 236, 266, 28)

c.text(250, 322, "居場所を教え合う", scale="sm")

c.raw('<line x1="480" y1="96" x2="480" y2="320" '
      'stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6 6"/>')

# --- 直接つながらないとき -----------------------------------------------
c.sticky(508, 86, 404, 244, color="orange")
c.text(710, 124, "直接つながらないとき", scale="lg", fill=PALETTE["orange"]["text"])

sv2 = c.node(710, 186, "中継サーバー", emoji_cp="1f5c4", w=64, h=56,
             label_scale="label")
a2 = c.node(588, 280, "", emoji_cp="1f4bb", w=60, h=52)
b2 = c.node(832, 280, "", emoji_cp="1f4bb", w=60, h=52)

c.link(a2, sv2)
c.link(sv2, b2)

c.text(710, 322, "通るけれど、直接ではない", scale="sm",
       fill=PALETTE["orange"]["text"])

c.text(480, 364, "どちらも、次の節で見る", scale="sm")

c.save("07-exceptions.svg")
