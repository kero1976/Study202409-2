"""
DynamoDB データの登録
"""
from logging import getLogger

from awssample.connect.connect import Connect
from awssample.dynamodb.insert.base.insert import add_item

# ロガーの作成
logger = getLogger(__name__)


class Insert():
    """DynamoDB テーブル登録用クラス
    """

    def __init__(self, connect: Connect):
        self.connect = connect
        self.resource = None

    # DynamoDBのテーブルにデータを追加する関数
    def add_item(self, table_name: str, item: dict) -> bool:
        """
        DynamoDBテーブルにデータを追加する関数

        :param table_name: テーブル名
        :param item: 追加するデータ（辞書形式）
        :return: 成功した場合はTrue、失敗した場合はFalse
        """
        logger.debug({"status": "start", "params": {"table_name": table_name, "item": item}})
        if self.resource is None:
            self.resource = self.connect.get_resource()
        return add_item(self.resource, table_name, item)
