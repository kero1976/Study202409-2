from csvtool2.filereader.filereader import (file_exist, read_csv_with_unknown_encoding)


def test_file_exist_ok():
    file = r"C:\WORK\test1.txt"
    assert file_exist(file) is True


def test_file_exist_ng():
    file = r"C:\WORK\test2.txt"
    assert file_exist(file) is False


def test_file_exist_ng_filename():
    file = r"data\01HOKKAI.CSV"
    assert file_exist(file) is True


def test_read_csv_with_unknown_encoding():
    file = r"data\01HOKKAI.CSV"
    assert read_csv_with_unknown_encoding(file) is not None
