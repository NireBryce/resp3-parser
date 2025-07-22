
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

class RESP3:
    @classmethod
    def parse_element(cls, data: bytes):
        match data[0].to_bytes():
            case b"+": 
                _result, _remaining = RESP3.parse_simple_string(data)
            case b"-": 
                _result, _remaining = RESP3.parse_simple_error(data)
            case b":": 
                _result, _remaining = RESP3.parse_integer(data)
            case b"$": 
                _result, _remaining = RESP3.parse_bulk_string(data)
            case b"*": 
                _result, _remaining = RESP3.parse_array(data)
            case b"_": 
                _result, _remaining = RESP3.parse_null(data)
            case b"#": 
                _result, _remaining = RESP3.parse_boolean(data)
            case b",": 
                _result, _remaining = RESP3.parse_double(data)
            case b"(": 
                _result, _remaining = RESP3.parse_bignum(data)
            case b"!": 
                _result, _remaining = RESP3.parse_bulk_error(data)
            case b"=": 
                _result, _remaining = RESP3.parse_verbatim_string(data)
            case b"%": 
                _result, _remaining = RESP3.parse_map(data)
            case b"|": 
                _result, _remaining = RESP3.parse_attribute(data)
            case b"~": 
                _result, _remaining = RESP3.parse_set(data)
            # case b">": 
                # _result, _remaining = parse_push(data)
            case b"":
                return print("Out of elements")
            case _:
                raise ValueError(f"Expected one of {TYPES}, got {data[0]}; input not in bytes or missing prefix?")
        return (_result, _remaining)
    @classmethod
    def parse(cls, data):
        _data = data
        _elements = []
        while _data:
            _element, _data = RESP3.parse_element(_data)
            _elements.append(_element)
        return _elements
    @classmethod
    def parse_simple_string(cls, data: bytes) -> tuple[str, bytes]:
        # +OK\r\n
        if data[0].to_bytes() != b"+":
            raise ValueError(f"Expected '+' for simple string prefix, got {data[0]}")
        _prefix, _str = data.split(b"+", 1)
        _str, _remaining = _str.split(CRLF, 1)
        return str(_str, TEXT_ENCODING), _remaining
    
    @classmethod
    def parse_simple_error(cls, data:bytes) -> tuple[str, bytes]:
        if data[0].to_bytes() != b"-":
            raise ValueError(f"Expected '-' for simple error prefix, got {data[0]}")
        _prefix, _error = data.split(b"-", 1)
        _error, _remaining = _error.split(CRLF, 1)
        return str(_error, TEXT_ENCODING), _remaining

    @classmethod
    def parse_integer(cls, data: bytes) -> tuple[int, bytes]:
        if data[0].to_bytes() != b":":
            raise ValueError(f"Expected ':' for integer prefix, got {data[0]}")
        _prefix, _int = data.split(b":", 1)
        _int, _remaining = _int.split(CRLF, 1)
        # if b"-" in _int:
        #     _sign: int = -1
        #     _int = _sign * _int[1:]
        # elif b"+" in _int:
        #     _int = _int[1:]
        return int(_int), _remaining
    @classmethod
    def parse_bulk_string(cls, data: bytes):
        if data[0].to_bytes() != b"$":
            raise ValueError(f"Expected '$' for bulk string prefix, got {data[0]}")
        _prefix, _string = data.split(b"$", 1)
        _length, _string = _string.split(CRLF, 1)
        
        # TODO: hack 
        if len(_string.split(CRLF, 1)) > 1:
            _string, _remaining = _string.split(CRLF, 1)
        else:
            _string, _remaining = _string, b""
        # /hack
        
        
        if _length == b"-1": 
            _string = None
        else:
            _string = _string[:int(_length)].decode()
        return _string, _remaining
    @classmethod
    def parse_array(cls, data: bytes):
        if data[0].to_bytes() != b'*':
            raise ValueError(f"Expected {b'*'} for array prefix, got {data[0]}")
        _prefix, _data = data.split(b"*", 1)
        _length, _data = _data.split(CRLF, 1)
        _array = [] 
        _array_member = []
        if int(_length) == -1: 
            return [None], _data
        elif int(_length) == 0:
            return [], _data
        for i in range(int(_length)+1): 
            # TODO: this needs to be redone because it doesn't work pseudo-recursively
            # instead it just adds the first element of each loop
            if _data and _data[0].to_bytes() in TYPES:
                element, _data = RESP3.parse_element(_data)
                print(f"{element=}")
                _array_member.append(element) 
        # # TODO: also a hack
        # if int(_length) > 1:
        #     _array = _array.append([member for member in _array_member])
        # elif int(_length) == 1: 
        
        # TODO: append to array such that you only add extra lists if there are extra lists.  IE, why is this not recursing
        # it should be [x, y] or [[a,b], [x,y]] if given two lists, it needs to nest the lists.
        
        _remaining = _data
        print(_array, _remaining)
        return _array, _remaining
    @classmethod
    def parse_null(cls, data: bytes):
        if data[0].to_bytes() != b"_":
            raise ValueError(f"Expected '_' for null prefix, got {data[0]}")
        _prefix, _remaining = data.split(b"_", 1)
        return None, _remaining
    @classmethod
    def parse_boolean(cls, data:bytes):
        if data[0].to_bytes() != b"#":
            raise ValueError(f"Expected '#' for boolean prefix, got {data[0]}")
        _prefix, _bool = data.split(b"#", 1)
        _bool, _remaining = _bool.split(CRLF, 1)
        if _bool == b"t":
            _result = True
        elif _bool == b"f":
            _result = False
        else:
            raise ValueError
        return _result, _remaining
    @classmethod
    def parse_double(cls, data: bytes):
        if data[0].to_bytes() != b",":
            raise ValueError(f"Expected ',' for double-precision prefix, got {data[0]}")
        _prefix, _data = data.split(b",", 1)
        _data, _remaining = _data.split(CRLF, 1)
        return float(_data), _remaining
    @classmethod
    def parse_bignum(cls, data: bytes):
        if data[0].to_bytes() != b"(":
            raise ValueError(f"Expected '(' for bignum prefix, got {data[0]}")

        _prefix, _data = data.split(b"(", 1)
        _data, _remaining = _data.split(CRLF, 1)
        return int(_data), _remaining
    @classmethod
    def parse_bulk_error(cls, data: bytes):
        if data[0].to_bytes() != b"!":
            raise ValueError(f"Expected '!' for bulk error prefix, got {data[0]}")

        _prefix, _data = data.split(b"!", 1)
        _length, _data = _data.split(CRLF, 1)
        _data, _remaining = _data.split(CRLF, 1)
        _error = _data[:int(_length)]
        return str(_error, TEXT_ENCODING), _remaining
    @classmethod
    def parse_verbatim_string(cls, data: bytes):
        if data[0].to_bytes() != b"=":
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
            
        _data, _remaining = _data.split(CRLF, 1)
        _string = _data[:int(_length)]
        return str(_string, encoding=_encoding), _remaining

    @classmethod
    def _resp_map_logic(cls, data: bytes, length: bytes) -> tuple[dict, bytes]:
        # TODO: why is this split out
        _data = data
        _length = int(length)
        
        _map = {}
        for _ in range(_length):
            _key, _data = RESP3.parse_element(_data)
            _value, _data = RESP3.parse_element(_data)
            _map[_key] = _value
        return _map, _data
    @classmethod
    def parse_map(cls, data: bytes):
        if data[0].to_bytes() != b"%":
            raise ValueError(f"Expected '%' for map prefix, got {data[0]}")

        _prefix, _data = data.split(b"%", 1)
        _length, _data = _data.split(CRLF, 1)
        
        _map, _remaining = RESP3._resp_map_logic(_data, _length) 
        
        return _map, _remaining

    @classmethod
    def parse_attribute(cls, data: bytes):
        class RESP3Attribute:
            def __init__(self, attribs: dict, reply):
                self.attribs = attribs # { key: { key : value, key2: value2 } }
                self.reply = reply
            def __repr__(self):
                return f"RESP3Attribute({self.attribs}, {self.reply})"
            
        
        if data[0].to_bytes() != b"|":
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
    @classmethod    
    def parse_set(cls, data: bytes):
        if data[0].to_bytes() != b"~":
            raise ValueError(f"Expected '~' for set prefix, got {data[0]}")
        _prefix, _data = data.split(b"~", 1)
        _length, _data = _data.split(CRLF, 1)
        _set = set()
        for _ in range(int(_length)):
            _element, _data = RESP3.parse_element(_data)
            _set.add(_element)
        _remaining = _data
        return _set, _remaining
    @classmethod
    def parse_push(cls, data: bytes):
        if data[0].to_bytes() != b">":
            raise ValueError(f"Expected '>' for push prefix, got {data[0]}")
        _prefix, _data = data.split(b">", 1)
        _length, _data = _data.split(CRLF, 1)
        pass # handle this eventually but it wants callbacks
    
def main():
    pass
    

if __name__ == "__main__":
    
    def test_simple_string():
        test_string = b"+OK\r\n"
        result, _ = RESP3.parse_element(test_string)
        print(result)
        assert result == ("OK")
    test_simple_string()
    
    def test_simple_error():
        test_string = b"-Error message\r\n"
        result, _ = RESP3.parse_element(test_string)
        assert result == ("Error message")
        
        test_string = b"-ERR unknown command 'asdf'\r\n"
        result, _ = RESP3.parse_element(test_string)
        assert result == ("ERR unknown command 'asdf'")
        
        test_string = b"-WRONGTYPE Operation against a key holding the wrong kind of value\r\n"
        result, _ = RESP3.parse_element(test_string)
        assert result == ("WRONGTYPE Operation against a key holding the wrong kind of value")
    test_simple_error()

    def test_integer():
        test_strings = [
            b":0\r\n",
            b":1000\r\n"
        ]
        result, _ = RESP3.parse_element(test_strings.pop(0)) 
        assert result == (0)
        result, _ = RESP3.parse_element(test_strings.pop(0)) 
        assert result == (1000)
    test_integer()
    
    def test_bulk_string():
        test_strings = [
            b"$5\r\nhello\r\n",
            b"$0\r\n\r\n", # empty
            b"$-1\r\n", # null
        ]
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == "hello"
        
        # empty
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == ""
        
        #null
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result is None
        
    test_bulk_string()
    
    
    def test_arrays():
        # simple array
        test1 = b"*2\r\n+hello\r\n:42\r\n"
        result, _ = RESP3.parse_array(test1)
        assert result == ["hello", 42] 

        # Empty array
        test2 = b"*0\r\n"
        result, _ = RESP3.parse_array(test2)
        assert result == []
        
        # Nested array
        test3 = b"*2\r\n+outer\r\n*2\r\n+inner1\r\n+inner2\r\n"
        result, _ = RESP3.parse_array(test3)
        assert result == ["outer", ["inner1", "inner2"]]
        
        # Mixed types
        test4 = b"*3\r\n+string\r\n:123\r\n$5\r\nworld\r\n"
        result, _ = RESP3.parse_array(test4)
        assert result == ["string", 123, "world"]    
        
        # clusterduck
        test_string = b"*5\r\n:1\r\n:2\r\n:3\r\n:4\r\n$5\r\nhello\r\n"
        result, _ = RESP3.parse_array(test_string)
        assert result == [1, 2, 3, 4, "hello"]
        
        test_string = b"*2\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Hello\r\n-World\r\n"
        result, _ = RESP3.parse_array(test_string)
        assert result == [[1, 2, 3], ["Hello", "World"]]
        
        test_string = b"*3\r\n$5\r\nhello\r\n$-1\r\n$5\r\nworld\r\n"
        result, _ = RESP3.parse_array(test_string)
        print(result)
        assert result == ["hello", None, "world"]
    test_arrays()
    
    def test_null():
        test_string = b"_\r\n"
        result, _ = RESP3.parse_element(test_string)
        assert result is None
    test_null()
    
    def test_bool():
        test_strings = [
            b"#t\r\n",
            b"#f\r\n"
        ]
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert not result
    test_bool()
    
    def test_double():
        test_strings = [
            b",1.23\r\n",
            b":10\r\n",
            b",10\r\n",
            b",inf\r\n",
            b",-inf\r\n",
            b",nan\r\n",
        ]
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == 1.23
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == 10
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == 10.0
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == float("inf")
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == float("-inf")
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == float("NaN")
    test_double()
    
    def test_bignum():
         test_strings = [ 
            b"(349\r\n",
            b"(-349\r\n",
            b"(+349\r\n",
            b"(0\r\n",
            b"(-0\r\n",
         ]
         result, _ = RESP3.parse_element(test_strings.pop(0))
         assert result == 349
         
         result, _ = RESP3.parse_element(test_strings.pop(0))
         assert result == -349
         
         result, _ = RESP3.parse_element(test_strings.pop(0))
         assert result == 349
         
         result, _ = RESP3.parse_element(test_strings.pop(0))
         assert result == 0
         
         result, _ = RESP3.parse_element(test_strings.pop(0))
         assert result == 0
    test_bignum()
    
    def test_bulk_error():
        test_strings = [
            b"!21\r\nSYNTAX invalid syntax\r\n",
        ]
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == "SYNTAX invalid syntax"
    test_bulk_error()
    
    def test_verbatim_string():
        test_strings = [
            b"=15\r\ntxt:Some string\r\n",
        ]
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == "txt:Some string"
    test_verbatim_string()
    
    def test_map():
        test_strings = [
            b"%2\r\na:1\r\nb:2\r\n",
            b"%2\r\n+first\r\n:1\r\n+second\r\n:2\r\n"
        ]
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == {"a": 1, "b": 2}
    test_map()
    
    def test_attribute():
        test_strings = [
            b"|1\r\n+key-popularity\r\n%2\r\n$1\r\na\r\n,0.1923\r\n$1\r\nb\r\n,0.0012\r\n*2\r\n:2039123\r\n:9543892\r\n",
        ]
        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result.attribs == {"key-popularity": {"a": 0.1923, "b": 0.0012}}
        assert result.reply == [2039123, 9543892]
    test_attribute()

    def test_set():
        test_strings = [
            b"~7\r\n:1\r\n:2\r\n:3\r\n:4\r\n:5\r\n:6\r\n",
        ]        
        result, _ = RESP3.parse_element(test_strings.pop(0))
        assert result == {1, 2, 3, 4, 5, 6}
    test_set()
    
    def test_pushes():
        # TODO: impliment pushes
        pass 
