def parse_double(cls, data: bytes):
    if data[0].to_bytes() != b",":
        raise ValueError(f"Expected ',' for double-precision prefix, got {data[0]}")
    _prefix, _data = data.split(b",", 1)
    _data, _remaining = _data.split(CRLF, 1)
    return float(_data), _remaining
