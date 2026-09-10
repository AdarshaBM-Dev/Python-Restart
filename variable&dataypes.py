#VARIABLES AND DATA TYPES

a = 5
b = 10
print(a)
print(a+b)

a, b, c, d = 1, 2, 3, 4
print(a, b, c, d)

a = b = c = 5
print(a, b, c)

name = "John"
print(name)

is_student = True
print(is_student)

name = ("Adarsha")
Name = ("Krishna")
print(name)

name = "Krishna" #string  
age = 23 #integer
is_student = True #boolean
weight = 70.5 #float
print("Name:", name)
print("Age:", age)
print("Is Student:", is_student)
print("Weight:", weight)
print("Data type of name:", type(name))
print("Data type of age:", type(age))
print("Data type of is_student:", type(is_student))
print("Data type of weight:", type(weight))

#Data type conversion dynamically
age = str(age) #converting integer to string
print("Age:", age)
print("Data type of age:", type(age))
is_student = "yes" #string
print("Is Student:", is_student)
print("Data type of is_student:", type(is_student))

#ARITH MATIC OPERATORS
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)
print("Data type of x:", type(x))
print("Data type of y:", type(y))
print("Data type of x/y:", type(x/y))
print("Data type of x//y:", type(x//y))

#SWAPING VARIABLES
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)
print("After swapping: a =", b, ", b =", a)
print("Before swapping: a =", a, ", b =", b)
