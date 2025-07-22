def parse_boolean(cls, data:bytes):
        if data[0].to_bytes() != b"#":
            raise ValueError(f"Expected '#' for boolean prefix, got {data[0]}")
        _prefix, _bool = data.split(b"#", 1)
        _bool, _remaining = _bool.split(CRLF, 1)
        if _bool == b"t":
            _result = True
        elif _bool == b"f":
            _result = False
        else:
            raise ValueError
        return _result, _remaining
