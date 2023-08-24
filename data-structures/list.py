
# list data strucutures

l = []
l.append(1) # append
l.append(2)
l.append([3, 4, 5])

print(list)

l1 = l.copy()  # copy
print(id(l), id(l1))

l.append(66)
l.remove(1)   # remove
l.extend([22,33,44,55]) # extend

print(l)
print(l.index(22)) # index
l.pop()  # pop
l.remove([3,4,5]) # remove

l.sort() # sort
print(l)

l.reverse() # reverse
print(l)

print(l.count(2)) # count
l.insert(0, 12) # insert
print(l)

l.clear()



