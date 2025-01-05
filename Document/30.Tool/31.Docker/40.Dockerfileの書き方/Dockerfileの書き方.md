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

## 2-1. FROM

イメージを指定する
指定するイメージは以下から探す

https://hub.docker.com/

イメージの種類について
https://qiita.com/tRbiWbc3hnM1Aor/items/ad319d434675236e3fcd

## 2-1-1. Java開発環境

