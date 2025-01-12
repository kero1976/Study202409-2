# 1.MinIOとは


# 2.MinIOサーバの起動方法

## 2-1.docker-compose.yaml

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

