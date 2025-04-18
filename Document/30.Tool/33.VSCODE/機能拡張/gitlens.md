# 1.はじめに

gitのインストールが必要

# 2.基本的な使い方

## 2-1.githubにあるプロジェクトを取得

以下のいずれかを選択

* ようこそ画面で、「Gitリポジトリのクローン」を選択




GitLens — Git supercharged
v15.4.0

git config --global user.name "kero"
git config --global user.email kero1976@outlook.jp

## VSCODEとgithubとの連携方法
1. 「GitHubに公開」を選択する
2. ブラウザが立ち上がるのでログインする

## TIPS

### 1.誤ってバージョン管理対象外ファイルをコミットした場合

1. gitignoreにファイルを追加
2. コミット履歴からファイルを削除「git rm --cached <ファイル名> # 例: git rm --cached config.py」
3. コミットする