from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_bulk_string(data: bytes):
    _PREFIX = b"$"
    if slice_first_byte(data) != _PREFIX:
        raise ValueError(f"Expected '{_PREFIX}' for bulk string prefix, got {data[0]}")
    
    if data.split(CRLF)[0][1:] == b"":
        print("bulk string, Empty")
    elif data.split(CRLF)[0][1:] == b"-1":
        print("bulk string, Null")
    
    
    else:
        prefix, data = data.split(_PREFIX, 1)
        length = int(data.split(CRLF, 1)[0])
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
