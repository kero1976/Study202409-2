import boto3
from awssample.dynamodb.create.base.create import create_table
from moto import mock_aws

# モックデータ
table_name = "TestTable"
key_schema = [{"AttributeName": "id", "KeyType": "HASH"}]
attribute_definitions = [{"AttributeName": "id", "AttributeType": "S"}]
provisioned_throughput = {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}


@mock_aws
def test_create_table():
    """motoを使用したテーブル作成
    """
    resource = boto3.resource("dynamodb")

    table = create_table(resource, table_name, key_schema, attribute_definitions,
                         provisioned_throughput)
    assert table
