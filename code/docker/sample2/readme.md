# 1.起動方法

## 1-1.ビルド

VSCODEのコンソールでWSLを選択し、Dockerfileがあるフォルダまで移動。
以下を実行する。

```
docker build -t foo:bar .
```

-tオプションでタグを指定。

## 1-2.作成したイメージの起動

```
docker run --env-file db.env --name bar1 --rm -p 3306:3306 foo:bar
```

## 1-3.起動したコンテナIDの確認

```
docker ps
```

## 1-4.起動したコンテナに接続

```
docker exec -it bar1 mysql -u root -pP@ssw0rd
```

# 2.設定説明

## 2-1.テーブルの作成

docker-entrypoint-initdb.dフォルダの下にSQL文のファイルを置けば実行される

# volumeの確認

https://qiita.com/akifumii/items/06e79428b09613235aa8



成功
grant all privileges on *.* to 'root'@'%' with grant option;
flush privileges; 
