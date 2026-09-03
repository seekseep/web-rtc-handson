# 00-thumbnail.svg
# スキーマ: PART-WHOLE（WebRTC の内訳）+ SPLITTING（使う / 使わない）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "WebRTC の 3 つの道具のうち、2 つを使う", scale="xl")

c.sticky(60, 92, 240, 150, color="gray")
c.emoji("1f4f7", 156, 116, 48)
c.text(180, 190, "getUserMedia", scale="sm", font="technical")
c.text(180, 218, "使わない", scale="sm")
c.sticky(330, 92, 240, 150, color="blue")
c.emoji("1f50c", 426, 116, 48)
c.text(450, 190, "RTCPeerConnection", scale="sm", font="technical")
c.text(450, 218, "通り道を作る", scale="sm", fill=PALETTE["blue"]["text"])
c.sticky(600, 92, 240, 150, color="green")
c.emoji("1f4e6", 696, 116, 48)
c.text(720, 190, "RTCDataChannel", scale="sm", font="technical")
c.text(720, 218, "データを流す", scale="sm", fill=PALETTE["green"]["text"])
c.text(450, 272, "PeerJS がこの 2 つを包んでくれる", scale="sm")

c.save("00-thumbnail.svg")
