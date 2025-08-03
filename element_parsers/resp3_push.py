from ..app.CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_push(data: bytes):
    _PREFIX = b">"
    if slice_first_byte(data) != _PREFIX:
        raise ValueError(f"Expected '{_PREFIX}' for push prefix, got {data[0]}")
    length = data.split(CRLF)[1]
    print(f"push, length: {length}")
    



# def test_pushes():
#     # TODO: impliment pushes
#     pass 
