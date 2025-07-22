@classmethod
def _resp_map_logic(cls, data: bytes, length: bytes) -> tuple[dict, bytes]:
    # TODO: why is this split out
    _data = data
    _length = int(length)
    
    _map = {}
    for _ in range(_length):
        _key, _data = RESP3.parse_element(_data)
        _value, _data = RESP3.parse_element(_data)
        _map[_key] = _value
    return _map, _data
@classmethod
def parse_map(cls, data: bytes):
    if data[0].to_bytes() != b"%":
        raise ValueError(f"Expected '%' for map prefix, got {data[0]}")

    _prefix, _data = data.split(b"%", 1)
    _length, _data = _data.split(CRLF, 1)
    
    _map, _remaining = RESP3._resp_map_logic(_data, _length) 
    
    return _map, _remaining
