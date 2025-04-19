"""read_default_csv.pyファイルのテスト"""
import pytest
from csv_tool.read_default_csv import read_csv_file
from csv_tool.read_default_csv import DefaultCsvReader

class TestReadCsvFile:
    """read_csv_file関数のテストクラス"""

    def test_data1(self):
        """CSVファイルの読み込みテスト1
        列数は1行数は5のCSVファイルを読み込む。
        """
        result = read_csv_file("./tests/data/read_default_csv/data1.txt")
        assert len(result) == 5
        assert result[0] == [""]
        assert result[1] == [""]
        assert result[2] == ["不明"]
        assert result[3] == [""]
        assert result[4] == ["未設定"]

    def test_data2(self):
        """CSVファイルの読み込みテスト2
        列数は2行数は5のCSVファイルを読み込む。
        """
        result = read_csv_file("./tests/data/read_default_csv/data2.txt")
        assert len(result) == 5
        assert result[0] == ["ID", ""]
        assert result[1] == ["名前", ""]
        assert result[2] == ["住所", "不明"]
        assert result[3] == ["性別", ""]
        assert result[4] == ["オプション情報", "未設定"]

    def test_data_nofile(self):
        """存在しないCSVファイルの読み込みテスト"""
        result = read_csv_file(
            "./tests/data/read_default_csv/data_no_file.txt")
        assert result is None


class TestDefaultCsvReader:

    def test_data1(self):
        """CSVファイルの読み込みテスト1
        列数は1行数は5のCSVファイルを読み込む。
        """
        reader = DefaultCsvReader("./tests/data/read_default_csv/data1.txt")
        assert reader.read() == ["", "", "不明", "", "未設定"]

    def test_data2(self):
        """CSVファイルの読み込みテスト2
        列数は2行数は5のCSVファイルを読み込む。
        """
        reader = DefaultCsvReader("./tests/data/read_default_csv/data2.txt")
        assert reader.read() == ["", "", "不明", "", "未設定"]

    def test_data_nofile(self):
        """存在しないCSVファイルの読み込みテスト"""
        reader = DefaultCsvReader(
            "./tests/data/read_default_csv/data_no_file.txt")
        assert reader.read() is None


