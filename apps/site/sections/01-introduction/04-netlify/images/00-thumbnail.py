# 00-thumbnail.svg
# スキーマ: SOURCE-PATH-GOAL（フォルダ → ドロップ → 公開 URL）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 290)
c.text(450, 52, "フォルダを落とすだけで URL がもらえる", scale="xl")

c.node(150, 165, "app/", emoji_cp="1f4c1")
c.sticky(330, 108, 240, 116, color="gray", dash="dashed")
c.text(450, 158, "ここに落とす", scale="md")
c.text(450, 186, "app.netlify.com/drop", scale="sm", font="technical")
c.node(760, 165, "公開 URL", emoji_cp="1f30d")
c.connector(232, 165, 322, 165)
c.connector(578, 165, 690, 165, label="数秒", label_scale="sm")

c.save("00-thumbnail.svg")
