# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（作りたい気持ちと手持ちの条件が、1 枚の要件に集まる）
# 節の入口。まだルールは決まっておらず、まず満たすべきことを並べる段階だと見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(900, 400)
c.text(450, 46, "まず、要件をまとめる", scale="xl")

want = c.node(160, 150, "iOS アプリを作りたい", emoji_cp="1f4f1", w=230, h=88)  # 📱
alone = c.node(160, 290, "1 人で作る", emoji_cp="1f9d1", w=230, h=88)  # 🧑
req = c.node(660, 220, "要件", shape="sticky", color="yellow", w=230, h=110)

c.link(want, req, label="動機")
c.link(alone, req, label="制約")

c.text(450, 378, "ルールを決める前に、満たすべきことを並べる", scale="sm")

c.save("00-thumbnail.svg")
