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


# def test_bulk_string():
#         test_strings = [
#             b"$5\r\nhello\r\n",
#             b"$0\r\n\r\n", # empty
#             b"$-1\r\n", # null
#         ]
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == "hello"
        
#         # empty
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == ""
        
#         #null
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result is None
        
#     test_bulk_string()
