#list
items = ["Bru","sugar","Milk","Bru"]

print(items)
print(items[0]) #index
items.pop() #last one delete
print(items)   #usine mention delete #items.pop(1)

items.append('biscut')   #add
print(items)

items.remove("sugar")
print(items)

items.insert(1,"spoon")
print(items)

#items.clear()

items[0] = "Coffe powder"  #repacle 
print(items)

print(len(items))

l = [1, 23, 22, 43,11]
print(sorted(l))

sorted_items = sorted(l)    #l.sort()
rev = sorted_items.reverse()

print(sorted_items)

#nested
m = [[1,2], [3,4]]
print(m)

print(type(m))