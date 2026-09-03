# 01-serialize.svg
# スキーマ: SOURCE-PATH-GOAL（詰める → 運ぶ → 開き直す）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 340)

c.text(450, 46, "通り道を流れるのは、バイトの並びだけ", scale="xl")
c.sticky(50, 96, 220, 110, color="green")
c.text(160, 138, "{ color: '#f00' }", scale="sm", font="technical", fill=PALETTE["green"]["text"])
c.text(160, 172, "オブジェクト", scale="sm")
c.sticky(340, 96, 220, 110, color="gray")
c.text(450, 134, "10010110", scale="sm", font="technical")
c.text(450, 158, "11001010…", scale="sm", font="technical")
c.text(450, 188, "バイトの並び", scale="sm")
c.sticky(630, 96, 220, 110, color="green")
c.text(740, 138, "{ color: '#f00' }", scale="sm", font="technical", fill=PALETTE["green"]["text"])
c.text(740, 172, "オブジェクト", scale="sm")
c.connector(278, 150, 332, 150, label="詰める", label_scale="sm")
c.connector(568, 150, 622, 150, label="開き直す", label_scale="sm")
c.text(450, 262, "詰められるのは「データとして表せるもの」だけ", scale="md")
c.text(450, 296, "関数は送れない。Date は文字列に、undefined は null になる", scale="sm")

c.save("01-serialize.svg")
