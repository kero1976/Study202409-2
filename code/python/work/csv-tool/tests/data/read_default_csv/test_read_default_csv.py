from csv_tool.read_default_csv import read_csv_file
import pytest


def test1():
    assert 1 == 1
    result = read_csv_file("./tests/data/read_default_csv/data1.txt")
    assert len(result) == 5
