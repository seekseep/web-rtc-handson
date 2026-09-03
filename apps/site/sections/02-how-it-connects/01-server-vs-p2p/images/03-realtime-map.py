# 03-realtime-map.svg
# スキーマ: SPLITTING（「リアルタイムに見えるもの」を3つに分ける）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 340)

c.text(480, 46, "「リアルタイムに見えるもの」の中身は 3 つに分かれる", scale="xl")

cols = [
    (160, "green", "1f91d", "直接つなぐ", "ビデオ通話・画面共有", "ファイルの受け渡し", "WebRTC"),
    (480, "blue", "1f5a5", "サーバーが配る", "同時編集・チャット", "ライブ配信・オンライン対戦", "WebSocket など"),
    (800, "purple", "1f500", "両方まざる", "つなぐまではサーバー", "3 人以上もサーバー経由", "実際のサービスの多く"),
]

for cx, color, cp, head, body1, body2, foot in cols:
    c.sticky(cx - 142, 76, 284, 224, color=color)
    c.emoji(cp, cx - 26, 106, 52)
    c.text(cx, 192, head, scale="lg", fill=PALETTE[color]["text"])
    c.text(cx, 226, body1, scale="sm")
    c.text(cx, 250, body2, scale="sm")
    c.text(cx, 284, foot, scale="sm", fill=PALETTE[color]["text"])

c.save("03-realtime-map.svg")
