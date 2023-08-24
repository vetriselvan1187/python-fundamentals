# strings in python


name = 'This is my name' 
about_me = 'I am Myname and I would like to wakeup at 6 A.M, I like'

my_comment = '''
 This is my multiline comment in python,
 It spans through from 1st line to last line.
 I would like to tell more about other things
 by commenting this'''

print(name)
print(about_me)
print(my_comment)


print(name[0]) # first character of my name
print(name[0:5]) # first five char of my name
print(2*name) # print name twice

print(name+name+name) # concat string

# formatting string

print('{}-{}'.format(name, about_me))

my_details = {'name':name, 'age':22, 'dept': 'Tax Department'}

print(my_details)

print('{e[name]}-{e[age]}-{e[dept]}'.format(e=my_details))

# 0[key] to access dict values
print('{0[name]}, {0[age]}, {0[dept]} '.format(my_details))


class Employee:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    

e = Employee(1, 'Name', 22)
print('{e.id}-{e.name}-{e.age}'.format(e=e))



# Template

from string import Template

s = Template('This is my $name and my age is $age')
dict = {'name1' : 'Marco Bakati', 'age' : 34}
print(s.safe_substitute(dict))
print(s.substitute(dict))


