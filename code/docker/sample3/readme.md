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

### 1-2-1.rmオプションについて

--rmを指定して、終了時にコンテナイメージを削除している。
これが無いと、コンテナを新規に作成した際に、既存のvolumeを使用して、挙動が怪しくなる。
コンテナ終了時にコンテナイメージとvolumeが削除されるので挙動が怪しくなることが無い。

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

# 3. Dockerfileについて

## 3-1.MySQLで日本語化できない問題について

mysql8.0で日本語化できない、全角入力しても消える現象が発生した。
OSが日本語化対応していないのが原因で、apt-getでlocaledefをインストールする必要がある。
ただ、apt-getｇは入っていないという問題があり、イメージ指定でdebianを選択する必要があった。

## 3-2.Oracle Linux Serverでの日本語確認

microdnf install -y glibc-locale-source
でうまく日本語入力ができるようになった。

ただ、proxyが必要な環境で、microdnfが動かない現象が発生し、解決方法が不明なまま。

# 4.接続確認

Windows環境でポートが開いているか確認する

```
netstat -an | findstr 3306
```