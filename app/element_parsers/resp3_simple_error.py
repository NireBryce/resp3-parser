from ..CONSTANTS import TEXT_ENCODING, CRLF
from ..util import slice_first_byte
def parse_simple_error(data:bytes) -> tuple[str, bytes]:
    if slice_first_byte(data) != b"-":
        raise ValueError(f"Expected '-' for simple error prefix, got {data[0]}")
    _prefix, _error = data.split(b"-", 1)
    _error, _remaining = _error.split(CRLF, 1)
    return str(_error, TEXT_ENCODING), _remaining
