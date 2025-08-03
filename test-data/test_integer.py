from element_parsers.resp3_integer import parse_integer
def test_integer():
    _tests = [
        (b":0\r\n", 0),
        (b":1000\r\n", 1000)
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_integer(test[0])

