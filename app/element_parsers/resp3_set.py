from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_set(data: bytes):
    if slice_first_byte(data) != b"~":
        raise ValueError(f"Expected '~' for set prefix, got {data[0]}")
    # _prefix, _data = data.split(b"~", 1)
    # _length, _data = _data.split(CRLF, 1)
    length = data.split(CRLF)[1]
    
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
