from ..util import slice_first_byte


def parse_double(data: bytes):
    _PREFIX = b","
    if slice_first_byte(data) != _PREFIX:
        print(f"error: '{data[:1]}' is not '{_PREFIX}'")
        # raise ValueError(f"Expected ',' for double-precision prefix, got {data[0]}")
    print("double")






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
