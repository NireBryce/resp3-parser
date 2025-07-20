from ctypes.util import test
from errno import EILSEQ


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

def parse_element(data): 
    if data[0] in TYPES:
        _prefix = data[0]
        return dispatch_table[_prefix](data)
    else:
        raise ValueError(f"Expected one of {TYPES}, got {data[0]}; input not in bytes or missing prefix?")
    

def parse_simple_string(data: bytes) -> tuple[str, bytes]:
    # +OK\r\n
    if data[0] != b"+":
        raise ValueError(f"Expected '+' for simple string prefix, got {data[0]}")
    _prefix, _str = data.split(b"+", 1)
    _str, _suffix = _str.split(CRLF, 1)
    return str(_str), _suffix
    
def parse_simple_error(data:bytes) -> tuple[str, bytes]:
    if data[0] != b"-":
        raise ValueError(f"Expected '-' for simple error prefix, got {data[0]}")
    _prefix, _error = data.split(b"-", 1)
    _error, _suffix = _error.split(CRLF, 1)
    return str(_error), _suffix

def parse_integer(data: bytes) -> tuple[int, bytes]:
    if data[0] != b":":
        raise ValueError(f"Expected ':' for integer prefix, got {data[0]}")
    _prefix, _int = data.split(b":", 1)
    _int, _suffix = _int.split(CRLF, 1)
    # if b"-" in _int:
    #     _sign: int = -1
    #     _int = _sign * _int[1:]
    # elif b"+" in _int:
    #     _int = _int[1:]
    return int(_int), _suffix

def parse_bulk_string(data: bytes):
    if data[0] != b"$":
        raise ValueError(f"Expected '$' for bulk string prefix, got {data[0]}")
    _prefix, _string = data.split(b"$", 1)
    _length, _string = _string.split(CRLF, 1)
    _string, _suffix = _string.split(CRLF, 1)
    if _length == b"-1": 
        return None
    _string = _string[:int(_length)]
    return _string, _suffix

def parse_array(data: bytes):
    if data[0] != b"*":
        raise ValueError(f"Expected '*' for array prefix, got {data[0]}")
    _prefix, _data = data.split(b"*", 1)
    _length, _data = _data.split(CRLF, 1)
    if _length == b"0": 
        return []
    if _length == b"-1": 
        return None
    
    _array = []
    for i in range(int(_length)): 
        if _data[0] in TYPES:
            element, _data = parse_element(_data)
            _array.append(element)
        else:
            raise IndexError(f"no prefix at index {i}")
        
    _suffix = _data
    return _array, _suffix

def parse_null(data: bytes) -> None:
    if data[0] != b"_":
        raise ValueError(f"Expected '_' for null prefix, got {data[0]}")
    _prefix, _ = data.split(b"_", 1)
    return None

def parse_boolean(data:bytes) -> bool:
    if data[0] != b"#":
        raise ValueError(f"Expected '#' for boolean prefix, got {data[0]}")
    _prefix, _bool = data.split(b"#", 1)
    _bool, _suffix = _bool.split(CRLF, 1)
    if _bool == b"t":
        return True
    elif _bool == b"f":
        return False
    else:
        raise ValueError

def parse_double(data: bytes) -> float:
    if data[0] != b",":
        raise ValueError(f"Expected ',' for double-precision prefix, got {data[0]}")
    _prefix, _data = data.split(b",", 1)
    _data, _suffix = _data.split(CRLF, 1)
    return float(_data)

def parse_bignum(data: bytes) -> int:
    if data[0] != b"(":
        raise ValueError(f"Expected '(' for bignum prefix, got {data[0]}")

    _prefix, _data = data.split(b"(", 1)
    _data, _suffix = _data.split(CRLF, 1)
    return int(_data)

def parse_bulk_error(data: bytes) -> str:
    if data[0] != b"!":
        raise ValueError(f"Expected '!' for bulk error prefix, got {data[0]}")

    _prefix, _data = data.split(b"!", 1)
    _length, _data = _data.split(CRLF, 1)
    _data, _suffix = _data.split(CRLF, 1)
    _error = _data[:int(_length)]
    return str(_data)

def parse_verbatim_string(data: bytes) -> str:
    if data[0] != b"=":
        raise ValueError(f"Expected '=' for verbatim string prefix, got {data[0]}")

    _prefix, _data = data.split(b"=", 1)
    _length, _data = _data.split(CRLF, 1)
    
    _encoding, _data = _data.split(CRLF, 1)
    if _encoding == b"txt":
        _encoding = "utf-8"
    elif _encoding == b"mkd":
        _encoding = "utf-8"
    else: 
        # underspecified in spec
        _encoding = "bytes"
        
    _data, _suffix = _data.split(CRLF, 1)
    _string = _data[:int(_length)]
    return str(_string, encoding=_encoding)

def _resp_map_logic(data: bytes, length: bytes) -> tuple[dict, bytes]:
    _data = data
    _length = int(length)
    
    _map = {}
    for _ in range(_length):
        _key, _data = parse_element(_data)
        _value, _data = parse_element(_data)
        _map[_key] = _value
    return _map, _data
def parse_map(data: bytes):
    if data[0] != b"%":
        raise ValueError(f"Expected '%' for map prefix, got {data[0]}")

    _prefix, _data = data.split(b"%", 1)
    _length, _data = _data.split(CRLF, 1)
    
    _map, _suffix = _resp_map_logic(_data, _length)
    
    return _map, _suffix

def parse_attribute(data: bytes):
    class RESP3Attribute:
        def __init__(self, name, attribs, reply):
            self.dict = {}
            self.dict[name] = attribs
            self.reply = reply
        def __repr__(self):
            return f"RESP3Attribute({self.dict}, {self.reply})"
        
    
    if data[0] != b"|":
        raise ValueError(f"Expected '|' for attribute prefix, got {data[0]}")

    _prefix, _data = data.split(b"|", 1)
    _length, _data = _data.split(CRLF, 1)
    
    for i in range(int(_length)):
        _attr_name, _data = parse_element(_data)
        _attr_map, _data = parse_element(_data)
        
    _result, _data = parse_element(_data)
    attrs = RESP3Attribute(_attr_name, _attr_map, _result)
    _suffix = _data
    
    return attrs, _suffix
    
    
    # _attr_map_blob, _remaining_data = _data.split(CRLF, int(_length) + 1)
    # _attr_map = _resp_map_logic(_attr_map_blob, _length)
    
    return _attr_name, _attr_map, _suffix
        
dispatch_table = {
    b"+": parse_simple_string,
    b"-": parse_simple_error,
    b":": parse_integer,
    b"$": parse_bulk_string,
    b"*": parse_array,
    b"_": parse_null,
    b"#": parse_boolean,
    b",": parse_double,
    b"(": parse_bignum,
    b"!": parse_bulk_error,
    b"=": parse_verbatim_string,
    b"%": parse_map,
    b"|": parse_attribute,
    b"~": parse_set,
    b">": parse_push
}
class Resp3Message:
    def __init__(self, message):
        self.message: bytes = message
        self.splits = message.split(CRLF)
        self.chunk = None
        self.position = 0
    def step(self):
        self.chunk = self.splits[self.position]
        self.parse(self.chunk)
        self.position += 1
    def parse(self, chunk):
        pass


if __name__ == "__main__":
    def test_arrays():
        # simple array
        test1 = b"*2\r\n+hello\r\n:42\r\n"
        result, _ = parse_array(test1)
        print(f"Test 1: {result}, correct: ['hello', 42]")  

        # Empty array
        test2 = "*0\r\n"
        result, _ = parse_array(test2)
        print(f"Test 2: {result}")  # []
        
        # Nested array
        test3 = "*2\r\n+outer\r\n*2\r\n+inner1\r\n+inner2\r\n"
        result, _ = parse_array(test3)
        print(f"Test 3: {result}")  # ['outer', ['inner1', 'inner2']]
        
        # Mixed types
        test4 = "*3\r\n+string\r\n:123\r\n$5\r\nworld\r\n"
        result, _ = parse_array(test4)
        print(f"Test 4: {result}")  # ['string', 123, 'world']
    
    test_arrays()
