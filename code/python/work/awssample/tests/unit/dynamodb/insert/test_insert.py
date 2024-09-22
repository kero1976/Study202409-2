"""
インサートのテスト用ファイル
"""
import logging

from awssample.connect.connect import Connect
from awssample.dynamodb.create.create import Create
from awssample.dynamodb.insert.insert import Insert
from moto import mock_aws

logging.getLogger("botocore").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("boto3").setLevel(logging.ERROR)


@mock_aws
class TestInsert():

    def setup_method(self, method):
        dynamodb = Connect("dynamodb")
        Create(dynamodb).create_table("table")

    @mock_aws
    def test_add_item_ok(self):
        dynamodb = Connect("dynamodb")
        insert = Insert(dynamodb)
        assert insert.add_item("table", {"id": "a"}) is True

    def test_add_item_big_data_ok(self):
        dynamodb = Connect("dynamodb")
        insert = Insert(dynamodb)
        assert insert.add_item("table", {"id": "big", "data1": "1" * 400000}) is True

    def test_add_item_big_data_ng(self):
        dynamodb = Connect("dynamodb")
        insert = Insert(dynamodb)
        assert insert.add_item("table", {"id": "big", "data1": "1" * 500000}) is False

    def test_add_item_ng(self):
        dynamodb = Connect("dynamodb")
        insert = Insert(dynamodb)
        assert insert.add_item("table2", {"id": "a"}) is False
