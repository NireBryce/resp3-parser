from ..util import slice_first_byte
def parse_null(data: bytes):
    if slice_first_byte(data) != b"_":
        raise ValueError(f"Expected '_' for null prefix, got {data[0]}")
    print("null")


# def parse_null(data: bytes):
#     if slice_first_byte(data) != b"_":
#         raise ValueError(f"Expected '_' for null prefix, got {data[0]}")
#     return None
