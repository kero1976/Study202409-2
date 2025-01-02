# docker build

## 1. 基本コマンド

コマンド形式

```
docker build .
```

Dockerfileがあるフォルダで実行する。
実行時に作成されたイメージIDを指定する必要があり、通常はタグを指定した方が良い。

## 2. 通常使うコマンド(タグあり)

コマンド形式

```
docker build -t <タグ名>[:バージョン] .
```

実行例

```
docker build -t mypro .
docker build -t mypro:1.1.1 .
```

## 3. ビルド失敗時の調査

ビルド時のログは簡略化されているため、詳細ログを確認するためには以下のコマンドを実行する。

コマンド形式

```
docker build --progress=plain .
```
