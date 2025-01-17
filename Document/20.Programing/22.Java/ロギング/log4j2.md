# 1.インストール

```xml
    <dependencies>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-core</artifactId>
            <version>2.24.3</version>
        </dependency>
        <dependency>
            <groupId>org.apache.logging.log4j</groupId>
            <artifactId>log4j-api</artifactId>
            <version>2.24.3</version>
        </dependency>
    </dependencies>
```

# 9.Q&A

## 9-1.log4j2.xml を修正してもログが出力されない

log4j2.xml を読み込んでいるか、ファイルパスが正しいかプログラム内から確認する。

```java
package com.example;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.core.LoggerContext;
import org.apache.logging.log4j.core.config.Configuration;

public class App {
    private static final Logger logger = LogManager.getLogger(App.class);

    public static void main(String[] args) {
        logger.info("アプリケーションが開始されました。");
        LoggerContext context = (LoggerContext) LogManager.getContext(false);
        Configuration config = context.getConfiguration();
        logger.info("設定ファイルの場所: " + config.getConfigurationSource().getLocation());
        // ここにアプリケーションのロジックを追加します

        logger.info("アプリケーションが終了しました。");
    }
}
```
