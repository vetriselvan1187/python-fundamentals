
# dictionary examples

d = {'1':1,'2':2,'3':3,'4':4}

print(d['1'])
print(d)

print(d.keys())
print(d.values())

d1 = d.copy()

print('d1 = ', d1)


for k,v in d.copy().items():
    print(k,v)


d1.update({'4':4, '5':5})
print(d1)

print(d1.get('4'))

d1.clear()

print(d1)

d1.update({'12':12, '13':13, '14':14})
d1.pop('13')

print(d1)

d2 = dict.fromkeys((1,2,3,4,5,6,7), 100) # fromkeys(iterable, value)
print(d2)



