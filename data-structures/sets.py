# set 

s = {1,2,3}

s.add(4) # add
s.add(5)
s.add(6)
s.add(7)

print(s)

s.pop() # pop

print(s)

s.remove(6) # remove
s.add(8)
s.add(9)
s.add(10)
print(s)

s.discard(8) # discard

s1 = s.copy()
s.clear()

print(s1)

s2 = {1,3,5,7,9,11,13}

print(s1&s2)
print(s1-s2)
print(s1|s2)
print(s1^s2)


print(s1.issubset({2,3,4,5,7,9,10,11}))
print(s1.issuperset({3,4,5}))









