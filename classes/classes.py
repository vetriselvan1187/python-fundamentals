
# classes

# Person class
class Person:
    classname='Person'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_my_name(self):
        return self.name
    def get_my_age(self):
        return self.age
    def __repr__(self):
        return '{self.name}-{self.age}'.format(self=self)
    def get_classname(cls):
        return cls.classname
    def get_static_classname():
       return Person.classname




# inheritance

class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(self.name, ' is walking')

    def eat(self):
        print(self.name, ' is eating ')


class Cat(Animal):
    classname='Cat'

    def __init__(self, name, breed, coat_pattern, origin):
        super().__init__(name)
        self.breed = breed
        self.coat_pattern = coat_pattern
        self.origin = origin

    def __repr__(self):
        return '{0}-{1}-{2}-{3}'.format(self.name, self.breed, self.coat_pattern, self.origin)


class Monkey(Animal):
     classname='Monkey'

     def __init__(self, name, group):
         super().__init__(name)
         self.group = group

     def __repr__(self):
         return '{0}-{1}'.format(self.name, self.group)


class Dog(Animal):
     classname='Dog'

     def __init__(self, name, breed):
         super().__init__(name)
         self.breed = breed

     def __repr__(self):
         return '{0}-{1}'.format(self.name, self.breed)




