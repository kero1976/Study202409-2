"""deleteのテスト
"""
from awssample.connect.connect import Connect
from awssample.dynamodb.drop.delete import Delete
from moto import mock_aws


@mock_aws
def test_delete_ok():
    conn = Connect("dynamodb")
    dynamo = Delete(conn)
    result = dynamo.delete_table("foo2")
    assert result is True


@mock_aws
def test_delete_ng():
    conn = Connect("s3")
    dynamo = Delete(conn)
    result = dynamo.delete_table("foo2")
    assert result is False
