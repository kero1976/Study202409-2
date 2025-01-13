# 1.elasticmqとは


# 2.サーバの起動方法

## 2-1.docker-compose.yaml

```
version: '3.8'
services:
  elasticmq:
    image: softwaremill/elasticmq
    container_name: elasticmq
    ports:
      - "9324:9324" # ElasticMQのデフォルトポート
    environment:
      - ELASTICMQ_SCALA_VERSION=2.13
    volumes:
      - ./elasticmq.conf:/opt/elasticmq.conf # カスタム設定ファイルを使用する場合
```