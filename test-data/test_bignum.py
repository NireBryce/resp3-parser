from app.element_parsers.resp3_bignum import parse_bignum
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
        parse_bignum(test[0])
