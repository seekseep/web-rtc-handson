# 00-thumbnail.svg
# スキーマ: VERTICALITY（層の上下）+ BLOCKAGE/穴（上の層に穴をあけると下が見える）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 310)
c.text(450, 50, "canvas は透明。背景は下の層に敷く", scale="xl")

c.node(490, 126, "描いた線（canvas）", shape="parallelogram", color="blue", w=360, h=78)
c.node(490, 224, "背景画像（CSS）", shape="parallelogram", color="green", w=360, h=78)

c.emoji("1f9fd", 128, 92, 58)
c.text(157, 182, "けしごむ", scale="md")
c.connector(212, 126, 292, 126, label="穴をあける", label_scale="sm", label_dy=-16)

c.text(772, 180, "穴から", scale="sm")
c.text(772, 204, "下が見える", scale="sm")

c.text(450, 292, "白で塗るのではなく、destination-out で透明にする", scale="sm")

c.save("00-thumbnail.svg")
