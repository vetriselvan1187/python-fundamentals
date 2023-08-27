

class X:
    def __init__(self, name):
        self.name = name
    def print_method(self):
        print('printing method of x')
    def printX(self):
        print('printing X')


class Y:
    def __init__(self, name):
        self.name = name
    def print_method(self):
        print('printing method of y')
    def printY(self):
        print('printing Y')

class Z:
    def __init__(self, name):
        self.name = name
    def print_method(self):
        print('printing method of z')
    def printZ(self):
        print('printing Z')


class XYZ(X,Y,Z):
    def __init__(self, name):
        super().__init__(name)
    def print_method(self):
        print('printing method of xyz')

xyz = XYZ('xyz')

xyz.print_method()
xyz.printY()


