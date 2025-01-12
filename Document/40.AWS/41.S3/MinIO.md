# 1.MinIOとは


# 2.MinIOサーバの起動方法

## 2-1.docker-compose.yaml

### 2-1-1.最小構成

```
version: "3.8"
services:
  minio:
    image: minio/minio:latest
    container_name: minio
    ports:
      - "9000:9000" # MinIOのWebアクセス用ポート
      - "9001:9001" # MinIOコンソール用ポート
    environment:
      MINIO_ROOT_USER: admin
      MINIO_ROOT_PASSWORD: admin123
    volumes:
      - ./data:/data # データを永続化するためのボリューム
    command: server /data
```
### 2-1-2.GUIあり

「command: server /data」だけだとブラウザからポート9001にアクセスできない。
listenはしているので、悩んだが、commandを以下の用にする必要がある。

```
    command: server /data --console-address ":9001"
```

### 2-1-3.最終系

```.env
MINIO_ROOT_USER=admin
MINIO_ROOT_PASSWORD=admin123
```

```docker-compose.yaml
version: "3.8"
services:
  minio:
    image: minio/minio:latest
    container_name: minio
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: ${MINIO_ROOT_USER}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD}
    volumes:
      - ./data:/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 5s
      timeout: 3s
      retries: 5
    command: server /data --console-address ":9001"

  createbuckets:
    image: minio/mc
    depends_on:
      minio:
        condition: service_healthy
    entrypoint: >
      /bin/sh -c "
      /usr/bin/mc alias set myminio http://minio:9000 ${MINIO_ROOT_USER} ${MINIO_ROOT_PASSWORD} && \
      /usr/bin/mc rm -r --force myminio/somebucketname || true && \
      /usr/bin/mc mb myminio/somebucketname && \
      /usr/bin/mc policy set download myminio/somebucketname && \
      exit 0
      "
```


# 3.mcコマンドについて

mcコマンドは同名のMidnight Commander (mc)というツールがあるので注意。

## 3-1.インストール方法

```
curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o $HOME/minio-binaries/mc

chmod +x $HOME/minio-binaries/mc
export PATH=$PATH:$HOME/minio-binaries/

mc --help
```

## 3-2.バケットの作成

### 3-2-1.エイリアス設定

```
mc alias set myminio http://localhost:9000 ACCESS_KEY SECRET_KEY
```

```
mc alias set myminio http://localhost:9000 admin admin123
```

### 3-2-2.バケット作成

```
mc mb myminio/somebucketname 
```

