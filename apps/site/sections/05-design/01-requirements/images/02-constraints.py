# 02-constraints.svg
# スキーマ: CONTAINER + BLOCKAGE（1 人で作るという枠が、3 つの制約を生む）
# 技術的な制約ではなく「自分の手持ちから来る制約」であることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1040, 430)
c.text(520, 46, "1 人で作るから生まれる 3 つの制約", scale="xl")

c.sticky(40, 86, 960, 250, color="gray")
c.text(72, 128, "1 人で作る", scale="lg", align="left",
       fill=PALETTE["blue"]["text"])

c.node(210, 240, "画像は作れない", emoji_cp="1f5bc", w=230, h=104)  # 🖼️
c.node(520, 240, "開発に時間をかけられない", emoji_cp="23f3", w=260, h=104)  # ⏳
c.node(830, 240, "1〜3 か月でリリース", emoji_cp="1f4c5", w=230, h=104)  # 📅

c.text(520, 392, "絵を描く人も、まとまった時間もない。期限だけは自分で決める",
       scale="sm")

c.save("02-constraints.svg")
