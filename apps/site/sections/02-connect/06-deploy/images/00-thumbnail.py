# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（公開）+ LINK（2端末が直接つながる）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "公開して、本当に 2 台でつなぐ", scale="xl")

c.node(450, 108, "Netlify の URL", emoji_cp="1f30d", w=140, h=80)
c.node(190, 200, "パソコン", emoji_cp="1f4bb")
c.node(710, 200, "スマホ", emoji_cp="1f4f1")
c.connector(396, 130, 250, 172, primary=False, dash="dashed")
c.connector(504, 130, 650, 172, primary=False, dash="dashed")
c.connector(288, 196, 612, 196, label="ここは直接つながる", label_scale="sm")

c.save("00-thumbnail.svg")
