# 02-draw-and-deliver.svg
# スキーマ: SPLITTING（1 つの願いが、2 つの別々の仕事に割れる）
# 「描く」と「届ける」は別物で、難しさも別、と分かるようにする

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(880, 350)
c.text(440, 44, "ひとつの願いが、2 つの仕事に割れる", scale="xl")

wish = c.node(140, 180, "いっしょに\nお絵かき", shape="sticky", color="yellow", w=180, h=104)

draw = c.node(540, 110, "描く", emoji_cp="1f5bc", w=130, h=90)  # 🖼️
deliver = c.node(540, 248, "届ける", emoji_cp="1f4f1", w=130, h=90)  # 📱

c.link(wish, draw, label="自分の画面に出す")
c.link(wish, deliver, label="相手の画面にも出す")

c.text(720, 118, "キャンバスの話", scale="sm")
c.text(720, 256, "通信の話", scale="sm")

c.text(440, 332, "難しさが別なので、分けて考える", scale="sm")

c.save("02-draw-and-deliver.svg")
