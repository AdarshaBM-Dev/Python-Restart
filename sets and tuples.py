#tuples
gender = ("male", "female", "other")
print(gender)
print(type(gender))
print(len(gender))
print(gender[0])
print(gender[1])
print(gender[0:2])
print(gender[-1])

#concatenation
tuple1 = (1, 2, 3)  
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

#repetition
tuple4 = ("hello",) * 3
print(tuple4)   
#membership
print("male" in gender)
print("transgender" in gender)
print(gender.index("female"))

#matrix
gender_matrix = (("male", 1), ("female", 2), ("other", 3))
print(gender_matrix)



#SETS
gender_set = {"male", "female", "other"}
print(gender_set) #set is unordered and does not allow duplicates and un indexed
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}  
print(set1 | set2)  #union
print(set1 & set2)  #intersection   
print(set1 - set2)  #difference
print(set1 ^ set2)  #symmetric difference   

set1.add(9)
print(set1) 
set1.remove(2) #remove an element from the set, raises KeyError if not found
set1.discard(3)

set1.pop() #removes and returns an arbitrary element from the set, raises KeyError if the set is empty
a = set1.pop()
print(a)    