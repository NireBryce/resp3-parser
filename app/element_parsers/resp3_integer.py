from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_integer(data: bytes):
    if slice_first_byte(data) != b":":
        raise ValueError(f"Expected ':' for integer prefix, got {data[0]}")
    length = data.split(CRLF)[1]
    print(f"integer, length: {length}")

def test_integer():
    _tests = [
        (b":0\r\n", 0),
        (b":1000\r\n", 1000)
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        result = parse_integer(test[0])
        print(f'integer, {result=}')
        
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


# def test_integer():
#         test_strings = [
#             b":0\r\n",
#             b":1000\r\n"
#         ]
#         result, _ = RESP3.parse_element(test_strings.pop(0)) 
#         assert result == (0)
#         result, _ = RESP3.parse_element(test_strings.pop(0)) 
#         assert result == (1000)
#     test_integer()
