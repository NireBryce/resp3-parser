from ..util import slice_first_byte


def parse_simple_string(data: bytes):
    """ Take a RESP3 simple string representation as bytes and return the 
        string it contains, as a string
    
        example: +OK\r\n
    """
    if slice_first_byte(data) != b"+":
        raise ValueError(f"Expected '+' for simple string prefix, got {data[0]}")
    print("Simple String")

def test_simple_string():
    _tests = [
        (b"+OK\r\n", "OK"),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        result = parse_simple_string(test[0])
        print(f'simple_string, {result=}')
        

# def test_simple_string():
#     test_string = b"+OK\r\n"
#     assert parse_simple_string(test_string) == ("OK")



# def parse_simple_string(data: bytes) -> tuple[str, bytes]:
#     # +OK\r\n
#     if slice_first_byte(data) != b"+":
#         raise ValueError(f"Expected '+' for simple string prefix, got {data[0]}")
#     _prefix, _str = data.split(b"+", 1)
#     _str, _remaining = _str.split(CRLF, 1)
#     return str(_str, TEXT_ENCODING), _remaining

# def test_simple_string():
#         test_string = b"+OK\r\n"
#         result, _ = RESP3.parse_element(test_string)
#         print(result)
#         assert result == ("OK")
#     test_simple_string()
