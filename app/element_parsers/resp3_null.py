from ..util import slice_first_byte
def parse_null(data: bytes):
    if slice_first_byte(data) != b"_":
        raise ValueError(f"Expected '_' for null prefix, got {data[0]}")
    print("null")

def test_null():
    _tests = [
        (b"_\r\n", None)
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        result = parse_null(test[0])
        print(f'null, {result=}')
        
# def parse_null(data: bytes):
#     if slice_first_byte(data) != b"_":
#         raise ValueError(f"Expected '_' for null prefix, got {data[0]}")
#     return None

# def test_null():
#         test_string = b"_\r\n"
#         result, _ = RESP3.parse_element(test_string)
#         assert result is None
#     test_null()
