# 02-before.svg
# スキーマ: FORCE:BLOCKAGE（以前）× 通る（いま）を左右に並べる SPLITTING
# 「使う人に入れてもらう」という壁が消えたことを見せる

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 330)

c.text(480, 50, "以前は、ブラウザだけではできなかった", scale="xl")

# --- 以前 ---------------------------------------------------------------
c.sticky(48, 86, 404, 196, color="gray")
c.text(250, 126, "以前", scale="lg", fill=PALETTE["gray"]["text"])

br1 = c.node(114, 180, "", emoji_cp="1f310", w=64, h=56)
c.text(114, 222, "ブラウザ", scale="sm")
wall = c.node(250, 180, "", emoji_cp="1f6a7", w=64, h=56)
c.text(250, 222, "プラグイン・専用ソフト", scale="sm")
cam1 = c.node(386, 180, "", emoji_cp="1f4f9", w=64, h=56)
c.text(386, 222, "ビデオ通話", scale="sm")

c.link(br1, wall, primary=False)
c.link(wall, cam1, primary=False, dash="dashed")

c.text(250, 258, "入れてもらわないと、始まらない", scale="sm")

c.raw('<line x1="480" y1="96" x2="480" y2="272" '
      'stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6 6"/>')

# --- いま ---------------------------------------------------------------
c.sticky(508, 86, 404, 196, color="green")
c.text(710, 126, "いま", scale="lg", fill=PALETTE["green"]["text"])

br2 = c.node(600, 180, "", emoji_cp="1f310", w=64, h=56)
c.text(600, 222, "ブラウザ", scale="sm")
cam2 = c.node(820, 180, "", emoji_cp="1f4f9", w=64, h=56)
c.text(820, 222, "ビデオ通話", scale="sm")

c.link(br2, cam2, label="WebRTC", label_scale="sm")

c.text(710, 258, "最初から入っているので、開くだけ", scale="sm",
       fill=PALETTE["green"]["text"])

c.text(480, 312, "使う人に何かをインストールしてもらう必要が、丸ごと消えた", scale="sm")

c.save("02-before.svg")
