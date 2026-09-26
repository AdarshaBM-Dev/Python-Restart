#list
items = ["apple", "banana", "cherry"]
print(items)
print(items[0])
print(items[1])
print(items[2])

l = [1, "hello", 3.14, True] 
print(l)
print(l[0])

items.pop(0)
print(items)

items.append("orange")
print(items)    

items.insert(1, "kiwi")
print(items)

items.remove("banana")
print(items)

items[0] = "grape"
print(items)

#slicing
print(items[0:2])   
print(items[1:])
print(items[:2])
print(items[-2:])
print(items[-3:-1])
print(items[::2])
print(items[::-1])  
print(items.index("kiwi"))

print(len(items))
print(max(items))
print(min(items))
print(sum([1, 2, 3, 4, 5]))
print(sorted(items))
print(items.count("kiwi"))


#matrix
print("matrix")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])

