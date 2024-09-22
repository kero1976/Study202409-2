"""
DynamoDB データの登録
"""
from logging import getLogger

from botocore.exceptions import ClientError

# ロガーの作成
logger = getLogger(__name__)


# DynamoDBのテーブルにデータを追加する関数
def add_item(resource, table_name, item):
    """
    DynamoDBテーブルにデータを追加する関数

    :param table_name: テーブル名
    :param item: 追加するデータ（辞書形式）
    :return: 成功した場合はTrue、失敗した場合はFalse
    """
    logger.debug({
        "status": "start",
        "params": {
            "resource": resource,
            "table_name": table_name,
            "item": item
        }
    })
    table = resource.Table(table_name)

    try:
        # アイテムをDynamoDBに追加
        table.put_item(Item=item)
        logger.info({"status": "success", "message": f"put_item({item})"})
        return True
    except ClientError as e:
        logger.error({"status": "fail", "message": f"{e.response['Error']['Message']}"})
        return False
