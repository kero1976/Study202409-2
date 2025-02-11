# 1.コマンド

```
docker run -p 9000:9000 --rm sonarqube:9.9.8-community
```

# 2.使い方

## 2-1.初期設定

1. http://localhost:9000/
2. admin/admin
3. パスワード変更(P@ssw0rd)

## 2-2.maven 実行

pom.xml の build 以下に sonarqube プラグインを設定する。

## 2-3.SonarQube プロジェクトの設定

1. Projects タブで新規プロジェクトを作成
2. リポジトリを聞かれるので、「Locally」を選択
3. トークン作成画面になるので、トークン作成
4. 「Run analysis on your project」と聞かれるので、Maven を選択
5. maven のコマンドが表示されるので、それを実行する。

# 9.トラブル対応

## 9-1.http://localhost:9000/api/server/version 503

SonarQube のサーバに接続できていないのが原因。
Maven で Proxy 設定している場合は、localhost に Proxy 経由で接続しようとしていることが原因。

/.m2/settings.xml

```
<proxy>
    <nonProxyHosts>localhost</nonProxyHosts>
</proxy>
```
