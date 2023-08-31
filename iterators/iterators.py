
# Iterate odd indices
class OddIndexIterator:
    def __init__(self, data):
        self.data = data
        self.len = len(data)
        self.index = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= self.len:
            raise StopIteration
        value = self.data[self.index]
        self.index = self.index+2
        return value


# Iterate even indices
class EvenIndexIterator:
    def __init__(self, data):
        self.data = data
        self.len = len(data)
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= self.len:
            raise StopIteration
        value = self.data[self.index]
        self.index = self.index+2
        return value


#for num in EvenIndexIterator([i for i in range(20)]):
#    print(num)


#for num in OddIndexIterator([i for i in range(20)]):
#    print(num)


print([num for num in EvenIndexIterator([i for i in range(20)])])
print([num for num in OddIndexIterator([i for i in range(20)])])



#



#



#
