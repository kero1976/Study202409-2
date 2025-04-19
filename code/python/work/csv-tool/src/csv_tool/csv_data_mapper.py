"""
標準CSVと入力CSVをマッピングするモジュール

マッピング情報を受け取り、1行の入力CSVから1行の出力CSVを生成する。
"""
from logging import getLogger
from csv_tool.read_default_csv import DefaultCsvReader

logger = getLogger(__name__)


class CsvDataMapper:
    """CSVデータマッパークラス"""

    def __init__(self, mapping_info: str,
                 default_csv: DefaultCsvReader) -> None:
        """コンストラクタ
        Args:
            mapping_info (str): マッピング情報
        """
        logger.debug({
            "status": "init   ",
            "message": "CsvDataMapper Create.",
            "params": {
                "mapping_info": mapping_info,
                "default_csv": default_csv
            }
        })
        self.mapping_info = mapping_info
        self.default_csv = default_csv

    def create_date(self, csv_row: list[str], mapping: list[str]) -> list[str]:
        """入力CSVデータの1行から、標準CSVデータを使用して出力CSVデータの1行を作成する
        
        Args:
            csv_row (list[str]): 入力CSVファイルの1行のデータ
            mapping (list[str]): 入力CSVファイルの1行のデータに対するマッピング情報
        Returns:
            str: CSVファイルの内容をリストとして返す
        """
        logger.debug({
            "status": "start  ",
            "message": "DefaultCsvReader create_date start.",
            "params": {
                "csv_row": csv_row,
                "mapping": mapping
            }
        })
        base_csv = self.default_csv.read()
        # forループでカウントを取得
        for i, map in enumerate(mapping):
            # マッピング情報が空の場合はスキップ
            if map == "":
                continue
            # マッピング情報が数字の場合は、入力CSVの値を設定する
            if map.isdigit():
                base_csv[int(map) - 1] = csv_row[i]
            # マッピング情報が文字列の場合は、標準CSVの値を設定する
            else:
                # base_csv[i] = map
                pass

        logger.debug({
            "status": "success",
            "message": "DefaultCsvReader create_date success.",
            "result": base_csv
        })
        return base_csv
