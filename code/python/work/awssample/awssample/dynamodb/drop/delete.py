"""
DynamoDB テーブル削除用ファイル
"""
from logging import getLogger

from awssample.connect.connect import Connect
from awssample.dynamodb.drop.base import delete
from awssample.dynamodb.exception import DynamoDBException

# ロガーの作成
logger = getLogger(__name__)


# pylint: disable=R0903
class Delete():
    """DynamoDB テーブル削除用クラス
    """

    def __init__(self, connect: Connect):
        self.connect = connect

    def delete_table(self, table_name: str) -> bool:

        logger.debug({"status": "start", "params": {"table_name": table_name}})
        try:
            delete.delete_table(self.connect.get_client(), table_name)
            logger.info({
                "status": "success",
                "message": f"'{table_name}' table successfully deleted!"
            })
            return True
        except DynamoDBException as e:
            logger.error({
                "status": "fail",
                "message": f"delete of '{table_name}' table failed!",
                "exception": e
            })
            return False
