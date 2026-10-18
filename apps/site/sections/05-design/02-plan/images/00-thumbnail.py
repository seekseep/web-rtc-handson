# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（要件 → 題材 → 実装の順番）
# 設計の節の入口。要件が先にあり、そこから作るものと順番が決まると見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(1020, 360)
c.text(510, 46, "要件から、作るものを決める", scale="xl")

req = c.node(160, 195, "要件", shape="sticky", color="yellow", w=190, h=104)
app = c.node(510, 195, "お絵かきアプリ", emoji_cp="1f3a8", w=230, h=104)  # 🎨
order = c.node(860, 195, "作る順番", shape="sticky", color="green", w=190, h=104)

c.link(req, app, label="満たせる題材")
c.link(app, order, label="小さく分ける")

c.text(510, 336, "思いつきで決めない。要件を満たせるかで題材を選ぶ", scale="sm")

c.save("00-thumbnail.svg")
