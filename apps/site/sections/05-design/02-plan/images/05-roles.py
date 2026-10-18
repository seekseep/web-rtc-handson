# 05-roles.svg
# スキーマ: CYCLE（人が頼み、AI が作り、人が判断する）＋ CONTAINER（それぞれの持ち分）
# コードは AI に任せても、決めることは人の手元に残ることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1000, 440)
c.text(500, 46, "決めるのは人、作るのは AI", scale="xl")

c.sticky(40, 86, 380, 280, color="yellow")
c.text(230, 126, "人が決める", scale="lg", fill=PALETTE["yellow"]["text"])
me = c.node(230, 200, "", emoji_cp="1f9d1", w=110, h=80)  # 🧑
c.text(230, 290, "要件・ルール", scale="md")
c.text(230, 322, "採るか捨てるか", scale="md")

c.sticky(580, 86, 380, 280, color="blue")
c.text(770, 126, "AI が作る", scale="lg", fill=PALETTE["blue"]["text"])
ai = c.node(770, 200, "", emoji_cp="1f916", w=110, h=80)  # 🤖
c.text(770, 290, "コード", scale="md")
c.text(770, 322, "（ロジックも装飾も）", scale="md")

c.link(me, ai, label="頼む", offset=22)
c.link(ai, me, label="できたもの", offset=22, primary=False)

c.text(500, 410, "触って確かめて、また頼む。要件が手元にあるから「これは違う」と言える",
       scale="sm")

c.save("05-roles.svg")
