import csv
import os
from logging import getLogger

# サポートするエンコーディングのリスト
encodings = ['utf-8', 'cp932', 'shift_jis', 'iso-8859-1']

# ロガーの作成
logger = getLogger(__name__)


def file_exist(file_path: str) -> bool:
    """ファイルが存在するか確認する

    Args:
        file_path (str): _description_

    Returns:
        bool: _description_
    """
    logger.debug({"status": "start", "param": {"filepath": file_path}})
    logger.debug({"status": "run", "abspath": os.path.abspath(file_path)})
    result = os.path.isfile(file_path)
    logger.debug({"status": "success", "result": result})
    return result


def read_csv_with_unknown_encoding(file_path):
    logger.debug({"status": "start", "param": {"filepath": file_path}})
    for encoding in encodings:
        try:
            with open(file_path, mode="r", encoding=encoding) as file:
                reader = csv.reader(file)
                data = [row for row in reader]
            logger.info({
                "status": "success",
                "message": f"File loaded successfully with encoding: {encoding}"
            })
            return data
        except UnicodeDecodeError as e:
            logger.warning({
                "status": "run",
                "message": f"Failed to read with encoding {encoding}: {e}"
            })
    logger.error({"status": "fail", "message": "Could not determine the encoding."})

    return None
