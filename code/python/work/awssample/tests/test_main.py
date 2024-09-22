"""シナリオテスト
"""

from awssample.connect.connect import Connect
from awssample.dynamodb.create.create import Create
from awssample.dynamodb.drop.delete import Delete
from awssample.dynamodb.insert.insert import Insert
from moto import mock_aws

TABLE_NAME = "test20240922"


@mock_aws
def test_case1():
    """テーブルを作成し、テーブルを削除する
    """
    dynamodb = Connect("dynamodb", "shijo", "ap-northeast-1")
    insert = Insert(dynamodb)
    Create(dynamodb).create_table(TABLE_NAME)
    for i in range(1):
        insert.add_item(TABLE_NAME, {"id": f"test4{i}", "foo": "bar"})
    Delete(dynamodb).delete_table(TABLE_NAME)
