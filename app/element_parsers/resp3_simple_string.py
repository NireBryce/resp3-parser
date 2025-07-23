from ..CONSTANTS import TEXT_ENCODING, CRLF
from ..util import slice_first_byte
def parse_simple_string(data: bytes) -> tuple[str, bytes]:
    # +OK\r\n
    if slice_first_byte(data) != b"+":
        raise ValueError(f"Expected '+' for simple string prefix, got {data[0]}")
    _prefix, _str = data.split(b"+", 1)
    _str, _remaining = _str.split(CRLF, 1)
    return str(_str, TEXT_ENCODING), _remaining
