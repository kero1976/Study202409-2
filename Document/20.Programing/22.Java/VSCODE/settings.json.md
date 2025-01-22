# 1.settings.json の修正方法

Ctrl + Shift + P

## 2-1.pom.xml ファイルのフォーマット

settings.json に以下を記載する

```
{
  "editor.formatOnSave": true,
  "[xml]": {
    "editor.defaultFormatter": "redhat.vscode-xml" // または使用するXMLフォーマッタ
  }
}
```

## 2-2.不要な import 文の削除

```
  "editor.codeActionsOnSave": {
    "source.organizeImports": "always"
  }
```

## 2-3.Java 色々

- import 文の整理
- 自動フォーマット
- タブを空白に置き換え

```
{
    "[java]": {
        "editor.defaultFormatter": "redhat.java",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
          "source.organizeImports": "explicit",
          "source.fixAll": true
        }
    }
}
```

- Java ファイルのデフォルトフォーマッターとして redhat の Java フォーマッタを使用する
- "editor.formatOnSave": true Java ファイルを保存する際に自動的にフォーマットを行う
- "editor.codeActionsOnSave"ファイルを保存する際に実行されるコードアクション
- "source.organizeImports": "explicit" インポート文を整理する
- "source.fixAll": true 可能なすべての修正を適用する
