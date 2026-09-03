# 00-thumbnail.svg
# スキーマ: LINK（2端末が直接つながる）+ CYCLE（描いた線が双方向に流れる）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "2 つの端末で、いっしょに絵を描く", scale="xl")

c.node(190, 165, "パソコン", emoji_cp="1f4bb")
c.node(710, 165, "スマホ", emoji_cp="1f4f1")
c.node(450, 150, "同じ絵", emoji_cp="1f3a8", shape="sticky", color="yellow", w=170, h=104)
c.connector(288, 140, 358, 140, label="線", label_scale="sm")
c.connector(612, 190, 542, 190, label="スタンプ", label_scale="sm", primary=False)
c.text(450, 268, "あいだにサーバーはいない", scale="sm")

c.save("00-thumbnail.svg")
