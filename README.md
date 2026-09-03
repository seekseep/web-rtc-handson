# web-rtc-handson

PeerJS（WebRTC）でブラウザ同士を直接つなぎ、**2 つの端末でいっしょに絵を描けるツール**を段階的に作るハンズオン教材です。「ボタンを押したら相手の画面が光る」ところから始めて、リアルタイムお絵かきまで組み立てます。作ったものは Netlify にドラッグ&ドロップで公開し、実際に自分のスマホと PC の 2 台で動かします。

## 構成

- **教材サイト本体**: [`apps/site/`](./apps/site/) — Astro + Starlight 製。教材ソース（`apps/site/README.md`・`apps/site/sections/`）から静的サイトを生成します。教材の読み方・目次は [apps/site/README.md](./apps/site/README.md) を参照。
- **完成サンプル**: [`apps/light/`](./apps/light/)（ボタンで光る）と [`apps/draw/`](./apps/draw/)（リアルタイムお絵かき） — 教材のゴールになる 2 つの完成形。`index.html` を開けば動きます。それぞれ [`03-connect/06-deploy`](./apps/site/sections/03-connect/06-deploy/example/) と [`05-drawing/07-deploy`](./apps/site/sections/05-drawing/07-deploy/example/) の `example/` と同じ中身です。

## 開発

```sh
pnpm install
pnpm dev
```

`pnpm build` で `apps/site/dist/` に静的サイトを出力します。`main` への push で GitHub Actions（[.github/workflows/deploy-docs.yml](./.github/workflows/deploy-docs.yml)）が GitHub Pages にデプロイします。

## 公開先

https://seekseep.github.io/web-rtc-handson/
