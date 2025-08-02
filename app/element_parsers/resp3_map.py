from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_map(data: bytes):
    if slice_first_byte(data) != b"%":
        raise ValueError(f"Expected '%' for map prefix, got {data[0]}")
    length = data.split(CRLF)[1]
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
