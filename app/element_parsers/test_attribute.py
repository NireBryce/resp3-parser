from app.element_parsers.resp3_attribute import parse_attribute
def test_attribute():
    _tests = [
        (b"|1\r\n+key-popularity\r\n%2\r\n$1\r\na\r\n,0.1923\r\n$1\r\nb\r\n,0.0012\r\n*2\r\n:2039123\r\n:9543892\r\n", 
            (
                # Attribs
                {"key-popularity": {"a": 0.1923, "b": 0.0012}},
                # reply value
                [2039123, 9543892])
        )
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_attribute(test[0])
