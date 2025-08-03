from app.element_parsers.resp3_array import parse_array
from app.element_parsers.resp3_attribute import parse_attribute
from app.element_parsers.resp3_bignum import parse_bignum
from app.element_parsers.resp3_boolean import parse_boolean
from app.element_parsers.resp3_bulk_error import parse_bulk_error
from app.element_parsers.resp3_bulk_string import parse_bulk_string
from app.element_parsers.resp3_double import parse_double
from app.element_parsers.resp3_integer import parse_integer
from app.element_parsers.resp3_map import parse_map
from app.element_parsers.resp3_null import parse_null
from app.element_parsers.resp3_push import parse_push
from app.element_parsers.resp3_set import parse_set
from app.element_parsers.resp3_simple_error import parse_simple_error
from app.element_parsers.resp3_simple_string import parse_simple_string
from app.element_parsers.resp3_verbatim_string import parse_verbatim_string


def test_array():
    _tests = [
        # simple array
        (b"*2\r\n+hello\r\n:42\r\n", ["hello", 42]),
        # empty array
        (b"*0\r\n", []),
        # nested array
        (
            b"*2\r\n+outer\r\n*2\r\n+inner1\r\n+inner2\r\n",
            ["outer", ["inner1", "inner2"]],
        ),
        # mixed types
        (b"*3\r\n+string\r\n:123\r\n$5\r\nworld\r\n", ["string", 123, "world"]),
        # clusterduck
        (b"*5\r\n:1\r\n:2\r\n:3\r\n:4\r\n$5\r\nhello\r\n", [1, 2, 3, 4, "hello"]),
        (
            b"*2\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Hello\r\n-World\r\n",
            [[1, 2, 3], ["Hello", "World"]],
        ),
        (b"*3\r\n$5\r\nhello\r\n$-1\r\n$5\r\nworld\r\n", ["hello", None, "world"]),
    ]

    # minimal to test identification functionality
    for test in _tests:
        parse_array(test[0])




def test_attribute():
    _tests = [
        (
            b"|1\r\n+key-popularity\r\n%2\r\n$1\r\na\r\n,0.1923\r\n$1\r\nb\r\n,0.0012\r\n*2\r\n:2039123\r\n:9543892\r\n",
            (
                # Attribs
                {"key-popularity": {"a": 0.1923, "b": 0.0012}},
                # reply value
                [2039123, 9543892],
            ),
        )
    ]

    # minimal to test identification functionality
    for test in _tests:
        parse_attribute(test[0])

def test_bignum():
    _tests = [
        ( b"(349\r\n", 349 ),
        ( b"(-349\r\n", -349 ),
        ( b"(+349\r\n", 349 ),
        ( b"(0\r\n", 0 ),
        ( b"(-0\r\n", 0 )
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_bignum(test[0])


def test_boolean():
    _tests = [
        (b"#t\r\n", True),
        (b"#f\r\n", False),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_boolean(test[0])

def test_bulk_error():
    _tests = [
        (b"!21\r\nSYNTAX invalid syntax\r\n", "SYNTAX invalid syntax"),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_bulk_error(test[0])

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

def test_integer():
    _tests = [
        (b":0\r\n", 0),
        (b":1000\r\n", 1000)
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_integer(test[0])

def test_map():
    _tests = [
        (b"%2\r\na:1\r\nb:2\r\n", {"a": 1, "b": 2}),
        (b"%2\r\n+first\r\n:1\r\n+second\r\n:2\r\n", {"first": 1, "second": 2}),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_map(test[0])

def test_null():
    _tests = [
        (b"_\r\n", None)
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_null(test[0])

def test_push():
    # TODO: impliment pushes
    _tests = [
    
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_push(test[0])

def test_set():
    _tests = [
        (b"~7\r\n:1\r\n:2\r\n:3\r\n:4\r\n:5\r\n:6\r\n", {1, 2, 3, 4, 5, 6})
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_set(test[0])

def test_simple_error():
    _tests = [
        (b"-Error message\r\n", "Error message"),
        (b"-ERR unknown command 'asdf'\r\n", "ERR unknown command 'asdf'"),
        (b"-WRONGTYPE Operation against a key holding the wrong kind of value\r\n", "WRONGTYPE Operation against a key holding the wrong kind of value"),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_simple_error(test[0])

def test_simple_string():
    _tests = [
        (b"+OK\r\n", "OK"),
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_simple_string(test[0])
        
def test_verbatim_string():
    _tests = [
        (b"=15\r\ntxt:Some string\r\n", "txt:Some string")
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        parse_verbatim_string(test[0])

if __name__ == "__main__":
    test_array()
    test_attribute()
    test_bignum()
    test_boolean()
    test_bulk_error()
    test_bulk_string()
    test_double()
    test_integer()
    test_map()
    test_null()
    test_push()
    test_set()
    test_simple_error()
    test_simple_string()
    test_verbatim_string()
