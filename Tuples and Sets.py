#Tuples and Sets

genders = ("male","female","others",(1,2,3))

print(genders)
print(type(genders))
print(genders.count("male"))
print(genders.index("male"))

#sets
s = {20, 2, 123}
s2 = {(1, 2, 3)}
print(s) #set is unordered ,un index, uniq
print(s2)
print(type(s2))

s3 = {1, 2, 3}
s4 = {3, 4 ,5}
print(s3 | s4)  #union
print(s3 & s4)  #intersection
print(s3 - s4)  #difference

s5 = {1, 2, 3}

s5.add(4)
s5.discard(10)
s5.pop()
a = s.pop()
print(a)
print(s5)