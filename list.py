items = ["Bru","sugar","Milk","bru"]
print(items)
print(items[-1]) #indexing
l = [1, "bru", True, [1,2,3]]
items.pop() #remove last elemenet
items.pop(0)
items.append("good day") #add
items.remove("sugar")
items.insert(1, "spoon")
items.clear()
items = "cffe powder" #replace element

 #slicing

l = [100, 200, 300, 400]
l[0:4]
l[0:3]
l[0:]
l[0::2]
l2 = l[1:3]
print(l2)

print(len(items))
items= [1, 23, 22, 43, 11]

print(sorted(items))
print(sum(items))
print(items.index("bru"))
print(reversed(items))

#matrix
m = [[1,2],[3,4],[[1,2],[1,3]]]
print(m)
