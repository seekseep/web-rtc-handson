# 02-spike.svg
# スキーマ: FORCE:BLOCKAGE + SOURCE-PATH-GOAL（塞がれた道と、かぶせもので通る道）
# 難しそうな技術は、薄い皮をかぶせたライブラリを探せば越えられることがある

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas

c = Canvas(960, 420)
c.text(480, 46, "難しそうなら、かぶせるものを探す", scale="xl")

want = c.node(120, 200, "やりたいこと", emoji_cp="1f4e1", w=170, h=92)  # 📡
c.text(120, 282, "リアルタイム通信", scale="sm")

wall = c.node(540, 118, "むずかしそう", emoji_cp="1f6a7", w=170, h=88)  # 🚧
c.link(want, wall, label="WebRTC を直接書く", primary=False, dash="dashed")

lib = c.node(520, 296, "PeerJS", emoji_cp="1f4e6", w=150, h=88)  # 📦
ok = c.node(840, 296, "つながった", emoji_cp="2705", w=150, h=88)  # ✅
c.link(want, lib, label="かぶせて使う")
c.link(lib, ok, label="30 行ほど")

c.text(480, 398, "そのまま書けば大変なものでも、薄い皮をかぶせたライブラリがあることは多い", scale="sm")

c.save("02-spike.svg")
