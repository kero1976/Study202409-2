FROM ubuntu:latest

# Squid をインストール
RUN apt-get update && apt-get install -y squid && rm -rf /var/lib/apt/lists/*

# 設定ファイルをコピー
COPY squid.conf /etc/squid/squid.conf

# Squid の起動
CMD ["squid", "-N", "-d", "1"]