
# decorators example

def deco1(func):
    def wrapper(*args, **kwargs):
        print('deco1 start')
        x = func(*args, **kwargs)
        print('deco1 end')
        return x
    return wrapper
    
def deco2(func):
    def wrapper(*args, **kwargs):
        print('deco2 start')
        x = func(*args, **kwargs)
        print('deco2 end')
        return x
    return wrapper

@deco1
@deco2
def exec_business_logic():
    print('executing business logic')
    

exec_business_logic()


import time

def logging(doc):
    def decorated(func):
        def wrapper(*args, **kwargs):
            print('logging = executing func = ')
            x = func(*args, **kwargs)
            print('logging end = ')
            return x
        return wrapper
    return decorated


def instrumenting(func):
    def wrapper(*args, **kwargs):
       start = time.time_ns()        
       x = func(*args, **kwargs)
       diff = time.time_ns()-start
       print('time taken to execute the function = ', diff/1000000000, 'seconds')
       return x
    return wrapper


@logging
@instrumenting
def my_func():
    time.sleep(2)
    print('executing my func')
    time.sleep(2)
    print('ending execution of my func')


my_func()
      
# -------

#2 decorator with arguments
def my_instrument(doc):
    def decorated(func):
        def wrapper(*args, **kwargs):
            print(doc, func.__name__)
            print('start')
            func(*args, **kwargs)
            print('end')
        return wrapper
    return decorated



@my_instrument('This is a doc')
def print_my_name():
    print('printing my name')


#3
import functools
def my_instrument(doc):
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(doc, func.__name__)
            print('start')
            func(args, kwargs)
            print('end')
        return wrapper
    return decorate

# -----

# class based decorators
class SpecialClass:
    def __init__(self, argument):
        self.argument = argument
    def __call__(self, func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            print('print decorate start ', self.argument)
            func(*args, **kwargs)
            print('decorate end')
        return decorated


@SpecialClass('Class Based Decorator')
def my_func(*args, **kwargs):
    print(args, kwargs)

my_func([1,2,3], {'one':1})


