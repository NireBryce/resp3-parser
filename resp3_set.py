@classmethod    
def parse_set(cls, data: bytes):
    if data[0].to_bytes() != b"~":
        raise ValueError(f"Expected '~' for set prefix, got {data[0]}")
    _prefix, _data = data.split(b"~", 1)
    _length, _data = _data.split(CRLF, 1)
    _set = set()
    for _ in range(int(_length)):
        _element, _data = RESP3.parse_element(_data)
        _set.add(_element)
    _remaining = _data
    return _set, _remaining
