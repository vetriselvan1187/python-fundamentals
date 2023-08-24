
# operator overloading or special methods


 
# operator overloading string
 
class mystr(str):
    def __new__(cls, s):
        self = super().__new__(cls, s)
        self.__init__(s)
        return self
    def __init__(self, s):
        self.s = s
    def __getitem__(self, index):
        return self.s[index]
    def __mul__(self, num):
	return mystr(self.s*num)
        #return NotImplemented




