"""Mockを使って実際にAWSリソースにはアクセスしないcreateのテストファイル
"""
from unittest.mock import MagicMock, patch

import pytest
from awssample.dynamodb.create.base.create import create_table_if_not_exists
from awssample.dynamodb.exception import DynamoDBException
from botocore.exceptions import ClientError

# モックデータ
table_name = "TestTable"
key_schema = [{"AttributeName": "id", "KeyType": "HASH"}]
attribute_definitions = [{"AttributeName": "id", "AttributeType": "S"}]
provisioned_throughput = {"ReadCapacityUnits": 5, "WriteCapacityUnits": 5}

TEST_METHOD_NAME = "awssample.dynamodb.create.base.create.create_table"


def test_create_table_if_exists_mock():
    """テーブルが既に存在する場合のテスト"""
    # DynamoDB resourceのモックを作成
    resource_mock = MagicMock()
    table_mock = MagicMock()

    # テーブルが既に存在する場合
    resource_mock.tables.all.return_value = [table_mock]
    table_mock.name = table_name

    # 関数を実行
    table = create_table_if_not_exists(resource_mock, table_name, key_schema, attribute_definitions,
                                       provisioned_throughput)

    assert table
    resource_mock.Table.assert_called_once_with(table_name)


def test_create_table_if_not_exists_mock():
    """テーブルが存在しない場合のテスト
    create_table_if_not_existsは内部でcreate_tableを呼んでいるので、create_tableをモックにする
    """
    # DynamoDB resourceのモックを作成
    resource_mock = MagicMock()
    table_mock = MagicMock()

    # テーブルが存在しない場合
    resource_mock.tables.all.return_value = []

    # テーブル作成用の関数をモック
    with patch(TEST_METHOD_NAME, return_value=table_mock) as create_table_mock:
        # 関数を実行
        table = create_table_if_not_exists(resource_mock, table_name, key_schema,
                                           attribute_definitions, provisioned_throughput)

        # テーブルが作成され、返されることを確認

        assert table == table_mock
        create_table_mock.assert_called_once_with(resource_mock, table_name, key_schema,
                                                  attribute_definitions, provisioned_throughput)
        resource_mock.Table.assert_not_called()


def test_create_table_resource_in_use_mock():
    """ResourceInUseExceptionが発生する場合のテスト
    """
    # DynamoDB resourceのモックを作成
    resource_mock = MagicMock()

    # テーブルが存在しないが、ResourceInUseException が発生する場合
    resource_mock.tables.all.return_value = []
    error_response = {"Error": {"Code": "ResourceInUseException"}}
    client_error = ClientError(error_response, "CreateTable")

    with patch(TEST_METHOD_NAME, side_effect=client_error):
        create_table_if_not_exists(resource_mock, table_name, key_schema, attribute_definitions,
                                   provisioned_throughput)

        # テーブルが存在するとして返されることを確認
        resource_mock.Table.assert_called_once_with(table_name)


def test_create_table_raises_unexpected_error():
    # DynamoDB resourceのモックを作成
    resource_mock = MagicMock()

    # テーブルが存在しない場合
    resource_mock.tables.all.return_value = []

    # エラーレスポンスをモック（例: "AccessDeniedException" のエラーを発生させる）
    error_response = {
        "Error": {
            "Code": "AccessDeniedException",
            "Message": "You are not authorized"
        }
    }
    client_error = ClientError(error_response, "CreateTable")

    # create_table関数をモックして、ClientErrorを発生させる
    with patch(TEST_METHOD_NAME, side_effect=client_error):
        # 例外が発生するかを確認
        with pytest.raises(DynamoDBException) as exc_info:
            create_table_if_not_exists(resource_mock, table_name, key_schema, attribute_definitions,
                                       provisioned_throughput)

        # エラーメッセージを確認
        assert exc_info.value.e.response["Error"]["Code"] == "AccessDeniedException"
