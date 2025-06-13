def bytes_to_int(byte_array: bytes, byteorder: str = 'big', signed: bool = False) -> int:
    """バイト配列を数値に変換するメソッド

    Args:
        byte_array (bytes): 変換するバイト配列
        byteorder (str): バイトオーダー ('big' または 'little')
        signed (bool): 符号付きかどうか

    Returns:
        int: 変換された数値
    """
    return int.from_bytes(byte_array, byteorder=byteorder, signed=signed)

