from app.element_parsers.resp3_array import parse_array
def test_array():
    _tests = [
        # simple array
        (b"*2\r\n+hello\r\n:42\r\n", ["hello", 42]),
        # empty array
        (b"*0\r\n", []),
        # nested array
        (b"*2\r\n+outer\r\n*2\r\n+inner1\r\n+inner2\r\n", ["outer", ["inner1", "inner2"]]),
        # mixed types
        (b"*3\r\n+string\r\n:123\r\n$5\r\nworld\r\n", ["string", 123, "world"]),
        # clusterduck
        (b"*5\r\n:1\r\n:2\r\n:3\r\n:4\r\n$5\r\nhello\r\n", [1, 2, 3, 4, "hello"]),
        (b"*2\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Hello\r\n-World\r\n", [[1, 2, 3], ["Hello", "World"]]),
        (b"*3\r\n$5\r\nhello\r\n$-1\r\n$5\r\nworld\r\n", ["hello", None, "world"]),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_array(test[0])
