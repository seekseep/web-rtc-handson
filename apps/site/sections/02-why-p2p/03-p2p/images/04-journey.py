# 04-journey.svg
# スキーマ: SOURCE-PATH-GOAL（教材を進むと 4 段階を順に踏む）
# 「4 つは別々の話ではなく、自分がこれから全部通る道」だと分かるようにする

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 310)
c.text(480, 48, "このハンズオンは、4 つ全部を通る", scale="xl")

steps = [
    (130, "gray", "①", "ローカル", "index.html を作って開く", "03 章のあいだ"),
    (360, "blue", "②", "サーバー", "Netlify に公開する", "03 章のおわり"),
    (590, "orange", "③", "WebSocket", "PeerJS Cloud とつながる", "気づかないうちに"),
    (820, "green", "④", "P2P", "相手のブラウザに直接送る", "03 章 〜 05 章"),
]

for cx, color, num, name, what, when in steps:
    c.ellipse(cx, 118, 34, 34, color=color)
    c.text(cx, 127, num, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, 194, name, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, 226, what, scale="sm")
    c.text(cx, 252, when, scale="sm", fill=PALETTE[color]["text"])

for i in range(3):
    x1 = steps[i][0] + 46
    x2 = steps[i + 1][0] - 46
    c.connector(x1, 118, x2, 118, primary=False)

c.text(480, 294, "③ だけは自分では書かない。PeerJS が裏でやっている", scale="sm")

c.save("04-journey.svg")
