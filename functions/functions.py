

# function examples

# function without arguments

def sum_range(start, end):
    sum = 0
    for num in range(start, end):
        sum = sum + num
    return sum

res = sum_range(1, 10)
print(res)
print(sum_range(1, 11))

print('-----------------')




# function with arguments
def repeat_my_name(name, n):
    return n*name

print(repeat_my_name('Mulkin', 10))

print('-----------------')


# function with default arguments

def repeat_your_name(name='Name', n=50):
    return n*name

print(repeat_your_name('Rambo'))

print('--------------------')



# avoid sharing list between subsequent calls

def wrap_my_name(name, list=[]):
    list.append(name)
    return list


def wrap_only_my_name(name, list=None):
    if list is None:
        list = []
    list.append(name)
    return list


print(wrap_my_name('Name1'))
print(wrap_my_name('Name2'))
print(wrap_my_name('Name3'))

print(wrap_only_my_name('Name1'))
print(wrap_only_my_name('Name2'))
print(wrap_only_my_name('Name3'))

print('----------------------------')


# function with positional / arguments
def print_my_pos_details(name, age, /):
    print(name, age)


# function with keyword only arguments
def print_my_kw_details(*, name, age):
    print(name, age)



# function with positional and keyword arguments
def print_my_pos_kw_details(name, age, /, address, *, dept, salary):
    print('{},{},{},{},{}'.format(name, age, address, dept, salary))

print('------------------')


# find my age 
def get_my_age(name, /,  dict):
    if name in dict:
        return dict[name]
    return None

dict = {'Name1':12, 'Name2':13, 'Mulkin':24}

print(get_my_age('Mulkin', dict))
print(get_my_age('Name1', dict))
print(get_my_age('Name44', dict))


print('-----------------')


# calculate total price

shopping_cart_dict={'product1':234.55, 'product2':23.45, 'product3':45.55}

def calculate_total_price(dict):
    total_price = 0.0
    for k,v in dict.copy().items():
        total_price += v
    return total_price

print(calculate_total_price(shopping_cart_dict))

# get list of random numbers

def get_random_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(0, 10))
    return numbers


def calculate_interest_amount(principal, interest):
    return principal*(interest/100)



def get_user_details(age, /, name, *, dept):
    return '{age}, {name}, {dept}'.format(age=age, name=name, dept=dept)


get_user_details(12, 'MyName', dept='tax')

