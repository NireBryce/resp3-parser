from ..CONSTANTS import CRLF
from ..util import slice_first_byte
def parse_push(data: bytes):
    if slice_first_byte(data) != b">":
        raise ValueError(f"Expected '>' for push prefix, got {data[0]}")
    _prefix, _data = data.split(b">", 1)
    _length, _data = _data.split(CRLF, 1)
    pass # handle this eventually but it wants callbacks
