def parse_bulk_error(cls, data: bytes):
    if data[0].to_bytes() != b"!":
        raise ValueError(f"Expected '!' for bulk error prefix, got {data[0]}")

    _prefix, _data = data.split(b"!", 1)
    _length, _data = _data.split(CRLF, 1)
    _data, _remaining = _data.split(CRLF, 1)
    _error = _data[:int(_length)]
    return str(_error, TEXT_ENCODING), _remaining
