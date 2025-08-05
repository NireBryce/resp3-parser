from CONSTANTS import TYPES
class RESP3Parser: 
    def __init__(self, data: bytes):
        self.data = data
        self.position = 0
        self.cursor = b''
    
    def update_cursor(self):
        self.cursor = self.data[self.position]
    def step(self):
        self.cursor = self.data[self.position]
        if self.cursor in TYPES:
            self.position += 1
            length = self.find_length()
            
            
            
            

    def find_length(self):
        length = 0
        while self.cursor != b'\r\n': 
            self.position += 1
            length += 1
        self.update_cursor()
        return length
    

