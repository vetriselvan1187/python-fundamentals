
# conditional example

#if

age = int(input('Please enter your age : ?'))

if age >= 18:
    print('you are eligible to vote')

print('-------------')


#if else

age  = int(input('Please enter your age : ?'))

if age < 18:
    print('Not eligible to vote')
else:
    print('you are eligible to vote')

print('------------')

# if elif else

age = int(input('Please enter your age : ?'))

if age < 18:
    print('you are minor')
elif age >= 18 and age < 30:
    print('you are young')
elif age >= 30 and age <= 50:
    print('you are not young')
else:
    print('you are old')

print('--------------') 


