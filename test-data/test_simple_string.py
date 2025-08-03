from element_parsers.resp3_simple_string import parse_simple_string
def test_simple_string():
    _tests = [
        (b"+OK\r\n", "OK"),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_simple_string(test[0])
