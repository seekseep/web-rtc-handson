# 01-candidates.svg
# スキーマ: SPLITTING（1 つの相談が、3 つの候補に分かれる）
# 候補を並べたうえで 1 つだけ選ばれた、という分岐の形を見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(940, 470)
c.text(470, 46, "候補を並べて、1 つ選ぶ", scale="xl")

theme = c.sticky(40, 160, 220, 120, color="yellow")
c.text(150, 210, "勉強会の\n題材", scale="lg")
c.text(150, 330, "何を試すかを\n話し合った", scale="sm")

camera = c.node(620, 130, "カメラ", emoji_cp="1f4f7", w=170, h=84)  # 📷
image = c.node(620, 250, "画像処理", emoji_cp="1f5bc", w=170, h=84)  # 🖼️
p2p = c.node(620, 370, "P2P 通信", emoji_cp="1f4e1", w=170, h=84)  # 📡

c.link(theme, camera, primary=False, dash="dashed")
c.link(theme, image, primary=False, dash="dashed")
c.link(theme, p2p, label="これにした")

c.text(470, 452, "ここで決まったのは「リアルタイム通信で何か作る」まで", scale="sm")

c.save("01-candidates.svg")
