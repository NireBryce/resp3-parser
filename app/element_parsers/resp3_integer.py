from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_integer(data: bytes):
    if slice_first_byte(data) != b":":
        raise ValueError(f"Expected ':' for integer prefix, got {data[0]}")
    length = data.split(CRLF)[1]
    print(f"integer, length: {length}")


# def parse_integer(data: bytes):
#     if slice_first_byte(data) != b":":
#         raise ValueError(f"Expected ':' for integer prefix, got {data[0]}")
#     _prefix, _int = data.split(b":", 1)
#     _int, _remaining = _int.split(CRLF, 1)
#     # if b"-" in _int:
#     #     _sign: int = -1
#     #     _int = _sign * _int[1:]
#     # elif b"+" in _int:
#     #     _int = _int[1:]
#     return int(_int)
