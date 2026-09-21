# 01-constraints.svg
# スキーマ: CONTAINER + BLOCKAGE（勉強会という枠が、3 つの制約を生む）
# 技術的な制約ではなく「集まってやるから生まれる制約」であることを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1040, 430)
c.text(520, 46, "勉強会だから生まれる 3 つの制約", scale="xl")

c.sticky(40, 86, 960, 250, color="gray")
c.text(72, 128, "勉強会という場", scale="lg", align="left",
       fill=PALETTE["blue"]["text"])

time = c.node(210, 240, "3 時間で完結", emoji_cp="23f0", w=230, h=104)  # ⏰
device = c.node(520, 240, "PC ＋ スマホ", emoji_cp="1f4f1", w=230, h=104)  # 📱
early = c.node(830, 240, "早く「動いた」", emoji_cp="1f389", w=230, h=104)  # 🎉

c.text(520, 392, "参加しやすさ・持ち物・集中力。どれも人が集まる日ならではの条件",
       scale="sm")

c.save("01-constraints.svg")
