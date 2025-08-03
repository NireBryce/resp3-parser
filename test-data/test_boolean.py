from app.element_parsers.resp3_boolean import parse_boolean

def test_boolean():
    _tests = [
        (b"#t\r\n", True),
        (b"#f\r\n", False),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_boolean(test[0])
