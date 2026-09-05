# 01-three-parts.svg
# スキーマ: PART-WHOLE（WebRTC の内訳）+ SPLITTING（使う / 使わない）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 330)

c.text(450, 46, "WebRTC の中身と、今回使うところ", scale="xl")
c.sticky(50, 84, 250, 190, color="gray")
c.emoji("1f4f7", 150, 112, 50)
c.text(175, 196, "getUserMedia", scale="md", font="technical")
c.text(175, 224, "カメラ・マイク", scale="sm")
c.text(175, 256, "今回は使わない", scale="sm", fill=PALETTE["gray"]["text"])
c.sticky(325, 84, 250, 190, color="blue")
c.emoji("1f50c", 425, 112, 50)
c.text(450, 196, "RTCPeerConnection", scale="sm", font="technical")
c.text(450, 224, "通り道を作る", scale="md", fill=PALETTE["blue"]["text"])
c.text(450, 256, "PeerJS が包む", scale="sm")
c.sticky(600, 84, 250, 190, color="green")
c.emoji("1f4e6", 700, 112, 50)
c.text(725, 196, "RTCDataChannel", scale="sm", font="technical")
c.text(725, 224, "データを流す", scale="md", fill=PALETTE["green"]["text"])
c.text(725, 256, "conn.send() がこれ", scale="sm")
c.text(450, 310, "ビデオ通話の技術だが、映像を使わずデータだけ流すこともできる", scale="sm")

c.save("01-three-parts.svg")
