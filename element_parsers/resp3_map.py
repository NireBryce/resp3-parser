from ..app.CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_map(data: bytes):
    _PREFIX = b"%"
    if slice_first_byte(data) != _PREFIX:
        raise ValueError(f"Expected '{_PREFIX}' for map prefix, got {data[0]}")
    prefix, data = data.split(_PREFIX, 1)
    length = int(data.split(CRLF, 1)[0])
    print(f"map, length: {length}")
    


# def _resp_map_logic(data: bytes, length: bytes) -> tuple[dict, bytes]:
#     # TODO: why is this split out
#     _data = data
#     _length = int(length)
    
#     _map = {}
#     for _ in range(_length):
#         # TODO: fix parse_Element
#         _key, _data = parse_element(_data)
#         _value, _data = parse_element(_data)
#         _map[_key] = _value
#     return _map, _data
# def parse_map(data: bytes):
#     if slice_first_byte(data) != b"%":
#         raise ValueError(f"Expected '%' for map prefix, got {data[0]}")

#     _prefix, _data = data.split(b"%", 1)
#     _length, _data = _data.split(CRLF, 1)
    
#     _map, _remaining = _resp_map_logic(_data, _length) 
    
#     return _map, _remaining

# def test_map():
#         test_strings = [
#             b"%2\r\na:1\r\nb:2\r\n",
#             b"%2\r\n+first\r\n:1\r\n+second\r\n:2\r\n"
#         ]
        
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == {"a": 1, "b": 2}
#     test_map()
