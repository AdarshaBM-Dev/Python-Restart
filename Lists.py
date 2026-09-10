#lists

items = ["apple", "banana", "cherry"]
print(items) #print all items in the list
items.append("orange") #add "orange" to the end of the list
print(items)    
items.remove("banana") #remove "banana" from the list
print(items)
items.insert(1, "kiwi") #insert "kiwi" at index 1
print(items)
items.sort() #sort the list in ascending order
print(items)
items.reverse() #reverse the list
print(items)
items.pop() #remove the last item from the list
print(items)
print(items[0]) #print the first item in the list
print(items[1:3]) #print items at index 1 and 2
print(len(items)) #print the length of the list
print("kiwi" in items) #check if "kiwi" is in the list
items[0] = "grape" #change the first item in the list to "grape"
print(items)

#slicing
numbers = [1, 2, 3, 4, 5]
print(numbers[0:3]) #print items at index 0, 1, and 2
print(numbers[:3]) #print items from the beginning to index 2
print(numbers[2:]) #print items from index 2 to the end
print(numbers[0:3:2]) #print items at index 0 and 2
print(numbers[::2]) #print every second item in the list
print(numbers[::-1]) #print the list in reverse order
print(numbers[-1]) #print the last item in the list
print(numbers[-3:-1]) #print items at index -3 and -2
print(numbers[-3:]) #print items from index -3 to the end
print(numbers[:-3]) #print items from the beginning to index -4
print(numbers[-1:-4:-1]) #print items at index -1, -2, and -3 in reverse order
print(numbers[-4:-1]) #print items at index -4, -3, and -2


#nested list 
m = [[1,2],[3,4],[5,6]]
print(m[0]) #print the first sublist    
print(m)
print(m[1][0]) #print the first item of the second sublist



print(type(items)) #print the type of the list