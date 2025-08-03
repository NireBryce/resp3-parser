from ..util import slice_first_byte
def parse_boolean(data:bytes):
        if slice_first_byte(data) != b"#":
            raise ValueError(f"Expected '#' for boolean prefix, got {data[0]}")
        print("boolean")
def test_boolean():
    _tests = [
        (b"#t\r\n", True),
        (b"#f\r\n", False),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        result = parse_boolean(test[0])
        print(f'boolean, {result=}')

# def parse_boolean(data:bytes):
#         if slice_first_byte(data) != b"#":
#             raise ValueError(f"Expected '#' for boolean prefix, got {data[0]}")
#         _prefix, _bool = data.split(b"#", 1)
#         _bool, _remaining = _bool.split(CRLF, 1)
#         if _bool == b"t":
#             _result = True
#         elif _bool == b"f":
#             _result = False
#         else:
#             raise ValueError
#         return _result

# def test_bool():
#         test_strings = [
#             b"#t\r\n",
#             b"#f\r\n"
#         ]
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result
        
#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert not result
#     test_bool()
    