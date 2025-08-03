class RESP3Parser: 
    def __init__(self, data: bytes):
        self.data = data
        self.position = 0
        self.cursor = b''
    
    
    def step(self):
        self.cursor = self.data[self.position]
        self.position += 1

    def find_length(self):
        length = 0
        while self.cursor != b'\r\n': 
            self.position += 1
            length += 1
        return length
    

