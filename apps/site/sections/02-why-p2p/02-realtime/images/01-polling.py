# 01-polling.svg
# スキーマ: CYCLE（同じ往復を繰り返す）+ SCALE（時間が進む）+ SPLITTING（3 回ぶんを横に並べる）
# 空振りが 2 回続いてから、3 回目でようやく届く。遅れと無駄が同時に見えるようにする

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 366)
c.text(480, 48, "ポーリング — 何秒かおきに、こちらから聞きに行く", scale="xl")

BROWSER = "1f310"
SERVER = "1f5a5"

steps = [
    (165, "gray", "0 秒", "まだ？", "まだ", "空振り"),
    (480, "gray", "3 秒", "まだ？", "まだ", "空振り"),
    (795, "green", "6 秒", "まだ？", "あった", "やっと届く"),
]

for cx, color, head, ask, reply, foot in steps:
    c.sticky(cx - 145, 76, 290, 200, color=color)
    c.text(cx, 108, head, scale="lg", fill=PALETTE[color]["text"])
    b = c.node(cx - 70, 178, "", emoji_cp=BROWSER, w=76, h=64)
    s = c.node(cx + 70, 178, "", emoji_cp=SERVER, w=76, h=64)
    c.link(b, s, label=ask, label_scale="sm", offset=22)
    c.link(s, b, label=reply, label_scale="sm", offset=22, primary=False)
    c.text(cx, 254, foot, scale="sm")

c.text(480, 314, "相手が書いたのは 3.5 秒。それが見えるのは 6 秒", scale="lg")
c.text(480, 348, "届くまで最大 3 秒遅れる。空振りのぶんは、そのまま無駄な通信になる",
       scale="sm")

c.save("01-polling.svg")
