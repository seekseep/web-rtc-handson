# 01-stack.svg
# スキーマ: CONTAINER × 2（通信のしくみと、配信のしくみを別の箱に入れる）
# PeerJS Cloud が描いたデータを中継しているように見えないよう、破線＋ラベルで
# 「つなぐ前の合図だけ」を明示し、Netlify は別の箱に分ける

import sys

sys.path.insert(0, "/Users/seekseep/.claude/skills/genfig")
from genfig import Canvas, PALETTE

c = Canvas(1060, 660)
c.text(530, 46, "通信のしくみと、配信のしくみは別もの", scale="xl")

# --- 上の箱: リアルタイム通信 ---
c.sticky(40, 80, 980, 300, color="gray")
c.text(72, 122, "リアルタイム通信", scale="lg", align="left",
       fill=PALETTE["blue"]["text"])

cloud = c.node(530, 195, "PeerJS Cloud", emoji_cp="2601", w=220, h=96)  # ☁️
pc = c.node(210, 315, "自分の PC", emoji_cp="1f4bb", w=190, h=96)  # 💻
phone = c.node(850, 315, "スマホ", emoji_cp="1f4f1", w=190, h=96)  # 📱

c.link(cloud, pc, primary=False, dash="dashed", label="つなぐ前の合図だけ")
c.link(cloud, phone, primary=False, dash="dashed")
c.link(pc, phone, label="描いたデータは直接", both=True)

# --- 下の箱: アプリの公開 ---
c.sticky(40, 410, 980, 210, color="gray")
c.text(72, 452, "アプリの公開", scale="lg", align="left",
       fill=PALETTE["green"]["text"])

folder = c.node(210, 540, "app フォルダ", emoji_cp="1f4c1", w=190, h=92)  # 📁
drop = c.node(530, 540, "Netlify Drop", emoji_cp="1f680", w=190, h=92)  # 🚀
url = c.node(850, 540, "2 台で開く URL", shape="sticky", color="green", w=210, h=76)

c.link(folder, drop, label="落とす")
c.link(drop, url)

c.text(530, 646, "Netlify はページを配るだけ。描いたデータはそこを通らない", scale="sm")

c.save("03-stack.svg")
