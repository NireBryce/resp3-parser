from olc.resp3_parser_elements import RESP3

CRLF = b"\r\n"
TYPES = [
    b"+",
    b"-",
    b":",
    b"$",
    b"*",
    b"_",
    b"#",
    b",",
    b"(",
    b"!",
    b"=",
    b"%",
    b"|",
    b"~",
    b">"
]
TEXT_ENCODING = "utf-8"

class RESP3_parser:
    @classmethod
    def parse_element(cls, data: bytes):
        match data[0].to_bytes():
            case b"+": 
                _result = RESP3.simple_string(data)
            case b"-": 
                _result = RESP3.simple_error(data)
            case b":": 
                _result = RESP3.integer(data)
            case b"$": 
                _result = RESP3.bulk_string(data)
            case b"*": 
                _result = RESP3.array(data)
            case b"_": 
                _result = RESP3.null(data)
            case b"#": 
                _result = RESP3.boolean(data)
            case b",": 
                _result = RESP3.double(data)
            case b"(": 
                _result = RESP3.bignum(data)
            case b"!": 
                _result = RESP3.bulk_error(data)
            case b"=": 
                _result = RESP3.verbatim_string(data)
            case b"%": 
                _result = RESP3.map(data)
            case b"|":
                _result = RESP3.attribute(data)
            case b"~": 
                _result = RESP3.set(data)
            # case b">": 
                # _result = parse_push(data)
            case b"":
                return print("Out of elements")
            case _:
                raise ValueError(f"Expected one of {TYPES}, got {data[0]}; input not in bytes or missing prefix?")
        return (_result)
    @classmethod
    def parse(cls, data):
        _data = data
        
        return _elements
    # @classmethod
    # def parse_simple_string(cls, data: bytes) -> tuple[str, bytes]:
    #     # +OK\r\n
    #     if data[0].to_bytes() != b"+":
    #         raise ValueError(f"Expected '+' for simple string prefix, got {data[0]}")
    #     _prefix, _str = data.split(b"+", 1)
    #     _str = _str.split(CRLF, 1)
    #     return str(_str, TEXT_ENCODING)
    
    # @classmethod
    # def parse_simple_error(cls, data:bytes) -> tuple[str, bytes]:
    #     if data[0].to_bytes() != b"-":
    #         raise ValueError(f"Expected '-' for simple error prefix, got {data[0]}")
    #     _prefix, _error = data.split(b"-", 1)
    #     _error = _error.split(CRLF, 1)
    #     return str(_error, TEXT_ENCODING)

    # @classmethod
    # def parse_integer(cls, data: bytes) -> tuple[int, bytes]:
    #     if data[0].to_bytes() != b":":
    #         raise ValueError(f"Expected ':' for integer prefix, got {data[0]}")
    #     _prefix, _int = data.split(b":", 1)
    #     _int = _int.split(CRLF, 1)
    #     # if b"-" in _int:
    #     #     _sign: int = -1
    #     #     _int = _sign * _int[1:]
    #     # elif b"+" in _int:
    #     #     _int = _int[1:]
    #     return int(_int)
    # # @classmethod
    # def parse_bulk_string(cls, data: bytes):
    #     if data[0].to_bytes() != b"$":
    #         raise ValueError(f"Expected '$' for bulk string prefix, got {data[0]}")
    #     _prefix, _string = data.split(b"$", 1)
    #     _length, _string = _string.split(CRLF, 1)
        
    #     # TODO: hack 
    #     if len(_string.split(CRLF, 1)) > 1:
    #         _string = _string.split(CRLF, 1)
    #     else:
    #         _string = _string, b""
    #     # /hack
        
        
    #     if _length == b"-1": 
    #         _string = None
    #     else:
    #         _string = _string[:int(_length)].decode()
    #     return _string
    # @classmethod
    # def parse_array(cls, data: bytes):
    #     if data[0].to_bytes() != b'*':
    #         raise ValueError(f"Expected {b'*'} for array prefix, got {data[0]}")
    #     _prefix, _data = data.split(b"*", 1)
    #     _length, _data = _data.split(CRLF, 1)
    #     _array = [] 
    #     _array_member = []
    #     if int(_length) == -1: 
    #         return [None], _data
    #     elif int(_length) == 0:
    #         return [], _data
    #     for i in range(int(_length)+1): 
    #         # TODO: this needs to be redone because it doesn't work pseudo-recursively
    #         # instead it just adds the first element of each loop
    #         if _data and _data[0].to_bytes() in TYPES:
    #             element, _data = RESP3.parse_element(_data)
    #             print(f"{element=}")
    #             _array_member.append(element) 
    #     # # TODO: also a hack
    #     # if int(_length) > 1:
    #     #     _array = _array.append([member for member in _array_member])
    #     # elif int(_length) == 1: 
        
    #     # TODO: append to array such that you only add extra lists if there are extra lists.  IE, why is this not recursing
    #     # it should be [x, y] or [[a,b], [x,y]] if given two lists, it needs to nest the lists.
        
    #    = _data
    #     print(_array)
    #     return _array
    # @classmethod
    # def parse_null(cls, data: bytes):
    #     if data[0].to_bytes() != b"_":
    #         raise ValueError(f"Expected '_' for null prefix, got {data[0]}")
    #     _prefix = data.split(b"_", 1)
    #     return None
    # @classmethod
    # def parse_boolean(cls, data:bytes):
    #     if data[0].to_bytes() != b"#":
    #         raise ValueError(f"Expected '#' for boolean prefix, got {data[0]}")
    #     _prefix, _bool = data.split(b"#", 1)
    #     _bool = _bool.split(CRLF, 1)
    #     if _bool == b"t":
    #         _result = True
    #     elif _bool == b"f":
    #         _result = False
    #     else:
    #         raise ValueError
    #     return _result
    # @classmethod
    # def parse_double(cls, data: bytes):
    #     if data[0].to_bytes() != b",":
    #         raise ValueError(f"Expected ',' for double-precision prefix, got {data[0]}")
    #     _prefix, _data = data.split(b",", 1)
    #     _data = _data.split(CRLF, 1)
    # #     return float(_data)
    # @classmethod
    # def parse_bignum(cls, data: bytes):
    #     if data[0].to_bytes() != b"(":
    #         raise ValueError(f"Expected '(' for bignum prefix, got {data[0]}")

    #     _prefix, _data = data.split(b"(", 1)
    #     _data = _data.split(CRLF, 1)
    #     return int(_data)
    # @classmethod
    # def parse_bulk_error(cls, data: bytes):
    #     if data[0].to_bytes() != b"!":
    #         raise ValueError(f"Expected '!' for bulk error prefix, got {data[0]}")

    #     _prefix, _data = data.split(b"!", 1)
    #     _length, _data = _data.split(CRLF, 1)
    #     _data = _data.split(CRLF, 1)
    #     _error = _data[:int(_length)]
    #     return str(_error, TEXT_ENCODING)
    # @classmethod
    # def parse_verbatim_string(cls, data: bytes):
    #     if data[0].to_bytes() != b"=":
    #         raise ValueError(f"Expected '=' for verbatim string prefix, got {data[0]}")

    #     _prefix, _data = data.split(b"=", 1)
    #     _length, _data = _data.split(CRLF, 1)
        
    #     _encoding, _data = _data.split(CRLF, 1)
    #     if _encoding == b"txt":
    #         _encoding = "utf-8"
    #     elif _encoding == b"mkd":
    #         _encoding = "utf-8"
    #     else: 
    #         # underspecified in spec
    #         _encoding = "bytes"
            
    #     _data = _data.split(CRLF, 1)
    #     _string = _data[:int(_length)]
    #     return str(_string, encoding=_encoding)

    # @classmethod
    # def _resp_map_logic(cls, data: bytes, length: bytes) -> tuple[dict, bytes]:
    #     # TODO: why is this split out
    #     _data = data
    #     _length = int(length)
        
    #     _map = {}
    #     for _ in range(_length):
    #         _key, _data = RESP3.parse_element(_data)
    #         _value, _data = RESP3.parse_element(_data)
    #         _map[_key] = _value
    #     return _map, _data
    # @classmethod
    # def parse_map(cls, data: bytes):
    #     if data[0].to_bytes() != b"%":
    #         raise ValueError(f"Expected '%' for map prefix, got {data[0]}")

    #     _prefix, _data = data.split(b"%", 1)
    #     _length, _data = _data.split(CRLF, 1)
        
    #     _map = RESP3._resp_map_logic(_data, _length) 
        
    #     return _map

    # @classmethod
    # def parse_attribute(cls, data: bytes):
    #     class RESP3Attribute:
    #         def __init__(self, attribs: dict, reply):
    #             self.attribs = attribs # { key: { key : value, key2: value2 } }
    #             self.reply = reply
    #         def __repr__(self):
    #             return f"RESP3Attribute({self.attribs}, {self.reply})"
            
        
    #     if data[0].to_bytes() != b"|":
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
    #    = _data
        
    #     return attrs
    # @classmethod    
    # def parse_set(cls, data: bytes):
    #     if data[0].to_bytes() != b"~":
    #         raise ValueError(f"Expected '~' for set prefix, got {data[0]}")
    #     _prefix, _data = data.split(b"~", 1)
    #     _length, _data = _data.split(CRLF, 1)
    #     _set = set()
    #     for _ in range(int(_length)):
    #         _element, _data = RESP3.parse_element(_data)
    #         _set.add(_element)
    #    = _data
    #     return _set
    # @classmethod
    # def parse_push(cls, data: bytes):
    #     if data[0].to_bytes() != b">":
    #         raise ValueError(f"Expected '>' for push prefix, got {data[0]}")
    #     _prefix, _data = data.split(b">", 1)
    #     _length, _data = _data.split(CRLF, 1)
    #     pass # handle this eventually but it wants callbacks
    
