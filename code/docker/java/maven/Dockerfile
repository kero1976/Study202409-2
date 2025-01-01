# Mavenを使用するための基本イメージ
FROM maven:3.9.5-eclipse-temurin-17 AS build

# 作業ディレクトリを設定
WORKDIR /app

# Mavenプロジェクトをコンテナにコピー
COPY pom.xml .
COPY src ./src

# プロジェクトをビルド
RUN mvn clean package

# 実行用の軽量JREイメージ
FROM eclipse-temurin:17-jre

# 作業ディレクトリを設定
WORKDIR /app

# ビルド成果物をコピー
COPY --from=build /app/target/maven-docker-sample-1.0-SNAPSHOT.jar app.jar

# コンテナ実行時にJavaプログラムを実行
CMD ["java", "-jar", "app.jar"]