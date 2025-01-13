# SLF4J + Logback
https://blog.kengo-toda.jp/entry/2023/12/15/111624

# インストール
```
        <!-- SLF4J API -->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-api</artifactId>
            <version>2.0.16</version>
        </dependency>

        <!-- Logback Classic -->
        <dependency>
            <groupId>ch.qos.logback</groupId>
            <artifactId>logback-classic</artifactId>
            <version>1.5.16</version>
        </dependency>
```

# JUnit実行時の確認

「デバッグコンソール」タブに出力される。
「出力」、「テスト結果」、「ターミナル」では無いので注意。