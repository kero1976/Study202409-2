"""

標準CSVファイルを読み込むモジュール

1列のデータを1行としたファイルを読み込む。
CSVファイルの列数が5列の場合は、必ず5行のデータとなる。

■想定するCSVファイル
"ID","名前","住所","性別","オプション情報"
"1","山田太郎","不明","男","未設定"
"2","佐藤花子","不明","女","未設定"
"3","田中一郎","不明","男","未設定"

■標準CSVファイルの例1
""
""
"不明"
""
"未設定"

■標準CSVファイルの2
"ID",""
"名前",""
"住所",""不明"
"性別",""
"オプション情報","未設定"
"""
import csv
import os
from logging import getLogger

logger = getLogger(__name__)


def read_csv_file(file_path: str) -> list[list[str]] | None:
    """CSVファイルを読み込む関数
    読み込めない場合はNoneを返す。
    
    Args:
        file_path (str): CSVファイルのパス

    Returns:
        list[list[str]]: CSVファイルの内容をリストとして返す
    """
    logger.debug({
        "status": "start  ",
        "message": "read_csv_file start.",
        "params": {
            "file_path": file_path
        }
    })
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            content = [row for row in csv_reader]
        logger.debug({
            "status": "success",
            "message": "read_csv_file success.",
            "result": content
        })
        return content
    except FileNotFoundError:
        logger.debug({
            "status": "failure",
            "message": "read_csv_file FileNotFoundError.",
            "result": {
                "abspath": os.path.abspath(file_path),
                "error": "File not found."
            }
        })
        return None
    except Exception as e:
        logger.debug({
            "status": "failure",
            "message": "read_csv_file error.",
            "result": {
                "abspath": os.path.abspath(file_path),
                "error": str(e)
            }
        })
        return None


class DefaultCsvReader:
    """標準CSVファイルCSVファイルを読み込むクラス
    読み込めない場合はNoneを返す。
    
    Attributes:
        file_path (str): CSVファイルのパス
    """

    def __init__(self, file_path: str) -> None:
        """コンストラクタ
        Args:
            file_path (str): CSVファイルのパス
        """
        logger.debug({
            "status": "init   ",
            "message": "DefaultCsvReader Create.",
            "params": {
                "file_path": file_path
            }
        })
        self.file_path = file_path
        self.raw_datasets = read_csv_file(file_path)

    def read(self) -> list[str] | None:
        """標準CSVデータを読み込んで1行のデータ配列を返す
        
        Returns:
            list[str]: CSVファイルの内容をリストとして返す
        """
        logger.debug({
            "status": "start  ",
            "message": "DefaultCsvReader read start.",
        })
        if self.raw_datasets is None:
            logger.debug({
                "status": "failure",
                "message": "DefaultCsvReader read error.",
                "result": {
                    "abspath": os.path.abspath(self.file_path),
                    "error": "File not found."
                }
            })
            return None
        row = []
        for row_data in self.raw_datasets:
            if len(row_data) == 2:
                row.append(row_data[1])
            else:
                row.append(row_data[0])
        logger.debug({
            "status": "success",
            "message": "DefaultCsvReader read success.",
            "result": row
        })
        return row
