@classmethod
def parse_simple_error(cls, data:bytes) -> tuple[str, bytes]:
    if data[0].to_bytes() != b"-":
        raise ValueError(f"Expected '-' for simple error prefix, got {data[0]}")
    _prefix, _error = data.split(b"-", 1)
    _error, _remaining = _error.split(CRLF, 1)
    return str(_error, TEXT_ENCODING), _remaining
