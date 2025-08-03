from app.element_parsers.resp3_simple_error import parse_simple_error
def test_simple_error():
    _tests = [
        (b"-Error message\r\n", "Error message"),
        (b"-ERR unknown command 'asdf'\r\n", "ERR unknown command 'asdf'"),
        (b"-WRONGTYPE Operation against a key holding the wrong kind of value\r\n", "WRONGTYPE Operation against a key holding the wrong kind of value"),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_simple_error(test[0])
