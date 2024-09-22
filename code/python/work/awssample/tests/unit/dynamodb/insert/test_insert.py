from awssample.connect.connect import Connect
from awssample.dynamodb.insert.insert import Insert
import logging

logging.getLogger("botocore").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("boto3").setLevel(logging.ERROR)


def test_add_item():
    dynamodb = Connect("dynamodb", "shijo")
    insert = Insert(dynamodb)
    insert.add_item("table", {"id": "a"})
