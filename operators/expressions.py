
# expressions

# ., [], [:], (), :=, lambda

numbers = [1, 2, 3, 4, 5]
numbers.append(6) # .
print(numbers[0])
print(numbers[:])

five = int(5) # ()

# :=
import re
pattern = re.compile('^k')
data = 'keep this product away from children'
if match := pattern.search(data):
    print('match exists = ', match)
else:
    print('no pattern match for this data')


# lambda

f = lambda x : x*2
[f(i) for i in numbers]

# 

