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

## 4.ユーザ認証を追加

### 4-1.認証用のパスワードファイルを作成

Squid は htpasswd 形式の認証ファイルを使用できる。
まず htpasswd コマンドを使って認証用のユーザーを作成する。

```sh
sudo apt-get install apache2-utils  # (Ubuntu) htpasswd コマンドをインストール
htpasswd -c ./passwd myuser
```

-c は新規作成（既存のファイルがある場合は 不要）。
myuser がプロキシ認証で使用するユーザー名。
パスワードを入力すると passwd ファイルが作成される

### 4-2.squid.confファイルの修正

```conf
http_port 3128

# 認証の設定
# # Basic 認証を有効化し、パスワードファイルを指定
auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd
# # Basic 認証を有効化し、パスワードファイルを指定
auth_param basic realm Proxy Server
# # proxy_auth を使う acl (アクセス制御リスト) を作成
acl authenticated proxy_auth REQUIRED
# # proxy_auth を使う acl (アクセス制御リスト) を作成
http_access allow authenticated

# 他のリクエストは拒否
http_access deny all

# ログ設定（省略可能）
access_log /var/log/squid/access.log squid
cache_log /var/log/squid/cache.log
```

### 4-3.Dockerfileを修正

```
FROM ubuntu:latest

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y squid apache2-utils && rm -rf /var/lib/apt/lists/*

# Squid 設定ファイルとパスワードファイルをコピー
COPY squid.conf /etc/squid/squid.conf
COPY passwd /etc/squid/passwd

# パスワードファイルの権限を適切に設定
RUN chmod 400 /etc/squid/passwd

# Squid の起動
CMD ["squid", "-N", "-d", "1"]
```

### 4-4.docker-compose.yamlの修正

```
version: '3'
services:
  squid:
    build: .
    container_name: squid-proxy
    restart: unless-stopped
    ports:
      - "3128:3128"
    volumes:
      - ./squid.conf:/etc/squid/squid.conf
      - ./passwd:/etc/squid/passwd
      - ./logs:/var/log/squid

```

### 4-5.動作確認

```
curl -x http://myuser:passw0rd@localhost:3128 -L https://www.google.com
curl -x http://localhost:3128 -U myuser -L https://www.google.com
```