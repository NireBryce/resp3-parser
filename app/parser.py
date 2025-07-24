from CONSTANTS import CRLF, TEXT_ENCODING, TYPES
from element_parsers.resp3_parser_elements import RESP3
from util import slice_first_byte
class RESP3_Parser:
    """ split data into chunks based on CRLF
        scan chunks for type indicator
        grab the length [the rest of the chunk]
        process chunks 'belonging' to that chunk, adding them as their actual type to a new list
        incriment position past those chunks
        
        consider: first pass, convert all types to their actual type
                  second pass, collect items into their parent multi-member types 
                  
        just encode the bytes into the string representation, 
        there don't seem to be downsides in the spec and it 
        means slicing won't bite you
        
        maybe hold a quque of complex objects like arrays and fill them as you go
        
    """
    class _RESP3_Cursor:
        def __init__(self, split_data, current_operation=None):
            self.chunks = split_data
            self.position = 0
            self.current_operation = current_operation
            
    def __init__(self, data):
        self.data = data.split(CRLF)
        self.position = 0
        self.cursor = self._RESP3_Cursor(self.data)

    def parse_element(self, chunk):
        data = chunk
        match slice_first_byte(data):
            case b"+": 
                _result = RESP3.simple_string(data)
            case b"-": 
                _result = RESP3.simple_error(data)
            case b":": 
                _result = RESP3.integer(data)
            case b"$": 
                _result = RESP3.bulk_string(data)
            case b"*": 
                _result = RESP3.array(data)
            case b"_": 
                _result = RESP3.null(data)
            case b"#": 
                _result = RESP3.boolean(data)
            case b",": 
                _result = RESP3.double(data)
            case b"(": 
                _result = RESP3.bignum(data)
            case b"!": 
                _result = RESP3.bulk_error(data)
            case b"=": 
                _result = RESP3.verbatim_string(data)
            case b"%": 
                _result = RESP3.map(data)
            case b"|":
                _result = RESP3.attribute(data)
            case b"~": 
                _result = RESP3.set(data)
            # case b">": 
                # _result = parse_push(data)
            case b"":
                return print("Out of elements")
            case _:
                raise ValueError(f"Expected one of {TYPES}, got {data[0]}; input not in bytes or missing prefix?")
        return (_result)
    @classmethod
    def parse(cls, data):
        # data
        # parse current position as many times as length requires
        # tracking the position
        # add parse to list of completed elements
        # update position
        _data = data
        return _data
