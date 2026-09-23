# 01-steps.svg
# スキーマ: SOURCE-PATH-GOAL（名乗る → つながった までの一方向の道のり）
#          + SPLITTING（サーバーに頼む前半 / 2 人のあいだで決まる後半）
# 6 段階を流れ図にして、どこまでがサーバー越しなのかを色で分ける。
# 色は下のデモにそろえる（サーバー経由 = オレンジ / 直接 = グリーン）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 470)
c.text(480, 48, "つながるまでの 6 段階", scale="xl")

STEPS = [
    ("① 名乗る", "2 人とも、シグナリング\nサーバーにつなぐ", "orange"),
    ("② SDP を交換", "「どう話すか」を、\n先に決める", "orange"),
    ("③ 候補を集める", "「どこに届けるか」の候補を、\nそれぞれが集める", "orange"),
    ("④ 候補を交換", "集めた候補を、\n相手に渡す", "orange"),
    ("⑤ 試す", "候補の組み合わせを試して、\n通る道を探す", "green"),
    ("⑥ つながった", "通った道で、\nデータチャネルが開く", "green"),
]

# 3 列 × 2 行。1 行に 6 つ並べると 1 つあたりが細くなり、説明が入らない。
COLS = [172, 480, 788]
ROWS = [84, 256]
BOX_W, BOX_H = 260, 108

boxes = []
for i, (title, desc, color) in enumerate(STEPS):
    cx = COLS[i % 3]
    y = ROWS[i // 3]
    box = c.sticky(cx - BOX_W / 2, y, BOX_W, BOX_H, color=color)
    c.text(cx, y + 42, title, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, y + 72, desc, scale="sm")
    boxes.append(box)

# 行の中は横に、行をまたぐところだけ下へ回り込む
c.link(boxes[0], boxes[1])
c.link(boxes[1], boxes[2])
c.link(boxes[2], boxes[3], route="elbow", start="s", end="n")
c.link(boxes[3], boxes[4])
c.link(boxes[4], boxes[5])

c.text(330, 408, "■ サーバーに頼む", scale="sm", fill=PALETTE["orange"]["text"])
c.text(636, 408, "■ 2 人のあいだで決まる", scale="sm", fill=PALETTE["green"]["text"])
c.text(480, 446, "①〜④ は、2 人の位置関係によらず同じ。変わるのは ⑤ の結果だけ", scale="sm")

c.save("01-steps.svg")
