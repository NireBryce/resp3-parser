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
        self.cursor = b''
        self.data = self.to_list_chunks(resp3_request)
    def update_cursor(self):
        self.cursor = self.data[self.position]

    def parse(self, prefix):
        self.cursor = self.data[self.position]
        match self.cursor: 
            case b"+": 
                
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
        
        prefix = self.cursor
        self.position += 1
        self.parse(prefix)


    def find_length(self):
        length = 0
        while self.cursor != b'\r\n': 
            self.position += 1
            length += 1
        self.update_cursor()
        return length
    

