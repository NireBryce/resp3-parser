from ..util import slice_first_byte
def parse_bignum(data: bytes):
    if slice_first_byte(data) != b"(":
        raise ValueError(f"Expected '(' for bignum prefix, got {data[0]}")
    print("bignum")

def test_bignum():
    _tests = [
        ( b"(349\r\n", 349 ),
        ( b"(-349\r\n", -349 ),
        ( b"(+349\r\n", 349 ),
        ( b"(0\r\n", 0 ),
        ( b"(-0\r\n", 0 )
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        result = parse_bignum(test[0])
        print(f'bignum, {result=}')

# def parse_bignum(data: bytes):
#     if slice_first_byte(data) != b"(":
#         raise ValueError(f"Expected '(' for bignum prefix, got {data[0]}")

#     _prefix, _data = data.split(b"(", 1)
#     _data, _remaining = _data.split(CRLF, 1)
#     return int(_data)

# def test_bignum():
#          test_strings = [ 
            # b"(349\r\n",
            # b"(-349\r\n",
            # b"(+349\r\n",
            # b"(0\r\n",
            # b"(-0\r\n",
#          ]
#          result, _ = RESP3.parse_element(test_strings.pop(0))
#          assert result == 349
         
#          result, _ = RESP3.parse_element(test_strings.pop(0))
#          assert result == -349
         
#          result, _ = RESP3.parse_element(test_strings.pop(0))
#          assert result == 349
         
#          result, _ = RESP3.parse_element(test_strings.pop(0))
#          assert result == 0
         
#          result, _ = RESP3.parse_element(test_strings.pop(0))
#          assert result == 0
#     test_bignum()
