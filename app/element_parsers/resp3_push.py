from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_push(data: bytes):
    if slice_first_byte(data) != b">":
        raise ValueError(f"Expected '>' for push prefix, got {data[0]}")
    length = data.split(CRLF)[1]
    print(f"push, length: {length}")
