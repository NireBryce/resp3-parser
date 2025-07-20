CRLF = b"\r\n"

def parse(self): 
        pass

def parse_simple_string(data: bytes) -> str:
    # +OK\r\n
    _prefix, _str = data.split(b"+", 1)
    _str, _suffix = _str.split(CRLF, 1)
    return str(_str)
    
def parse_simple_error(data:bytes) -> str:
    _prefix, _error = data.split(b"-", 1)
    _error, _suffix = _error.split(CRLF, 1)
    return str(_error)

def parse_integer(data: bytes) -> int:
    _prefix, _int = data.split(b":", 1)
    _int, _suffix = _int.split(CRLF, 1)
    # if b"-" in _int:
    #     _sign: int = -1
    #     _int = _sign * _int[1:]
    # elif b"+" in _int:
    #     _int = _int[1:]
    return int(_int)

def parse_bulk_string(data: bytes) -> bytes | None:
    _prefix, _string = data.split(b"$", 1)
    _length, _string = _string.split(CRLF, 1)
    if _length == b"-1": 
        return None
    _string = _string[:int(_length)]
    return _string

def parse_array(data: bytes) -> list | None:
    _prefix, _array = data.split(b"*", 1)
    _length, _array = _array.split(CRLF, 1)
    if _length == b"0": 
        return []
    if _length == b"-1": 
        return None
    
    _array = [ parse(member) 
               for member 
               in _array.split(CRLF)[:int(_length)]
            ]
    return _array

def parse_null(data: bytes) -> None:
    _prefix, _ = data.split(b"_", 1)
    return None

def parse_boolean(data:bytes) -> bool:
    _prefix, _bool = data.split(b"#", 1)
    _bool, _suffix = _bool.split(CRLF, 1)
    if _bool == b"t":
        return True
    elif _bool == b"f":
        return False
    else:
        raise ValueError

def parse_double(data: bytes) -> float:
    _prefix, _data = data.split(b",", 1)
    _data, _suffix = _data.split(CRLF, 1)
    return float(_data)

def parse_bignum(data: bytes) -> int:
    _prefix, _data = data.split(b"(", 1)
    _data, _suffix = _data.split(CRLF, 1)
    return int(_data)

def parse_bulk_error(data: bytes) -> str:
    _prefix, _data = data.split(b"!", 1)
    _length, _data = _data.split(CRLF, 1)
    _data, _suffix = _data.split(CRLF, 1)
    _error = _data[:int(_length)]
    return str(_data)

def parse_verbatim_string(data: bytes) -> str:
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

def parse_map(data: bytes) -> dict:
    
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
