# tuple

genders = ("male", "female", "other")
print(genders)
print(type(genders))
print(len(genders))
print(genders[0])
print(genders[1:3])

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

repeated_tuple = (1, 2) * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

# print("apple" in fruits)  # Output: True

#sets 

s = {20, 2, 123} # set is  unordered collection of unique elements and  un indexed
print(s)

s2 = set((1, 2, 3))
print(s2)
print(type(s2))

#set  operations
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5, 6}
print(s1.intersection(s2))  # Output: {3, 4}
print(s1.difference(s2))  # Output: {1, 2}
print(s2.difference(s1))  # Output: {5, 6}
print(s1 | s2) #union
print(s1 & s2) #intersection 
print(s1 - s2) #difference
print(s1 ^ s2) # symmetric difference 

# set  methods 

x =  {1, 2, 3}
x.add(4)
x.remove(2)
x.discard(10) 
x.pop(0)
x.clear()