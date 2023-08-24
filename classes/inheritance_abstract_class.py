
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def eat(self):
        print(self.name, ' is eating')
    @classmethod
    @abstractmethod
    def print_cls_args(cls, args):
        pass
    @staticmethod
    @abstractmethod
    def print_static_args(args):
        print(args)    

class Cat(Animal):
    def __init__(self, name, breed, origin):
        super().__init__(name)
        self.breed = breed
        self.origin = origin
    def eat(self):
        print('cat -> ', self.name, ' is eating')
    def print_cls_args(cls,args):
        print(args)
    def print_static_args(args):
        print(args)
    def __repr__(self):
        return '{self.name}-{self.breed}-{self.origin}'.format(self=self)


c = Cat('CatName', 'BreedX', 'Brazil')
c.eat()
c.print_cls_args('2-30405-5')
Cat.print_static_args('static method is called')

