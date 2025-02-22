# 1. Maven を使用して Java プログラムを実行

## 1-1.説明

Java の Main メソッドからプログラムを実行したい場合のやり方

## 1-2.pom.xml

```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.0.0</version>
                <configuration>
                    <mainClass>com.example.App</mainClass>
                </configuration>
            </plugin>
        </plugins>
    </build>
```

## 1-3.実行コマンド

```
mvn compile exec:java
```

# 2.Maven が使用する Java のバージョンを変更する。

1. プロジェクトの直下に「.vscode/settings.json」ファイルを作成する

2. その中で Maven で使用する JDK を指定する

```
    "maven.terminal.customEnv": [
		{
		  "environmentVariable": "JAVA_HOME",
		  "value": "C:\\Users\\kero\\AppData\\Roaming\\Code\\User\\globalStorage\\pleiades.java-extension-pack-jdk\\java\\17"
		}
	  ],
```
