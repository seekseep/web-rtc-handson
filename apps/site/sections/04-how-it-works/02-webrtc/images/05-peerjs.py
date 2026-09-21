# 05-peerjs.svg
# スキーマ: VERTICALITY（上に積む）
# 自分が書くのはいちばん上だけ、実際に通信するのはいちばん下であることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(880, 348)

c.text(440, 50, "PeerJS は、WebRTC の上にかぶせる薄い皮", scale="xl")

layers = [
    (92, "green", "あなたのコード", "new Peer(...) / peer.connect(...)", "technical"),
    (166, "blue", "PeerJS", "面倒な手続きを肩代わりする", None),
    (240, "gray", "WebRTC（ブラウザの中）", "実際に通信しているのはここ", None),
]

for y, color, name, note, font in layers:
    c.sticky(60, y, 460, 62, color=color)
    c.text(290, y + 40, name, scale="lg", fill=PALETTE[color]["text"])
    c.text(548, y + 38, note, scale="sm", align="left", font=font)

c.text(440, 334, "書き足したのは上の 1 枚だけ。下の 2 枚は最初からそこにある", scale="sm")

c.save("05-peerjs.svg")
