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
