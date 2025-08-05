from ast import Pass
from CONSTANTS import TYPES
class RESP3Parser: 
    @classmethod
    def to_list_chunks(cls, resp3_request):
        """ convert a request from bytes to string, and split into a list of 
            strings at the CRLF boundaries so they're easier to iterate through
        """
        return str(resp3_request, "utf-8").split() 
    def __init__(self, resp3_request: bytes):
        self.position = 0
        self.cursor: bytes = b''
        self.data = resp3_request
        # self.data = self.to_list_chunks(resp3_request)
        self.results = []
        self._sync_cursor()
    def _sync_cursor(self):
        self.cursor = self.data[:self.position] # absurd way to get a one-character bytes literal

    def step(self):
        self.position += 1
        self._sync_cursor
    
    def _simple_parse(self):
        _result = b""
        while self.cursor != b"\r":
            _result += self.cursor
            self.step()
        self.step() # skip \n
        return _result
    def _simple_parse_edge_case_loop(self):
        while self.cursor != b"\r":
            self.step()
        self.step() # skip \n
        
    def resp3_simple_str(self):
        self.results.append(str(self._simple_parse()))
    def resp3_simple_error(self):
        self.results.append(str(self._simple_parse()))
    
    def resp3_integer(self):
        self.results.append(int(self._simple_parse()))
    
    def resp3_boolean(self):
        _bool = False if self.cursor == "f" else True
        self._simple_parse_edge_case_loop()
        self.results.append(bool(_bool))
    
    def resp3_null(self):
        self._simple_parse_edge_case_loop()
        self.results.append(None)
        
    def resp3_double(self):
        self.results.append(int(self._simple_parse()))
        
    def resp3_bignum(self):
        self.results.append(int(self._simple_parse()))
    
    def _aggregate_parse(self):
        length = b""
        while self.cursor != b"\r":
            length += self.cursor
            self.step()
        
    
    def dispatch(self, prefix):
        if prefix == b"+":
                self.resp3_simple_str()
        if prefix == b"-":
            self.resp3_simple_error()
        if prefix == b":":
            self.resp3_integer()
            

    def parse(self):
        while True:
            prefix: bytes = self.cursor
            self.step()
            self.dispatch(prefix)
            
                
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
    

