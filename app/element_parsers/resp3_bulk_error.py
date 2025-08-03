from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_bulk_error(data: bytes):
    _PREFIX = b"!"
    if slice_first_byte(data) != _PREFIX:
        raise ValueError(f"Expected '{_PREFIX}' for bulk error prefix, got {data[0]}")
    prefix, data = data.split(_PREFIX, 1)
    length = int(data.split(CRLF, 1)[0])
    print(f"bulk error, length: {length}")




# def parse_bulk_error(data: bytes):
#     if slice_first_byte(data) != b"!":
#         raise ValueError(f"Expected '!' for bulk error prefix, got {data[0]}")

#     _prefix, _data = data.split(b"!", 1)
#     _length, _data = _data.split(CRLF, 1)
#     _data, _remaining = _data.split(CRLF, 1)
#     _error = _data[:int(_length)]
#     return str(_error, TEXT_ENCODING)

# def test_bulk_error():
#         test_strings = [
#             b"!21\r\nSYNTAX invalid syntax\r\n",
#         ]
        
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == "SYNTAX invalid syntax"
#     test_bulk_error()
