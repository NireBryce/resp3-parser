from ..util import slice_first_byte
def parse_attribute(data: bytes):
    class RESP3Attribute:
        def __init__(self, attribs: dict, reply):
            self.attribs = attribs # { key: { key : value, key2: value2 } }
            self.reply = reply
        def __repr__(self):
            return f"RESP3Attribute({self.attribs}, {self.reply})"
        
    
    if slice_first_byte(data) != b"|":
        raise ValueError(f"Expected '|' for attribute prefix, got {data[0]}")

    _prefix, _data = data.split(b"|", 1)
    _length, _data = _data.split(CRLF, 1)
    _attr_name = ""
    _attr_map = {}
    for _ in range(int(_length)):
        _attr_name, _data = RESP3.parse_element(_data)
        _attr_map[_attr_name], _data = RESP3.parse_element(_data)
        
        
    _result, _data = RESP3.parse_element(_data)
    
    attrs = RESP3Attribute(_attr_map, _result)
    _remaining = _data
    
    return attrs, _remaining
