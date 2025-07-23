from ..CONSTANTS import CRLF
from ..util import slice_first_byte

def parse_double(data: bytes):
    if slice_first_byte(data) != b",":
        raise ValueError(f"Expected ',' for double-precision prefix, got {data[0]}")
    _prefix, _data = data.split(b",", 1)
    _data, _remaining = _data.split(CRLF, 1)
    return float(_data)
