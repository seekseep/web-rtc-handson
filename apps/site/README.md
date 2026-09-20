---
docs: true
title: リアルタイムお絵かきハンズオン
---

# リアルタイムお絵かきハンズオン

PeerJS を使って**ブラウザ同士を直接つなぎ**、2 つの端末でいっしょに絵を描けるツールを作る教材です。
手を動かしてコードを組み立てながら進めます。

手を動かす前に、**どうしてこの題材になったのか・どうやって実現するのか・何をどの順で作るのか**を決めます。
そのうえで、まず「ボタンを押したら、相手の画面の丸が光る」だけの小さなアプリでつなぎ方を覚え、
それを Netlify に公開して自分の PC とスマホの 2 台で動かします。
つながったところで、その裏で何が起きているのかを一度ていねいに見ます。
最後に同じ仕組みのまま、スタンプ・線・色・消しゴムを足してお絵かきツールに育てます。

サーバーは書きません。ブラウザだけで動きます。PeerJS 本体は CDN（cdnjs）から読み込むので、
インストールも npm も使いません。

## 必要なもの

- パソコン（Windows / Mac どちらでも）とブラウザ（Chrome 推奨）
- **もう 1 台の端末**（スマホでも、2 台目の PC でも、友達の PC でも可）
- インターネットに接続できる環境

公開はフォルダをブラウザに落とすだけです（Netlify Drop）。ターミナルも Git も使いません。

PeerJS Cloud は登録もキーも不要で使えます。

## 過去のハンズオン

これまでに公開したハンズオン教材です（新しい順）。気になるものがあれば、この教材のあとにどうぞ。

- [パチンコ物理ゲームハンズオン](https://seekseep.github.io/slingshot-game-handson/)（2026-07）— Phaser 3 + Matter.js。鳥を飛ばして構造物を崩すアングリーバード風ゲームを作ります。
- [スイカゲーム風パズルハンズオン](https://seekseep.github.io/physics-based-game-handson/)（2026-07）— Phaser 3 + Matter.js。落として合体させる物理パズルを作ります。
- [Cloudflare 公開・運用ハンズオン](https://seekseep.github.io/cloudflare-introduction-handson/)（2026-06）— Cloudflare の無料プランで、作ったアプリを公開して運用するところまで。
- [AI Webapp Security ハンズオン 2026](https://seekseep.github.io/ai-webapp-security-handson-2026/)（2026-05）— 意図的に問題を仕込んだ Web アプリで、セキュリティとパフォーマンスを体験しながら直します。
- [シミュレーションゲーム作成ハンズオン 2026](https://github.com/seekseep/simulation-game-handson-2026)（2026-01）— 3D グラフィックス・API・データベース・AI を組み合わせて、単語を教えると話す動物キャラクターを作ります。
- [AI お絵描きハンズオン](https://github.com/seekseep/ai-drawing-handson)（2025-12）— HTML / CSS / JavaScript の基礎から、Canvas API を使ったお絵描きアプリまで。
- [Web アプリ開発の基本を学ぶハンズオン 2025](https://github.com/seekseep/webapp-handson-2025)（2025-02）— React でクライアント、Hono で Web API を作ります。
