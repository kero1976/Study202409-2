from csv_tool.csv_data_mapper import CsvDataMapper
from csv_tool.read_default_csv import DefaultCsvReader
import pytest
# @pytest.mark.shijo
# def test_create_date1(self):
#     """CSVデータの作成テスト1"""
#     reader = DefaultCsvReader("./tests/data/read_default_csv/data1.txt")
#     input_data = ["1", "山田太郎", "男"]
#     mapping = ["1", "2", "4"]
#     assert reader.create_date(input_data,
#                               mapping) == ["1", "山田太郎", "不明", "男", "未設定"]

@pytest.mark.shijo
def test_CsvDataMapper():
    reader = DefaultCsvReader("./tests/data/read_default_csv/data1.txt")
    mapper = CsvDataMapper("1,2,4", reader)
    result = mapper.create_date(["1", "山田太郎", "男"])
    assert result == ["1", "山田太郎", "不明", "男", "未設定"]