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


def read_csv_file(file_path: str) -> list[dict[str, str]]:
    """CSVファイルを読み込む関数

    
    Args:
        file_path (str): CSVファイルのパス

    Returns:
        list[dict[str, str]]: CSVファイルの内容を辞書のリストとして返す
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        content = [row for row in csvreader] 
    return content
