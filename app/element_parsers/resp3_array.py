from ..util import slice_first_byte
from ..CONSTANTS import CRLF
def parse_array(data: bytes):
    if slice_first_byte(data) != b'*':
        raise ValueError(f"Expected {b'*'} for array prefix, got {data[0]}")
    prefix, data = data.split(b"*", 1)
    length = int(data.split(CRLF, 1)[0])
    print(f"array, length: {length}")




    # for test in _tests:
    #     result = parse_array(test[0])
    #     print(f"{result=}")
    #     assert result == test[1]

# def parse_array(data: bytes):
#     if slice_first_byte(data) != b'*':
#         raise ValueError(f"Expected {b'*'} for array prefix, got {data[0]}")
#     _prefix, _data = data.split(b"*", 1)
#     _length, _data = _data.split(b"\r\n", 1)
#     _array = [] 
#     _array_member = []
#     if int(_length) == -1: 
#         return [None], _data
#     elif int(_length) == 0:
#         return [], _data
#     for i in range(int(_length)+1): 
#         # TODO: this needs to be redone because it doesn't work pseudo-recursively
#         # instead it just adds the first element of each loop
#         if _data and slice_first_byte(_data) in TYPES:
#             element, _data = parse_element(_data)
#             print(f"{element=}")
#             _array_member.append(element) 
#     # # TODO: also a hack
#     # if int(_length) > 1:
#     #     _array = _array.append([member for member in _array_member])
#     # elif int(_length) == 1: 
    
#     # TODO: append to array such that you only add extra lists if there are extra lists.  IE, why is this not recursing
#     # it should be [x, y] or [[a,b], [x,y]] if given two lists, it needs to nest the lists.
    
#     _remaining = _data
#     print(_array, _remaining)
#     return _array, _remaining

# def test_arrays():
#         # simple array
#         test1 = b"*2\r\n+hello\r\n:42\r\n"
#         result, _ = RESP3.parse_array(test1)
#         assert result == ["hello", 42] 

#         # Empty array
#         test2 = b"*0\r\n"
#         result, _ = RESP3.parse_array(test2)
#         assert result == []
        
#         # Nested array
#         test3 = b"*2\r\n+outer\r\n*2\r\n+inner1\r\n+inner2\r\n"
#         result, _ = RESP3.parse_array(test3)
#         assert result == ["outer", ["inner1", "inner2"]]
        
#         # Mixed types
#         test4 = b"*3\r\n+string\r\n:123\r\n$5\r\nworld\r\n"
#         result, _ = RESP3.parse_array(test4)
#         assert result == ["string", 123, "world"]    
        
#         # clusterduck
#         test_string = b"*5\r\n:1\r\n:2\r\n:3\r\n:4\r\n$5\r\nhello\r\n"
#         result, _ = RESP3.parse_array(test_string)
#         assert result == [1, 2, 3, 4, "hello"]
        
#         test_string = b"*2\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Hello\r\n-World\r\n"
#         result, _ = RESP3.parse_array(test_string)
#         assert result == [[1, 2, 3], ["Hello", "World"]]
        
#         test_string = b"*3\r\n$5\r\nhello\r\n$-1\r\n$5\r\nworld\r\n"
#         result, _ = RESP3.parse_array(test_string)
#         print(result)
#         assert result == ["hello", None, "world"]
#     test_arrays()


