from awssample.connect.connect import Connect
from awssample.dynamodb.insert.insert import Insert


def test_add_item():
    dynamodb = Connect("dynamodb")
    insert = Insert(dynamodb)
    insert.add_item("table", {"id": "a"})
