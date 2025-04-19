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
        self.mapping = None

    def create_mapping(self) -> list[int]:
        """マッピング情報をリストに変換する

        Returns:
            list[int]: マッピング情報をリストに変換したもの
        """
        logger.debug({
            "status": "start  ",
            "message": "CsvDataMapper create_mapping start.",
            "params": {
                "mapping_info": self.mapping_info
            }
        })
        if self.mapping is not None:
            logger.debug({
                "status": "success",
                "message": "CsvDataMapper create_mapping cashed.",
                "result": self.mapping
            })
            return self.mapping

        mapping = self.mapping_info.split(",")
        # 数字以外の文字列はスキップする
        mapping = [int(map) for map in mapping if map.isdigit()]
        logger.debug({
            "status": "success",
            "message": "CsvDataMapper create_mapping success.",
            "result": mapping
        })
        return mapping

    def create_date(self, csv_row: list[str]) -> list[str]:
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
                "csv_row": csv_row
            }
        })
        base_csv = self.default_csv.read()
        mapping = self.create_mapping()
        # forループでカウントを取得
        for i, map in enumerate(mapping):
            # マッピング情報が空の場合はスキップ
            base_csv[map - 1] = csv_row[i]

        logger.debug({
            "status": "success",
            "message": "DefaultCsvReader create_date success.",
            "result": base_csv
        })
        return base_csv
