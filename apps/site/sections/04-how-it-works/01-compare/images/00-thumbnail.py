# 00-thumbnail.svg
# スキーマ: SCALE（「他人の変更がどこまで届くか」が 4 段階で上がる）+ SPLITTING（横に並べる）
# どの段でも両端にいるのは自分と相手の 2 台。あいだに何が居るかだけが違う

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 346)
c.text(480, 48, "他人の変更は、どうやって届くのか", scale="xl")

DEVICE = "1f4bb"
SERVER = "1f5c4"

cols = [
    (123, "gray", "① 静的サイト", "同じものが配られるだけ"),
    (361, "blue", "② 動的サイト", "聞けば、変更も届く"),
    (599, "orange", "③ WebSocket", "聞かなくても届く"),
    (837, "green", "④ WebRTC", "誰も経由せずに届く"),
]

for cx, color, head, foot in cols:
    c.sticky(cx - 111, 76, 222, 222, color=color)
    c.text(cx, 108, head, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, 284, foot, scale="sm")

def devices(cx):
    a = c.node(cx - 64, 230, "", emoji_cp=DEVICE, w=52, h=44)
    b = c.node(cx + 64, 230, "", emoji_cp=DEVICE, w=52, h=44)
    return a, b

# ① サーバーが同じファイルを配るだけ。A と B のあいだに線は無い
a, b = devices(123)
s = c.node(123, 160, "", emoji_cp=SERVER, w=52, h=44)
c.link(s, a, primary=False)
c.link(s, b, primary=False)

# ② DB にためる。ただし線はどちらも自分と相手の側から
a, b = devices(361)
db = c.node(361, 160, "DB", shape="cylinder", color="blue", w=66, h=50,
            label_scale="sm")
c.link(a, db, both=True, primary=False)
c.link(b, db, both=True, primary=False)

# ③ サーバーがつなぎっぱなしで、向こうから流し込んでくる
a, b = devices(599)
s = c.node(599, 160, "", emoji_cp=SERVER, w=52, h=44)
c.link(a, s)
c.link(s, b)

# ④ あいだに誰も居ない
a, b = devices(837)
c.text(837, 166, "あいだに\n誰も居ない", scale="sm")
c.link(a, b, both=True)

c.text(480, 330, "右へ行くほど速く、近くなる。その代わり、残らなくなる", scale="sm")

c.save("00-thumbnail.svg")
