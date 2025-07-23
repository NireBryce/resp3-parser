from ..util import slice_first_byte
def parse_verbatim_string(data: bytes):
    if slice_first_byte(data) != b"=":
        raise ValueError(f"Expected '=' for verbatim string prefix, got {data[0]}")

    _prefix, _data = data.split(b"=", 1)
    _length, _data = _data.split(CRLF, 1)
    
    _encoding, _data = _data.split(CRLF, 1)
    if _encoding == b"txt":
        _encoding = "utf-8"
    elif _encoding == b"mkd":
        _encoding = "utf-8"
    else: 
        # underspecified in spec
        _encoding = "bytes"
        
    _data, _remaining = _data.split(CRLF, 1)
    _string = _data[:int(_length)]
    return str(_string, encoding=_encoding), _remaining
