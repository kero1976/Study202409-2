import pytest
from convert_tools.bytes_number import bytes_to_int

def test_bytes_to_int_big_endian_unsigned():
    """符号なし、ビッグエンディアンのテスト"""
    byte_array = b'\x00\x01'
    result = bytes_to_int(byte_array, byteorder='big', signed=False)
    assert result == 1

def test_bytes_to_int_little_endian_unsigned():
    """符号なし、リトルエンディアンのテスト"""
    byte_array = b'\x01\x00'
    result = bytes_to_int(byte_array, byteorder='little', signed=False)
    assert result == 1

def test_bytes_to_int_big_endian_signed():
    """符号付き、ビッグエンディアンのテスト"""
    byte_array = b'\xff\xff'
    result = bytes_to_int(byte_array, byteorder='big', signed=True)
    assert result == -1

def test_bytes_to_int_little_endian_signed():
    """符号付き、リトルエンディアンのテスト"""
    byte_array = b'\xff\xff'
    result = bytes_to_int(byte_array, byteorder='little', signed=True)
    assert result == -1

def test_bytes_to_int_empty_array():
    """空のバイト配列のテスト"""
    byte_array = b''
    result = bytes_to_int(byte_array, byteorder='big', signed=False)
    assert result == 0