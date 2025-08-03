from ..app.CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_set(data: bytes):
    _PREFIX = b"~"
    if slice_first_byte(data) != _PREFIX:
        raise ValueError(f"Expected '{_PREFIX}' for set prefix, got {data[0]}")
    prefix, data = data.split(_PREFIX, 1)
    length = int(data.split(CRLF, 1)[0])
    
    print(f"set, length: {length}")


        
# def parse_set(data: bytes):
#     if slice_first_byte(data) != b"~":
#         raise ValueError(f"Expected '~' for set prefix, got {data[0]}")
#     _prefix, _data = data.split(b"~", 1)
#     _length, _data = _data.split(CRLF, 1)
#     _set = set()
#     for _ in range(int(_length)):
#         _element, _data = parse_element(_data)
#         _set.add(_element)
#     _remaining = _data
#     return _set, _remaining

# def test_set():
#         test_strings = [
#             b"~7\r\n:1\r\n:2\r\n:3\r\n:4\r\n:5\r\n:6\r\n",
#         ]        
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == {1, 2, 3, 4, 5, 6}
#     test_set()
