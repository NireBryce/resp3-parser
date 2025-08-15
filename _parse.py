from ast import Pass
from CONSTANTS import TYPES
class RESP3Parser: 
    @classmethod
    def to_str_chunks(cls, resp3_request):
        """ convert a request from bytes to string, and split into a list of 
            strings at the CRLF boundaries so they're easier to iterate through
        """
        return str(resp3_request, "utf-8").split() 
    def __init__(self, resp3_request: bytes):
        self.data = self.to_str_chunks(resp3_request)
        self.position = 0
        self.results = []
        self.debug_previous = []
        self.cursor = self.data[self.position]
        # self.step() # load first into queue
        
        # I really need to figure out a way to do 'for elem in data:' but then skip iterations.
        # or just handle every thing in every loop but oof.


    def step(self):
        self.debug_previous.append(self.cursor)
        self.cursor = self.data[self.position]
    
    def _simple_parse(self):
        result = None
        
        # _result = b""
        # while self.cursor:
        #     _result += self.cursor
        #     self.step()
        # self.step() # skip \n
        # return _result
    def _simple_parse_edge_case_loop(self):
        while self.cursor != b"\r":
            self.step()
        self.step() # skip \n
        
    def resp3_simple_str(self):
        return str(self._simple_parse())
    def resp3_simple_error(self):
        return str(self._simple_parse())
    
    def resp3_integer(self):
        return int(self._simple_parse())
    
    def resp3_boolean(self):
        _bool = False if self.cursor == "f" else True
        self._simple_parse_edge_case_loop()
        return bool(_bool)
    
    def resp3_null(self):
        self._simple_parse_edge_case_loop()
        return None
        
    def resp3_double(self):
        return int(self._simple_parse())
        
    def resp3_bignum(self):
        return int(self._simple_parse())
    
    def parse_length(self):
        length = b""
        while self.cursor != b"\r":
            length += self.cursor
            self.step()
        self.step() # skip \n
        
        return int(length)
        
    def _aggregate_parse(self, length):
        elements = []
        for _ in range(length): # TODO: check if this needs to be length + 1
            element = None
            while self.cursor != b"\r":
                element = self.dispatch() # this should run once, ie, this while-loop should end immediately after.
            self.step() # remove \n
            elements.append(element) 
        return elements
    
    def resp3_array(self):
        length = self.parse_length()
        if int(length) == -1: 
            return [None]
        elif int(length) == 0:
            return []
        else:
            elements = self._aggregate_parse(length)
            return elements
    
    def resp3_map(self):
        length = self.parse_length()
        elements = {}
        for _ in range(length):
            key = self.dispatch()
            value = self.dispatch()
            elements[key] = value
        return elements
    
    def resp3_attribute(self):
        length = self.parse_length()
        attrs = {}
        for _ in range(length):
            name = self.dispatch()
            attr = self.dispatch()
            attrs[name] = attr
        return attrs
        # TODO: may have to also handle the reply here? documentation unclear.
    
    def dispatch(self):
        prefix: bytes = self.cursor
        self.step()
        if prefix == b"+":
            return self.resp3_simple_str()
        if prefix == b"-":
            return self.resp3_simple_error()
        if prefix == b":":
            return self.resp3_integer()
            

    def parse(self):
        while True:
            self.results.append(self.dispatch())
            
                
        match self.cursor: 
            case b"+":
                position += 1
                
            # case b"-":
            # case b":":
            # case b"$":
            # case b"*":
            # case b"_":
            # case b"#":
            # case b",":
            # case b"(":
            # case b"!":
            # case b"=":
            # case b"%":
            # case b"|":
            # case b"~":
            # case b">":
        

        self.position += 1
        self.parse(prefix)

def parse_simple_string(data:str):
    """ Take a RESP3 simple string representation as bytes and return the 
        string it contains, as a string
    
        example: +OK\r\n
    PREFIX = "+"
    """
    prefix, data = data.split("+")
    return str(data)

    def find_length(self):
        length = 0
        while self.cursor != b'\r\n': 
            self.position += 1
            length += 1
        self.update_cursor()
        return length
    

