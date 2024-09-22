"""
DynamoDBのテーブル作成用ファイル
"""
from logging import getLogger

from awssample.dynamodb.exception import DynamoDBException
from botocore.exceptions import ClientError

# ロガーの作成
logger = getLogger(__name__)


def create_table(resource, table_name: str, key_schema: list[dict],
                 attribute_definitions: list[dict], provisioned_throughput: dict):
    """テーブル作成。作成後待機。

    Args:
        resource (_type_): _description_
        table_name (str): テーブル名
        key_schema (list[dict]): _description_
        attribute_definitions (list[dict]): _description_
        provisioned_throughput (dict): _description_
    """
    logger.debug({
        "status": "start",
        "params": {
            "resource": resource,
            "table_name": table_name,
            "key_schema": key_schema,
            "attribute_definitions": attribute_definitions,
            "provisioned_throughput": provisioned_throughput
        }
    })

    # テーブルの作成
    table = resource.create_table(
        TableName=table_name,  # テーブル名
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput)

    # テーブルが作成されるまで待機
    table.meta.client.get_waiter("table_exists").wait(TableName=table_name)
    logger.info({"status": "success", "result": table})

    return table


def create_table_if_not_exists(resource, table_name: str, key_schema: list[dict],
                               attribute_definitions: list[dict], provisioned_throughput: dict):
    """テーブルが存在しない場合は作成する
    Args:
        resource (_type_): _description_
        table_name (str): _description_
        key_schema (list[dict]): _description_
        attribute_definitions (list[dict]): _description_
        provisioned_throughput (dict): _description_

    Returns:
        _type_: _description_
    """
    logger.debug({"status": "start", "params": {"resource": resource, "table_name": table_name}})
    try:
        # 既存のテーブルの一覧を取得
        existing_tables = list(resource.tables.all())
        logger.debug({"status": "run", "message": f"all table len={len(existing_tables)}"})
        if any(table.name == table_name for table in existing_tables):
            logger.info({"status": "success", "message": f"Table {table_name} is exist."})
            return resource.Table(table_name)

        table = create_table(resource, table_name, key_schema, attribute_definitions,
                             provisioned_throughput)
        logger.info({"status": "success", "message": f"Table {table_name} is created."})
        return table
    except ClientError as e:
        # すでにテーブルが存在している場合は例外を無視
        if e.response["Error"]["Code"] == "ResourceInUseException":
            logger.info({"status": "success", "message": f"Table {table_name} is exist."})
            return resource.Table(table_name)
        logger.error({
            "status": "fail",
            "message": f"ClientError! creation of '{table_name}' table failed!",
            "exception": e
        })
        raise DynamoDBException("create error.", e) from e
    except Exception as e:
        logger.error({
            "status": "fail",
            "message": f"Other Error! creation of '{table_name}' table failed!",
            "exception": e
        })
        raise DynamoDBException("create error.", e) from e
