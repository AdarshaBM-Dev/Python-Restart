# dictionaries 

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(student)
print(type(student))
print(len(student))
print(student["name"])
print(student.get("age"))
print(student.get("height", "Not Found"))
print(student.keys())
print(student.values())
print(student.items())

student["class"] = "10th" #adding new key-value pair
student["age"] = 21 #updating existing key-value pair   
print(student)  

student.pop("grade") #removing key-value pair by key
print(student)
# del student["class"] #removing key-value pair by key

classroom = {
    "students": ["Alice", "Bob", "Charlie"],
    "teacher": "Mr. Smith",
    "subject": "Math"
} 
print(classroom)


item1 = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 800
}
item2 = {
    "name": "Smartphone",   
    "brand": "Samsung",
    "price": 500
}
items = [item1, item2]
print(items)
print(f"total value :{item1['price'] + item2['price']}")