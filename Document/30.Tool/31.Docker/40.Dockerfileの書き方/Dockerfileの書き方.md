# Dockerfileの書き方

# 1. 基本的な内容

* 上から順に実行される
  * 実行順を考え、なるべく上の行に変更になるのを書かない
* 1行が1レイヤー
  * インストールなどは可能なら1行にまとめる

# 2. 使用できるコマンド

* FROM
* ENTRYPOINT
* RUN
* CMD
* ENV
* ARG
* COPY

## 2-1. FROM

イメージを指定する
指定するイメージは以下から探す

https://hub.docker.com/

イメージの種類について
https://qiita.com/tRbiWbc3hnM1Aor/items/ad319d434675236e3fcd

## 2-2. ENVとARG

ENVはDockerfileに記載することも、コンテナ実行時に指定することも可能。

以下はDockerfile内の抜粋

```Dockerfile
ENV PORT 80
EXPOSE $PORT
```

そのため、ポート番号を変更する際に、イメージの再作成が不要になる。
Dockerfileに指定した値はデフォルト値のため、実行時に上書き可能なため。

実行時は
--ENV PORT=8080 または -e PORT=8080
と指定する。
--env-fileの指定も可能。

## 2-3.COPY

```
COPY コピー元のローカル コピー先のDocker
```

上の階層のコピーが出来なかった。
ビルドコンテキストの
