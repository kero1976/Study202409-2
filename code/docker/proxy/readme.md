# squidを使ったProxy環境をDockerで構築する

## 1.Docker コンテナをビルド & 起動
以下のコマンドを実行して、Squid プロキシを起動します。

```sh
docker compose up -d --build
```

## 2.動作確認
クライアントから Squid プロキシを使用するには、ブラウザや curl のプロキシ設定を変更する

### 2-1.curl でテスト
以下のコマンドを実行し、プロキシ経由で https://www.google.com にアクセスできるか確認します。

```sh
curl -x http://localhost:3128 -L https://www.google.com
```

エラーが出ずにレスポンスが返ってくれば成功

### 2-2.ブラウザで設定
ブラウザのプロキシ設定で http://localhost:3128 を指定する

## 3.ログの確認

```sh
docker exec -it squid-proxy tail -f /var/log/squid/access.log
```