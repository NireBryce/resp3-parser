from element_parsers.resp3_null import parse_null
def test_null():
    _tests = [
        (b"_\r\n", None)
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_null(test[0])

