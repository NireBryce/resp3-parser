from ..util import slice_first_byte
from ..CONSTANTS import CRLF

def parse_verbatim_string(data: bytes):
    _PREFIX = b"="
    if slice_first_byte(data) != _PREFIX:
        raise ValueError(f"Expected '{_PREFIX}' for verbatim string prefix, got {data[0]}")
    prefix, data = data.split(_PREFIX, 1)
    length = int(data.split(CRLF, 1)[0])
    print(f"verbatim string, length: {length}")


# def parse_verbatim_string(data: bytes):
#     if slice_first_byte(data) != b"=":
#         raise ValueError(f"Expected '=' for verbatim string prefix, got {data[0]}")

#     _prefix, _data = data.split(b"=", 1)
#     _length, _data = _data.split(CRLF, 1)
    
#     _encoding, _data = _data.split(CRLF, 1)
#     if _encoding == b"txt":
#         _encoding = "utf-8"
#     elif _encoding == b"mkd":
#         _encoding = "utf-8"
#     else: 
#         # underspecified in spec
#         _encoding = "bytes"
        
#     _data, _remaining = _data.split(CRLF, 1)
#     _string = _data[:int(_length)]
#     return str(_string, encoding=_encoding), _remaining

# def test_verbatim_string():
#         test_strings = [
#             b"=15\r\ntxt:Some string\r\n",
#         ]
        
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == "txt:Some string"
#     test_verbatim_string()
