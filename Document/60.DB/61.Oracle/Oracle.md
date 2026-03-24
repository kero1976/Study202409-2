# Clientのインストール

NT_193000_client.zipとNT_193000_client_home.zipがある。

homeが付いているのはゴールデンイメージ。homeが付いていないのでインストールする。

# Orale Instant Client 12.2.0.1

# Oracle 19

V982656-01をダウンロード。

## SQL

### 接続確認

show con_name;

CDB$ROOTとなっていたらCDBに接続している。

### PDBの名前とアクセス権限の確認

select name,openmode from v$pdbs;

### PDBスタート

ALTER PLUGGABLE DATABASE <PDB名> OPEN;

### 切替

ALTER SESSION SET CONTAINER =<PDB名>

# 2.ツール

## 2-1.SQLPLUS# 接続方法

sqlplus ユーザ名/パスワード@エンドポイント:1521/DB名

## 2-2.ODBCとNETCA

### 接続方法

#### netca

- 「ローカル・ネット・サービス名構成」を選択
- 「追加」を選択
- サービス名に「ORCL」を選択
- 「TCP」を選択
- ホスト名にエンドポイントを入力
- 任意の名前を付ける。この名前をODBCで使用する。

#### ODBC

- 「TNSサービス名」に自分でつけた名前を設定
- 「ユーザーID」にユーザ名/パスワードを入力する
