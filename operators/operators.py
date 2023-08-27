
# operators

# boolean operators
# and, or, not

name = "What's in a name?"
print(name)

if 'n' in name and 's' in name:
    print('n and s in name = True')

if 'n' in name or 'z' in name:
    print('n or z in name = True')

if 'k' not in name:
    print('k not in name = True')


# comparison and in operators
# >, >=, <, <=, ==, != , is, is not, in, not in 
 
num1 = 10

if num1 >= 10 and num1 < 20:
    print('ten to twenty')
if num1 <= 30 and num1 > 19:
    print('twenty to thirty')

if num1 == 10:
    print('num1 equals 10')

if num1 != 10:
    print('num1 not equals 10')

num2 = num1
num3 = 20

print(num1 is num2)
print(num1 == num2)
print(num1 is not num2, num1 is not num3)

numbers = [i for i in range(10)]
print(8 in numbers, 8 not in numbers, 12 not in numbers)

print('------------------')

# arithmetic operations

num1 = 100
num2 = 20

print(num1+num2, num1-num2, num1*num2, num1/num2, num1//num2, num1%num2)

print('-------------------')

# bitwise operations ~, |, & , ^, >>, <<

num1 = 10

print('{0:b}'.format(num1))
print('{0:b}'.format(~num1))

num2 = 20

print('{0:b}'.format(num1|num2))
print('{0:b}'.format(num1&num2))
print('{0:b}'.format(num1^num2))

print('{0:d}'.format(num1 << 1))
print('{0:d}'.format(num1 >> 1))


