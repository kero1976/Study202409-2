GitLens — Git supercharged
v15.4.0

git config --global user.name "kero"
git config --global user.email kero1976@outlook.jp


## TIPS

### 1.誤ってバージョン管理対象外ファイルをコミットした場合

1. gitignoreにファイルを追加
2. コミット履歴からファイルを削除「git rm --cached <ファイル名> # 例: git rm --cached config.py」
3. コミットする