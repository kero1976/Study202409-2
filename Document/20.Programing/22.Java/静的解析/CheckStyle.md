# 1.CheckStyle

## 1-1.pom.xml

```xml
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.6.0</version>
                <configuration>
                    <configLocation>checkstyle.xml</configLocation>
                    <outputFile>target/checkstyle-result.xml</outputFile>
                    <outputFileFormat>xml</outputFileFormat>
                    <failOnViolation>false</failOnViolation>
                </configuration>
                <executions>
                    <execution>
                        <phase>validate</phase>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
```

- Lifecycle の validate フェーズで CheckStyle の check 処理を行う
- failOnViolation を false で CheckStyle の違反があってもビルドを失敗にしない

## 1-2.設定ファイル

```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN" "https://checkstyle.sourceforge.io/dtds/configuration_1_3.dtd">

<module name="Checker">
    <!-- ファイル全体の設定 -->
    <module name="TreeWalker">
        <!-- クラス名は大文字で始める -->
        <module name="TypeName">
            <property name="format" value="^[A-Z][a-zA-Z0-9]*$" />
        </module>

        <!-- メソッド名は小文字で始める -->
        <module name="MethodName">
            <property name="format" value="^[a-z][a-zA-Z0-9]*$" />
        </module>


        <!-- インデントを4スペースに設定 -->
        <module name="Indentation">
            <property name="basicOffset" value="4" />
            <property name="braceAdjustment" value="0" />
            <property name="caseIndent" value="4" />
            <property name="lineWrappingIndentation" value="8" />
        </module>

        <!-- 不要なインポートをチェック -->
        <module name="UnusedImports" />


        <!-- 1つのファイルに1つのトップレベルクラスのみ -->
        <module name="OneTopLevelClass" />

        <!-- コメントスタイルのチェック -->
        <module name="JavadocStyle" />
        <module name="JavadocType" />

        <!-- コーディング標準に準拠したインポート順 -->
        <module name="ImportOrder">
            <property name="option" value="under" />
            <property name="groups" value="java,javax,org,com" />
            <property name="ordered" value="true" />
            <property name="separated" value="true" />
        </module>
    </module>
    <!-- 行の長さ制限 -->
    <module name="LineLength">
        <property name="max" value="100" />
    </module>

    <!-- ファイルの最後は空行で終わる -->
    <module name="NewlineAtEndOfFile" />


</module>
```

## 1-3.実行方法

maven で validate を実行する
