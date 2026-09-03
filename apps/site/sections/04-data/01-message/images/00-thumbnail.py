# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（詰める → 運ぶ → 開き直す）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "オブジェクトは、詰められて運ばれる", scale="xl")

c.node(140, 165, "オブジェクト", emoji_cp="1f4e6", w=130, h=80)
c.sticky(320, 118, 260, 84, color="gray")
c.text(450, 152, "01001010 11001…", scale="sm", font="technical")
c.text(450, 182, "バイトの並び", scale="sm")
c.node(760, 165, "オブジェクト", emoji_cp="1f4e6", w=130, h=80)
c.connector(210, 160, 312, 160, label="詰める", label_scale="sm")
c.connector(588, 160, 690, 160, label="開き直す", label_scale="sm")
c.text(450, 262, "詰められないもの（関数・Date）は形が変わる", scale="sm")

c.save("00-thumbnail.svg")
