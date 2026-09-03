# 01-local.svg
# スキーマ: CONTAINER（自分の PC の中で完結）+ BLOCKAGE（外へ出て行かない）
# 「相手がいない」ことを、箱の外に置いた相手と ✕ で見せる

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(960, 352)
c.text(480, 46, "① ローカルのファイルを開く", scale="xl")

c.sticky(44, 84, 428, 222, color="gray")
c.text(258, 116, "あなたのパソコンの中", scale="lg", fill=PALETTE["gray"]["text"])
c.node(155, 198, "index.html", emoji_cp="1f4c4")
c.node(362, 198, "ブラウザ", emoji_cp="1f310")
c.connector(202, 190, 314, 190, label="ひらく", label_scale="sm")
c.text(258, 288, "ネットワークは 1 バイトも動かない", scale="sm")

c.connector(492, 198, 662, 198, dash="dashed", primary=False)
c.emoji("274c", 560, 180, 36)

c.node(812, 198, "相手のブラウザ", emoji_cp="1f310")
c.text(812, 288, "同じファイルが無いので、開けない", scale="sm")

c.save("01-local.svg")
