# 1.起動方法

## 1-1.ビルド

VSCODEのコンソールでWSLを選択し、Dockerfileがあるフォルダまで移動。
以下を実行する。

```
docker build .
```

## 1-2.作成したイメージの起動

```
docker run --env-file db.env　<イメージ>
```

## 1-3.起動したコンテナIDの確認

```
docker ps
```

## 1-4.起動したコンテナに接続

```
 docker exec -it <コンテナID> mysql -u root -p
```

# volumeの確認

https://qiita.com/akifumii/items/06e79428b09613235aa8



成功
grant all privileges on *.* to 'root'@'%' with grant option;
flush privileges; 
