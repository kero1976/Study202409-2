# 1.settings.jsonの修正方法

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
