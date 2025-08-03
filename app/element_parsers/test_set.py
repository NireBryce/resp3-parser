from app.element_parsers.resp3_set import parse_set
def test_set():
    _tests = [
        (b"~7\r\n:1\r\n:2\r\n:3\r\n:4\r\n:5\r\n:6\r\n", {1, 2, 3, 4, 5, 6})
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_set(test[0])
