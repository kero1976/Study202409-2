"""DynamoDB用Exception
"""


class DynamoDBException(Exception):
    """DynamoDB用Exception

    Args:
        Exception (_type_): _description_
    """

    def __init__(self, message: str, e: Exception):
        self.message = message
        self.e = e
