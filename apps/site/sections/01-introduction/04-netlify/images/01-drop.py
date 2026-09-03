# 01-drop.svg
# スキーマ: SOURCE-PATH-GOAL（フォルダ → ドロップゾーン → 公開 URL）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 330)

c.text(450, 46, "app フォルダを、まるごと落とす", scale="xl")
c.node(140, 180, "app/", emoji_cp="1f4c1", w=140, h=100)
c.sticky(320, 116, 250, 130, color="gray", dash="dashed")
c.text(445, 170, "ドロップゾーン", scale="lg")
c.text(445, 200, "app.netlify.com/drop", scale="sm", font="technical")
c.node(760, 180, "https://…", emoji_cp="1f30d", w=160, h=100)
c.connector(226, 176, 312, 176)
c.connector(578, 176, 690, 176, label="数秒で発行", label_scale="sm")
c.text(450, 296, "中の index.html を選ぶのではなく、フォルダそのものを落とす", scale="sm")

c.save("01-drop.svg")
