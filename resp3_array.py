def parse_array(data: bytes):
    if data[0].to_bytes() != b'*':
        raise ValueError(f"Expected {b'*'} for array prefix, got {data[0]}")
    _prefix, _data = data.split(b"*", 1)
    _length, _data = _data.split(b"\r\n", 1)
    _array = [] 
    _array_member = []
    if int(_length) == -1: 
        return [None], _data
    elif int(_length) == 0:
        return [], _data
    for i in range(int(_length)+1): 
        # TODO: this needs to be redone because it doesn't work pseudo-recursively
        # instead it just adds the first element of each loop
        if _data and _data[0].to_bytes() in TYPES:
            element, _data = RESP3.parse_element(_data)
            print(f"{element=}")
            _array_member.append(element) 
    # # TODO: also a hack
    # if int(_length) > 1:
    #     _array = _array.append([member for member in _array_member])
    # elif int(_length) == 1: 
    
    # TODO: append to array such that you only add extra lists if there are extra lists.  IE, why is this not recursing
    # it should be [x, y] or [[a,b], [x,y]] if given two lists, it needs to nest the lists.
    
    _remaining = _data
    print(_array, _remaining)
    return _array, _remaining
