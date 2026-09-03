# 01-signaling-only.svg
# スキーマ: SOURCE-PATH-GOAL（挨拶はサーバー経由）+ LINK（そのあとは直接）

import sys
sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(900, 340)
c.text(450, 50, "サーバーを通るのは、最初のひと声だけ", scale="xl")

c.node(450, 128, "自分の PeerServer", icon_name="server", label_scale="label")

c.node(140, 250, "ブラウザ A", emoji_cp="1f310", label_scale="label")
c.node(760, 250, "ブラウザ B", emoji_cp="1f310", label_scale="label")

c.connector(196, 212, 372, 148, dash="dashed", primary=False,
            label="あいことば", label_scale="sm")
c.connector(528, 148, 704, 212, dash="dashed", primary=False)

c.connector(206, 288, 694, 288, label="線・スタンプはここを流れる", label_scale="sm")

c.text(450, 328, "100 人が描いていても、サーバーが運ぶのは挨拶だけ", scale="sm")

c.save("01-signaling-only.svg")
