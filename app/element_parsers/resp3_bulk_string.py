from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_bulk_string(data: bytes):
    if slice_first_byte(data) != b"$":
        raise ValueError(f"Expected '$' for bulk string prefix, got {data[0]}")
    length = data.split(CRLF)[1]
    print(f"bulk string, length: {length}")


# def parse_bulk_string(data: bytes):
#     if slice_first_byte(data) != b"$":
#         raise ValueError(f"Expected '$' for bulk string prefix, got {data[0]}")
#     _prefix, _string = data.split(b"$", 1)
#     _length, _string = _string.split(CRLF, 1)
    
#     # TODO: hack 
#     if len(_string.split(CRLF, 1)) > 1:
#         _string, _remaining = _string.split(CRLF, 1)
#     else:
#         _string, _remaining = _string, b""
#     # /hack
    
    
#     if _length == b"-1": 
#         _string = None
#     else:
#         _string = _string[:int(_length)].decode()
#     return _string
