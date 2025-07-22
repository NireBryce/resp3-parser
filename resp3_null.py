def parse_null(data: bytes):
        if data[0].to_bytes() != b"_":
            raise ValueError(f"Expected '_' for null prefix, got {data[0]}")
        _prefix, _remaining = data.split(b"_", 1)
        return None, _remaining
