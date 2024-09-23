"""シナリオテスト
"""

from awssample.connect.connect import Connect
from awssample.dynamodb.create.create import Create
from awssample.dynamodb.drop.delete import Delete
from awssample.dynamodb.insert.insert import Insert
from moto import mock_aws

TABLE_NAME = "test20240922"


def test_case1():
    """テーブルを作成し、テーブルを削除する
    """
    dynamodb = Connect("dynamodb", endpoint_url="http://localhost:8000")
    insert = Insert(dynamodb)
    Create(dynamodb).create_table(TABLE_NAME)
    for i in range(10000):
        insert.add_item(TABLE_NAME, {"id": f"test4{i}", "foo1": "1"})
    # Delete(dynamodb).delete_table(TABLE_NAME)
