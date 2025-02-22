# <maven.compiler.source> と <maven.compiler.target> を別々に指定する理由

ソースコードの互換性と生成されるバイトコードの互換性を個別に設定するためです。
これにより、異なるバージョンの Java を使用してソースコードを記述し、異なるバージョンの Java で実行可能なバイトコードを生成することができます。

具体的には以下のようなケースがあります：

## 新しい構文を使用しつつ古いバージョンの互換性を保つ:

新しいバージョンの Java の構文や機能を使用してソースコードを記述しつつ、古いバージョンの Java で実行可能なバイトコードを生成する場合です。
例えば、Java 17 の構文を使用してソースコードを記述し、Java 11 で実行可能なバイトコードを生成する場合、以下のように設定します。

```
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
</properties>
```

## 互換性のあるバージョンを指定

プロジェクトの一部が特定の Java バージョンに依存している場合、そのバージョンに合わせてソースコードとバイトコードの互換性を設定することができます。

```
<properties>
    <maven.compiler.source>17</maven.compiler.source>
    <maven.compiler.target>17</maven.compiler.target>
</properties>
```

この設定は、Java 17 の構文を使用してソースコードを記述し、Java 17 で実行可能なバイトコードを生成することを意味します。これにより、Java 17 の新機能をフルに活用しつつ、Java 17 互換の環境で実行することができます。

異なるバージョンを指定する場合は、プロジェクトの要件に応じて適切に設定してください。

# 実行時の環境について

VSCODE では pom.xml の値を見て、使用する Java のバージョンを切り替えている。
