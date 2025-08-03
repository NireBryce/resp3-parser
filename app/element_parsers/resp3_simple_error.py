from ..util import slice_first_byte

def parse_simple_error(data:bytes):
    if slice_first_byte(data) != b"-":
        raise ValueError(f"Expected '-' for simple error prefix, got {data[0]}")
    print("Simple Error")

def test_simple_error():
    _tests = [
        (b"-Error message\r\n", "Error message"),
        (b"-ERR unknown command 'asdf'\r\n", "ERR unknown command 'asdf'"),
        (b"-WRONGTYPE Operation against a key holding the wrong kind of value\r\n", "WRONGTYPE Operation against a key holding the wrong kind of value"),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        result = parse_simple_error(test[0])
        print(f'{result=}')
        




# def parse_simple_error(data:bytes) -> tuple[str, bytes]:
#     if slice_first_byte(data) != b"-":
#         raise ValueError(f"Expected '-' for simple error prefix, got {data[0]}")
#     _prefix, _error = data.split(b"-", 1)
#     _error, _remaining = _error.split(CRLF, 1)
#     return str(_error, TEXT_ENCODING), _remaining


# def test_simple_error():
#         test_string = b"-Error message\r\n"
#         result, _ = RESP3.parse_element(test_string)
#         assert result == ("Error message")
        
#         test_string = b"-ERR unknown command 'asdf'\r\n"
#         result, _ = RESP3.parse_element(test_string)
#         assert result == ("ERR unknown command 'asdf'")
        
#         test_string = b"-WRONGTYPE Operation against a key holding the wrong kind of value\r\n"
#         result, _ = RESP3.parse_element(test_string)
#         assert result == ("WRONGTYPE Operation against a key holding the wrong kind of value")
