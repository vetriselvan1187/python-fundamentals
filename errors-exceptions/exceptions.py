

# error

#for i in range(10) print True


#Exception - error detected while executing the code

#10/0

#3*name

#3+'name'


# Handling exception with try and except

try:
    10/0
except ZeroDivisionError as e:
    print(e)
    #raise e


# raise to throw specified exception

# user defined exception
class FileNotExistsError(BaseException):
    pass



# User defined custom exception
class FileError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.with_traceback = None
        self.__cause__ = None
        self.traceback = ('','','')



# raise to throw specified exception
try:
    open('some random filename', 'r', encoding='utf-8')
except FileNotFoundError as e:
    print(e)
    #raise FileNotExistsError('file does not exist error')


# exception chaining

try:
    open('some random file','r', encoding='utf-8')
except FileNotFoundError as e:
    print(e)
    #raise RuntimeError('runtime error')



# exception with traceback
# exception chaining

def call_method_1():
    try:
        1/0
    except ZeroDivisionError as e:
        tb = e.__traceback__
        raise Exception('call method 1 exception').with_traceback(tb)


def call_method_2():
    try:
        call_method_1()
    except Exception as e:
        tb = e.__traceback__
        print(tb)
        raise Exception('call method 2 exception').with_traceback(tb)


def call_method_3():
    try:
        call_method_1()
    except Exception as e:
        raise Exception('call method 3 exception')


#call_method_2()
#call_method_3()

# try except else finally

def open_file(filename):
    f = None
    try:
        f = open(filename, 'r', encoding='utf-8')
    except Exception as e:
        print(e)
        raise e
    else:
        print('file opened = ',f)
    finally:
        if f is not None:
            f.close()
    

import sys
print('try except else finally')
open_file(sys.argv[1])



