# 06-unknown-first.svg
# スキーマ: BALANCE + FORCE:COMPULSION（2 つの仕事を並べ、不安なほうへ先に向かう）
# 「分からないほうを先に、小さく試す」というエンジニアの判断を見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(920, 340)
c.text(460, 46, "分からないほうを、先に確かめる", scale="xl")

draw = c.node(220, 150, "描く", emoji_cp="1f5bc", w=140, h=92)  # 🖼️
c.text(220, 236, "手元だけで終わる", scale="sm")
c.text(220, 262, "うまくいかなければ", scale="sm")
c.text(220, 286, "原因は自分のコード", scale="sm")

deliver = c.node(700, 150, "届ける", emoji_cp="1f4e1", w=140, h=92)  # 📡
c.text(700, 236, "相手と回線しだい", scale="sm")
c.text(700, 262, "会場のネットワークで", scale="sm")
c.text(700, 286, "通らないこともある", scale="sm")

c.link(draw, deliver, label="こちらを先に、小さく")

c.save("06-unknown-first.svg")
