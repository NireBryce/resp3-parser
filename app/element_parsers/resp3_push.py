from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_push(data: bytes):
    if slice_first_byte(data) != b">":
        raise ValueError(f"Expected '>' for push prefix, got {data[0]}")
    length = data.split(CRLF)[1]
    print(f"push, length: {length}")
    
def test_push():
    # TODO: impliment pushes
    _tests = [
    
    ]
    
    # minimal to test identification functionality
    for test in _tests:
        result = parse_push(test[0])
        print(f'{result=}')
            

# def test_pushes():
#     # TODO: impliment pushes
#     pass 
