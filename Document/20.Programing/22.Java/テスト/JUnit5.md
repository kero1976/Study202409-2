# インストール

## 1. pom.xml

```
    <!-- JUnit 5 -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter</artifactId>
        <version>5.11.4</version>
        <scope>test</scope>
    </dependency>
```

## 2. Maven からテスト実行

maven-surefire-plugin を使用する。
プラグインは build の下に指定する。

```
  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>3.5.2</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
```

### 2-1.テストの実行フォルダを変更

maven-surefire-plugin に以下の設定を追加する。

```
                    <configuration>
                        <workingDirectory>${java.io.tmpdir}/hoge</workingDirectory>
                    </configuration>
```

上記の例では、実行時フォルダは以下になる。
C:\Users\kero\AppData\Local\Temp\hoge
