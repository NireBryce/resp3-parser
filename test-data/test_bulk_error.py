from element_parsers.resp3_bulk_error import parse_bulk_error
def test_bulk_error():
    _tests = [
        (b"!21\r\nSYNTAX invalid syntax\r\n", "SYNTAX invalid syntax"),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_bulk_error(test[0])
