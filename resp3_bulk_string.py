@classmethod
def parse_bulk_string(cls, data: bytes):
    if data[0].to_bytes() != b"$":
        raise ValueError(f"Expected '$' for bulk string prefix, got {data[0]}")
    _prefix, _string = data.split(b"$", 1)
    _length, _string = _string.split(CRLF, 1)
    
    # TODO: hack 
    if len(_string.split(CRLF, 1)) > 1:
        _string, _remaining = _string.split(CRLF, 1)
    else:
        _string, _remaining = _string, b""
    # /hack
    
    
    if _length == b"-1": 
        _string = None
    else:
        _string = _string[:int(_length)].decode()
    return _string, _remaining
