#tuple and sets

gender = ("male", "female", "others",(1,2,3)) 
print(gender)
print(len(gender))
print(gender[0])
gender[0] = "male v2" #update
print(gender.cout("male v2"))
print(gender.index("male v2"))


#sets
s = {20, 2, 123} #set is unored and un indexd
s2 = set((1, 2, 3))
print(s)
print(type(s2))

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2) #union
print(s & 2)  #intersection
print(s1 - s2)#difference

#methods
s ={1, 2, 3}
s.add(4)
s.remove(10)
s.discard(10) #also remove
a = s.pop() #randum remove
print(a)
s.clear()

