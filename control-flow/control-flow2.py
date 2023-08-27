
# conditional statments

# break

for i in range(10):
    if i == 5:
        break
    print(i)


print("----------")

# break #2

import random
i = 0
while i < 20:
    if i >= 10:
        break
    i = i + random.randint(1, 3)
    print(i)

print("---------")

# break #3

animal = ['cat', 'rat', 'elephant', 'mouse']

for name in animal:
    if name == 'elephant':
        break
    print(name)


print("-----------")
 
#-----

# continue

for i in range(20):
    if i >= 10 and i <= 15:
        continue
    print(i)


print("-----------")


# pass

# does nothing
#while True:
#    pass

# calling this method would do nothing
def do_nothing_method():
    pass

# empty class
class EmptyClass:
    pass


print("----------")

# Else Clause loops

for i in range(25):
    if(i == 25):
        break
else:
    print('else executed = ', i)


# find prime numbers
for i in range(2, 10):
   for j in range(2, i):
       if i % j == 0:
           break
   else:
       print(i)

 
