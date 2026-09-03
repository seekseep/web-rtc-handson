# 01-deploy.svg
# スキーマ: SOURCE-PATH-GOAL（公開）+ LINK（2 端末が直接つながる）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 380)

c.text(450, 46, "公開するのはファイル。つながるのは端末同士", scale="xl")
c.node(140, 130, "app/", emoji_cp="1f4c1", w=130, h=90)
c.sticky(320, 90, 250, 88, color="gray", dash="dashed")
c.text(445, 128, "Netlify にドロップ", scale="md")
c.text(445, 154, "app.netlify.com/drop", scale="sm", font="technical")
c.node(760, 130, "https://…", emoji_cp="1f30d", w=150, h=90)
c.connector(212, 130, 312, 130)
c.connector(578, 130, 690, 130)
c.node(250, 290, "パソコン", emoji_cp="1f4bb")
c.node(650, 290, "スマホ", emoji_cp="1f4f1")
c.connector(700, 190, 320, 238, dash="dashed", primary=False, label="同じ URL を開く", label_scale="sm")
c.connector(752, 196, 682, 238, dash="dashed", primary=False)
c.connector(320, 300, 580, 300, label="つながるのはここ（直接）", label_scale="sm")

c.save("01-deploy.svg")
