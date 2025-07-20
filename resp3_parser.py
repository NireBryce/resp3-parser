CRLF = "\r\n"

star
class Resp3Message:
    def __init__(self, message):
        self.message: bytes = message
        self.splits = message.split(CRLF)
        self.chunk = None
        self.position = 0
    def step(self):
        self.chunk = self.splits[self.position]
        self.parse(self.chunk)
        self.position += 1
    def parse(self): 
        pass
