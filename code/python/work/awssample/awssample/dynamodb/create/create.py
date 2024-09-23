"""
DynamoDBのテーブル作成用ファイル
"""
from logging import getLogger

from awssample.connect.connect import Connect
from awssample.dynamodb.create.base.create import create_table_if_not_exists
from awssample.dynamodb.exception import DynamoDBException

# ロガーの作成
logger = getLogger(__name__)


class Create():
    """DynamoDBのテーブル作成用クラス
    """

    def __init__(self, connect: Connect):
        self.connect = connect

    def create_table(self, table_name: str) -> bool:
        """テーブル作成(冪等)

        Args:
            table_name (str): _description_
        """
        logger.debug({"status": "start", "params": {"table_name": table_name}})
        key_schema = [{
            "AttributeName": "id",  # パーティションキーの属性名
            "KeyType": "HASH"  # パーティションキー
        }]

        attribute_definitions = [{
            "AttributeName": "id",
            "AttributeType": "S"  # 文字列型 (S: String, N: Number, B: Binary)
        }]

        provisioned_throughput = {
            "ReadCapacityUnits": 5,  # 読み取りキャパシティ
            "WriteCapacityUnits": 5  # 書き込みキャパシティ
        }
        try:
            create_table_if_not_exists(self.connect.get_resource(), table_name, key_schema,
                                       attribute_definitions, provisioned_throughput)

            logger.info({
                "status": "success",
                "message": f"'{table_name}' table successfully created!"
            })
            return True
        except DynamoDBException as e:
            logger.error({
                "status": "fail",
                "message": f"creation of '{table_name}' table failed!",
                "exception": e
            })
            return False

    def create_table_custom(self, table_name: str, key_schema: list[dict],
                            attribute_definitions: list[dict],
                            provisioned_throughput: dict) -> bool:
        """テーブル作成(冪等)

        Args:
            table_name (str): _description_
        """
        logger.debug({
            "status": "start",
            "params": {
                "table_name": table_name,
                "key_schema": key_schema,
                "attribute_definitions": attribute_definitions,
                "provisioned_throughput": provisioned_throughput
            }
        })

        try:
            create_table_if_not_exists(self.connect.get_resource(), table_name, key_schema,
                                       attribute_definitions, provisioned_throughput)

            logger.info({
                "status": "success",
                "message": f"'{table_name}' table successfully created!"
            })
            return True
        except DynamoDBException as e:
            logger.error({
                "status": "fail",
                "message": f"creation of '{table_name}' table failed!",
                "exception": e
            })
            return False
