@classmethod
def parse_push(cls, data: bytes):
    if data[0].to_bytes() != b">":
        raise ValueError(f"Expected '>' for push prefix, got {data[0]}")
    _prefix, _data = data.split(b">", 1)
    _length, _data = _data.split(CRLF, 1)
    pass # handle this eventually but it wants callbacks
