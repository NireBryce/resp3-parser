from element_parsers.resp3_bulk_string import parse_bulk_string
def test_bulk_string():
    _tests = [
        (b"$5\r\nhello\r\n", "hello"),
        # empty
        (b"$0\r\n\r\n", ""),
        # null
        (b"$-1\r\n", None), 
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_bulk_string(test[0])

