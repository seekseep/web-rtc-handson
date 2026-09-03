# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（ゲストがホストを呼び出す）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "名乗る人と、呼び出す人", scale="xl")

c.node(190, 170, "ホスト", emoji_cp="1f3e0")
c.text(190, 242, "あいことばを名乗る", scale="sm")
c.node(710, 170, "ゲスト", emoji_cp="1f6b6")
c.text(710, 242, "名乗らず呼び出す", scale="sm")
c.sticky(360, 118, 180, 60, color="yellow")
c.text(450, 155, "あいことば", scale="md", fill=PALETTE["yellow"]["text"])
c.connector(258, 148, 352, 148, label="名乗る", label_scale="sm", primary=False)
c.connector(646, 148, 552, 148, label="呼び出す", label_scale="sm", primary=False)
c.text(450, 206, "つながったら、どちらも対等", scale="sm")

c.save("00-thumbnail.svg")
