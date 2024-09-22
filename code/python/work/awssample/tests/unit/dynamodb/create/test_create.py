from awssample.connect.connect import Connect
from awssample.dynamodb.create.create import Create
from moto import mock_aws


@mock_aws
def test_create():
    conn = Connect("dynamodb")
    dynamo = Create(conn)
    table = dynamo.create_table("foo2")
    assert table is True


@mock_aws
def test_create_error():
    conn = Connect("s3")
    dynamo = Create(conn)
    table = dynamo.create_table("foo2")
    assert table is False
