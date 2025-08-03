from ..CONSTANTS import CRLF
from ..util import slice_first_byte


def parse_double(data: bytes):
    if slice_first_byte(data) != b",":
        raise ValueError(f"Expected ',' for double-precision prefix, got {data[0]}")
    print("double")


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
        result = parse_double(test[0])
        print(f"{result=}")


# def parse_double(data: bytes):
#    """ it matches the float format for python, so we can just pass it on through
#    """
#     if slice_first_byte(data) != b",":
#         raise ValueError(f"Expected ',' for double-precision prefix, got {data[0]}")
#     _prefix, _data = data.split(b",", 1)
#     _data, _remaining = _data.split(CRLF, 1)
#     return float(_data)

# def test_double():
#         test_strings = [
#             b",1.23\r\n",
#             b":10\r\n",
#             b",10\r\n",
#             b",inf\r\n",
#             b",-inf\r\n",
#             b",nan\r\n",
#         ]

#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == 1.23

#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == 10

#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == 10.0

#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == float("inf")

#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == float("-inf")

#         result, _ = RESP3.parse_element(test_strings.pop(0))
#         assert result == float("NaN")
#     test_double()
