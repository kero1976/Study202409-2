"""Mockを使って実際にAWSリソースにはアクセスしないinsertのテストファイル
"""
from unittest.mock import MagicMock

from awssample.dynamodb.insert.base.insert import add_item
from botocore.exceptions import ClientError


def test_add_item_mock_ok():

    mock = MagicMock()

    result = add_item(mock, "foo1", {"id": "A6", "data": "BBB5"})
    assert result


def test_add_item_mock_ng():
    mock = MagicMock()
    table = MagicMock()
    error_response = {
        "Error": {
            "Code": "ResourceInUseException",
            "Message": "You are not authorized"
        }
    }

    table.put_item.side_effect = ClientError(error_response, "CreateTable")
    mock.Table.return_value = table

    result = add_item(mock, "foo1", {"id": "A6", "data": "BBB5"})
    assert result is False
