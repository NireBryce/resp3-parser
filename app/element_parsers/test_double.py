from app.element_parsers.resp3_double import parse_double
def test_double():
    _tests = [
        (b",1.23\r\n", 1.23),
        (b":10\r\n", 10),
        (b",10\r\n", 10.0),
        (b",inf\r\n", float("inf")),
        (b",-inf\r\n", float("-inf")),
        (b",nan\r\n", float("NaN")),
    ]

    # minimal to test identification functionality
    for test in _tests:
        parse_double(test[0])
