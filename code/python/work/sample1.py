import boto3

# DynamoDBのクライアントを作成
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')

# テーブルを作成する
def create_table():
    try:
        # テーブルの作成
        table = dynamodb.create_table(
            TableName='SampleTable',  # テーブル名
            KeySchema=[
                {
                    'AttributeName': 'id',  # パーティションキーの属性名
                    'KeyType': 'HASH'  # パーティションキー
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'  # 文字列型 (S: String, N: Number, B: Binary)
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,  # 読み取りキャパシティ
                'WriteCapacityUnits': 5  # 書き込みキャパシティ
            }
        )

        # テーブルが作成されるまで待機
        table.meta.client.get_waiter('table_exists').wait(TableName='SampleTable')
        print("テーブルが正常に作成されました")
    
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# テーブルを作成する関数を実行
create_table()
