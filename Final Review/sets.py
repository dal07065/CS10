#sets
#no duplicates, not in order, mutable

#--------------------------------#
intSet = {1, 2, 3}
intSet2 = set("abac")

#{'a,' 'b', 'c'}

#--------------------------------#

my_set = set('one two three')
your_set = set(['one', 'two', 'three'])
print(my_set)
print(your_set)

#{' ', 'w', 'n', 'h', 'o', 'r', 'e', 't'}
#{'one', 'two', 'three'}

#--------------------------------#
a_set = {'a', 'b', 'c', 'd'}
b_set = {'c', 'd', 'e', 'f'}

#--------------------------------#
c_set = a_set & b_set
# c_set = b_set & a_set
# c_set = a_set.intersection(b_set)
# c_set = b_set.intersection(a_set) 
print(c_set)

## {'c', 'd'}

#--------------------------------#

c_set = a_set | b_set
# c_set = b_set | a_set
# c_set = a_set.union(b_set)
# c_set = b_set.union(a_set) 
print(c_set)

## {'a', 'b', 'c', 'd', 'e', 'f'}

#--------------------------------#

c_set = a_set - b_set
# c_set = a_set.difference(b_set)
print(c_set)

## {'a', 'b'}

#--------------------------------#

c_set = b_set - a_set
# c_set = b_set.difference(a_set)
print(c_set)

## {'e', 'f'}

#--------------------------------#

c_set = a_set ^ b_set
# c_set = b_set ^ a_set
# c_set = a_set.symmetric.difference(b_set)
# c_set = b_set.symmetric.difference(a_set)
print(c_set)

## {'a', 'b', 'e', 'f'}

