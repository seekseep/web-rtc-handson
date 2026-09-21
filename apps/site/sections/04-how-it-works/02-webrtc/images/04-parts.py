# 04-parts.svg
# スキーマ: CONTAINER + PART-WHOLE（WebRTC という枠の中に部品が並ぶ）
# 「WebRTC は総称」であること、今回使うのは右の 1 つだけであることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(980, 350)

c.text(490, 48, "WebRTC は、部品のまとまりに付いた名前", scale="xl")

c.sticky(56, 78, 868, 218, color="blue", dash="dashed")
c.text(490, 114, "WebRTC", scale="lg", fill=PALETTE["blue"]["text"])

c.sticky(672, 142, 190, 152, color="green")

parts = [
    (240, "1f4f7", "MediaStream", "カメラとマイクから\n映像と音声を取り出す", None),
    (490, "1f50c", "RTCPeerConnection", "端末と端末をつなぎ\n映像・音声を送受信する", None),
    (767, "1f4dd", "RTCDataChannel", "任意のデータを流す", "green"),
]

for cx, cp, name, desc, color in parts:
    c.node(cx, 182, "", emoji_cp=cp, w=72, h=64)
    c.text(cx, 232, name, scale="md",
           fill=PALETTE[color]["text"] if color else None)
    c.text(cx, 256, desc, scale="sm")

c.text(767, 284, "今回使うのはこれだけ", scale="sm",
       fill=PALETTE["green"]["text"])

c.text(490, 330, "3 つとも使う必要はない。お絵かきが送るのは、線の座標と色だけ", scale="sm")

c.save("04-parts.svg")
