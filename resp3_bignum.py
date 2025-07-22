def parse_bignum(data: bytes):
    if data[0].to_bytes() != b"(":
        raise ValueError(f"Expected '(' for bignum prefix, got {data[0]}")

    _prefix, _data = data.split(b"(", 1)
    _data, _remaining = _data.split(CRLF, 1)
    return int(_data), _remaining
