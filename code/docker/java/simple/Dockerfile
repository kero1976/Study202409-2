# 基本イメージを指定
FROM openjdk:17-jdk-slim

# 作業ディレクトリを設定
WORKDIR /app

# Javaプログラムをコンテナにコピー
COPY . .

# Javaプログラムをコンパイル
RUN javac App.java

# コンテナ実行時にJavaプログラムを実行
CMD ["java", "App"]
