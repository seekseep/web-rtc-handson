# 00-thumbnail.svg
# スキーマ: SCALE（「他人の変更がどこまで見えるか」が 3 段階で増える）+ SPLITTING（横に並べる）
# 3 段目まで来ても「勝手には届かない」ことが残る、というのがこの節の結論

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 330)
c.text(480, 48, "他人の変更は、どこまで見えるのか", scale="xl")

BROWSER = "1f310"
SERVER = "1f5a5"
FILE = "1f4c4"

cols = [
    (165, "gray", "① ファイルを開く", "file://", "自分の中で終わる"),
    (480, "blue", "② サーバーに置く", "https://", "同じものが見える"),
    (795, "green", "③ DB に入れる", "https:// + DB", "変更も入る"),
]

for cx, color, head, url, foot in cols:
    c.sticky(cx - 145, 76, 290, 214, color=color)
    c.text(cx, 110, head, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, 236, url, scale="sm", font="technical")
    c.text(cx, 270, foot, scale="sm")

# ① ファイル → ブラウザ。自分のパソコンの中で完結する
f1 = c.node(105, 172, "", emoji_cp=FILE, w=76, h=56)
b1 = c.node(225, 172, "", emoji_cp=BROWSER, w=76, h=56)
c.link(f1, b1, primary=False)

# ② サーバー → 2 台のブラウザ。同じものが配られるだけ
s2 = c.node(420, 158, "", emoji_cp=SERVER, w=76, h=56)
b2a = c.node(545, 136, "", emoji_cp=BROWSER, w=64, h=48)
b2b = c.node(545, 190, "", emoji_cp=BROWSER, w=64, h=48)
c.link(s2, b2a, primary=False)
c.link(s2, b2b, primary=False)

# ③ 2 台のブラウザが DB を読み書きする。ただし線はどちらもブラウザ発
db = c.node(855, 172, "DB", shape="cylinder", color="green", w=80, h=64,
            label_scale="sm")
b3a = c.node(730, 140, "", emoji_cp=BROWSER, w=64, h=48)
b3b = c.node(730, 204, "", emoji_cp=BROWSER, w=64, h=48)
c.link(b3a, db, both=True, primary=False)
c.link(b3b, db, both=True, primary=False)

c.text(480, 316, "③ まで来ても、変更は「こちらが聞いたとき」にしか届かない", scale="sm")

c.save("00-thumbnail.svg")
