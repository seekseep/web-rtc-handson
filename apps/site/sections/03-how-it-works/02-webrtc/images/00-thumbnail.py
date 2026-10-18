# 00-thumbnail.svg
# スキーマ: LINK（2 台が直接つながる）
# この節の答えを 1 行で見せる。「映像・音声・データを、相手へ直接」

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(900, 300)

c.text(450, 52, "WebRTC は、何をするための技術か", scale="xl")

me = c.node(230, 172, "自分", emoji_cp="1f4bb")
you = c.node(670, 172, "相手", emoji_cp="1f4bb")

c.link(me, you, label="映像・音声・データ", both=True, label_scale="md")

c.text(450, 272, "あいだにサーバーを置かずに、相手のパソコンへ直接", scale="sm")

c.save("00-thumbnail.svg")
