def slice_first_byte(data: bytes):
    """ b'xyz'[0] -> 120 because there is no 'byte' literal, only 
        byte-sequence literals.  By taking a sequence of length 1, 
        we get b'<data[0]>' instead of the int value of the byte
    """
    return data[:1]
