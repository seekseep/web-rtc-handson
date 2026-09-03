# 00-thumbnail.svg
# スキーマ: SCALE（通信の「濃さ」が 4 段階で増えていく）+ SPLITTING（4 つを横に並べる）
# 左から右へ、登場するものが増えていくのが一目で分かるようにする

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 306)
c.text(480, 48, "ブラウザの通信は、4 段階ある", scale="xl")

BROWSER = "1f310"
SERVER = "1f5a5"
FILE = "1f4c4"

cols = [
    (135, "gray", "① ローカル", "file://", "通信しない"),
    (365, "blue", "② サーバー", "https://", "もらって終わり"),
    (595, "orange", "③ WebSocket", "wss://", "サーバーが配る"),
    (825, "green", "④ P2P", "（URL なし）", "直接つながる"),
]

for cx, color, head, url, foot in cols:
    c.sticky(cx - 106, 76, 212, 206, color=color)
    c.text(cx, 108, head, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, 218, url, scale="sm", font="technical")
    c.text(cx, 254, foot, scale="sm")

# ① 自分の中で完結（ファイル → ブラウザ）
c.emoji(FILE, 78, 138, 40)
c.emoji(BROWSER, 152, 138, 40)
c.connector(122, 158, 148, 158, primary=False)

# ② ブラウザ ↔ サーバー（1 往復して終わり）
c.emoji(BROWSER, 288, 138, 40)
c.emoji(SERVER, 402, 138, 40)
c.connector(332, 148, 398, 148, primary=False)
c.connector(398, 172, 332, 172, primary=False)

# ③ ブラウザ ↔ サーバー ↔ ブラウザ（つなぎっぱなし）
c.emoji(BROWSER, 506, 143, 30)
c.emoji(SERVER, 580, 143, 30)
c.emoji(BROWSER, 654, 143, 30)
c.biconnector(540, 158, 576, 158, primary=True, weight="thin")
c.biconnector(614, 158, 650, 158, primary=True, weight="thin")

# ④ ブラウザ ↔ ブラウザ（あいだに誰もいない）
c.emoji(BROWSER, 748, 138, 40)
c.emoji(BROWSER, 862, 138, 40)
c.biconnector(792, 158, 858, 158, primary=True, weight="thin")

c.save("00-thumbnail.svg")
