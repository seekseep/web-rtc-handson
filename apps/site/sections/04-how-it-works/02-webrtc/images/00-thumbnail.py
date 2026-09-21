# 00-thumbnail.svg
# スキーマ: LINK（2 人が直接つながる）
# この節の答えを 1 行で見せる。「映像・音声・データを、相手のブラウザへ直接」

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(900, 300)

c.text(450, 52, "WebRTC は、何をするための技術か", scale="xl")

c.emoji("1f9d1", 70, 133, 52)
c.text(96, 223, "あなた", scale="label")
a = c.node(210, 172, "ブラウザ A", emoji_cp="1f310")

b = c.node(690, 172, "ブラウザ B", emoji_cp="1f310")
c.emoji("1f9d1", 778, 133, 52)
c.text(804, 223, "相手", scale="label")

c.link(a, b, label="映像・音声・データ", both=True, label_scale="md")

c.text(450, 272, "あいだにサーバーを置かずに、相手のブラウザへ直接", scale="sm")

c.save("00-thumbnail.svg")
