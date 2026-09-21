# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（ばらばらの材料が、1 枚の要件に集まる）
# 章の入口。まだ作るものは決まっておらず、まず条件を並べる段階だと見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(900, 400)
c.text(450, 46, "まず、要件をまとめる", scale="xl")

past = c.node(160, 150, "これまでの勉強会", emoji_cp="1f4dd", w=220, h=88)  # 📝
limit = c.node(160, 290, "3 時間・2 台", emoji_cp="23f0", w=220, h=88)  # ⏰
req = c.node(660, 220, "要件", shape="sticky", color="yellow", w=230, h=110)

c.link(past, req, label="振り返る")
c.link(limit, req, label="制約")

c.text(450, 378, "作るものを決める前に、満たすべきことを並べる", scale="sm")

c.save("00-thumbnail.svg")
