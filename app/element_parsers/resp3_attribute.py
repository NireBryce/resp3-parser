from ..util import slice_first_byte
from ..CONSTANTS import CRLF
def parse_attribute(data: bytes):
    if slice_first_byte(data) != b"|":
        raise ValueError(f"Expected '|' for attribute prefix, got {data[0]}")
    length = data.split(CRLF)[1]
    print(f"attribute, length: {length}")




# def parse_attribute(data: bytes):
#     class RESP3Attribute:
#         def __init__(self, attribs: dict, reply):
#             self.attribs = attribs # { key: { key : value, key2: value2 } }
#             self.reply = reply
#         def __repr__(self):
#             return f"RESP3Attribute({self.attribs}, {self.reply})"
        
    
#     if slice_first_byte(data) != b"|":
#         raise ValueError(f"Expected '|' for attribute prefix, got {data[0]}")

#     _prefix, _data = data.split(b"|", 1)
#     _length, _data = _data.split(CRLF, 1)
#     _attr_name = ""
#     _attr_map = {}
#     for _ in range(int(_length)):
#         _attr_name, _data = RESP3.parse_element(_data)
#         _attr_map[_attr_name], _data = RESP3.parse_element(_data)
        
        
#     _result, _data = RESP3.parse_element(_data)
    
#     attrs = RESP3Attribute(_attr_map, _result)
#     _remaining = _data
    
#     return attrs, _remaining

# def test_attribute():
#         test_strings = [
#             b"|1\r\n+key-popularity\r\n%2\r\n$1\r\na\r\n,0.1923\r\n$1\r\nb\r\n,0.0012\r\n*2\r\n:2039123\r\n:9543892\r\n",
#         ]
        
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result.attribs == {"key-popularity": {"a": 0.1923, "b": 0.0012}}
#         assert result.reply == [2039123, 9543892]
#     test_attribute()
