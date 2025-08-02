from ..CONSTANTS import TEXT_ENCODING, CRLF
from ..util import slice_first_byte
def parse_bulk_error(data: bytes):
    if slice_first_byte(data) != b"!":
        raise ValueError(f"Expected '!' for bulk error prefix, got {data[0]}")
    length = data.split(CRLF)[1]
    print(f"bulk error, length: {length}")


# def parse_bulk_error(data: bytes):
#     if slice_first_byte(data) != b"!":
#         raise ValueError(f"Expected '!' for bulk error prefix, got {data[0]}")

#     _prefix, _data = data.split(b"!", 1)
#     _length, _data = _data.split(CRLF, 1)
#     _data, _remaining = _data.split(CRLF, 1)
#     _error = _data[:int(_length)]
#     return str(_error, TEXT_ENCODING)
