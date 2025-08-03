from element_parsers.resp3_map import parse_map
def test_map():
    _tests = [
        (b"%2\r\na:1\r\nb:2\r\n", {"a": 1, "b": 2}),
        (b"%2\r\n+first\r\n:1\r\n+second\r\n:2\r\n", {"first": 1, "second": 2}),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_map(test[0])

