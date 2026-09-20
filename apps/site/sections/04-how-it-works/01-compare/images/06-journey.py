# 06-journey.svg
# スキーマ: SOURCE-PATH-GOAL（教材を進むと 4 段階を順に踏む）
# 「別々の話ではなく、自分がすでに通ってきた道」だと分かるようにする。② だけ欠けている

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 310)
c.text(480, 48, "この教材で、すでに通ってきた道", scale="xl")

steps = [
    (130, "gray", "⓪", "ローカル", "index.html を作って開く", "03 章のあいだ"),
    (360, "blue", "①", "静的サイト", "Netlify に公開する", "03 章のおわり"),
    (590, "orange", "③", "WebSocket", "PeerJS Cloud とつながる", "気づかないうちに"),
    (820, "green", "④", "WebRTC", "相手のブラウザに直接送る", "03 章 〜 05 章"),
]

dots = []
for cx, color, num, name, what, when in steps:
    dots.append(c.ellipse(cx, 118, 34, 34, color=color))
    c.text(cx, 127, num, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, 194, name, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, 226, what, scale="sm")
    c.text(cx, 252, when, scale="sm", fill=PALETTE[color]["text"])

for a, b in zip(dots, dots[1:]):
    c.link(a, b, primary=False)

c.text(480, 294, "② 動的サイトだけ通っていない。どこにも保存しないから", scale="sm")

c.save("06-journey.svg")
