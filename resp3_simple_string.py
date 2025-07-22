@classmethod
def parse_simple_string(cls, data: bytes) -> tuple[str, bytes]:
    # +OK\r\n
    if data[0].to_bytes() != b"+":
        raise ValueError(f"Expected '+' for simple string prefix, got {data[0]}")
    _prefix, _str = data.split(b"+", 1)
    _str, _remaining = _str.split(CRLF, 1)
    return str(_str, TEXT_ENCODING), _remaining
