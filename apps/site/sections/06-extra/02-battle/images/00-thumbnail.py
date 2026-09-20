# 00-thumbnail.svg
# スキーマ: COUNTERFORCE（2 人が同じ盤面を押し合う）+ BALANCE（取った割合が釣り合う）

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 300)
c.text(450, 50, "同じ盤面を、ふたりで塗り合う", scale="xl")

blue = c.node(150, 160, "あなた", emoji_cp="1f58a", color="blue")
orange = c.node(750, 160, "あいて", emoji_cp="1f58a", color="orange")

# 盤面はラベル付きノードだと文字が中央で重なるので、枠だけ置いて中身は自分で並べる
board = c.sticky(350, 97, 200, 116, color="gray")
c.text(450, 126, "40 x 30 マス", scale="sm")
c.text(450, 163, "58%", scale="lg", fill=PALETTE["blue"]["text"])
c.text(450, 197, "42%", scale="lg", fill=PALETTE["orange"]["text"])

c.link(blue, board, label="ぬる", label_scale="sm")
c.link(orange, board, label="ぬる", label_scale="sm", primary=False)

c.text(450, 278, "インクは、手を離しているあいだだけ回復する", scale="sm")

c.save("00-thumbnail.svg")
