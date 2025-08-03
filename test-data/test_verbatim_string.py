from element_parsers.resp3_verbatim_string import parse_verbatim_string
def test_verbatim_string():
    _tests = [
        (b"=15\r\ntxt:Some string\r\n", "txt:Some string")
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_verbatim_string(test[0])
