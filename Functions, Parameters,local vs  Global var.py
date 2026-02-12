# def greet():
#     print("Hello, Good morning!")

# greet()



# def marriage(boy, girl):  #parameters
#     print(f"Boy is {boy}")
#     print(f"Girl is {girl}")
#     print(f"{boy} married {girl}")

# marriage("Adarsha", "Ranjitha") #positional arguments



# def tables(num):
#     for i in range(1,11):
#         print(f"{num}X{i}={num*i}")

# tables(4)



# def marriage(boy, girl= "Girl"):
#     print(f"Boy is {boy}")
#     print(f"Girl is {girl}")
#     print(f"{boy} married {girl}")

# marriage("Adarsha")



# def func(num):
#     return int(str(num)*5)

# a = 100
# b = func(1)
# c = a + b 
# print(c)


def func():
    x = "adarsh" #local varible
    print("hello world")
    print(y)

y="amith" #global variable


1. Basics of Functions
A function is a reusable block of code that performs a specific task when called. Functions are useful to organize code, make it reusable, and reduce redundancy.

2. Defining a Function
You define a function using the def keyword followed by the function name, parentheses, and a colon :.

Syntax:
def function_name(parameters):
    # Block of code
Example: Basic function to greet a user
def greet():
    print("Hello! Welcome to the Python course.")
greet()
Output:

Hello! Welcome to the Python course.
3. Function Parameters
Parameters are variables used to pass data into a function.

Example: Function with a parameter
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python course.")

greet_user("Anand")
Output:

Hello, Anand! Welcome to the Python course.
4. Returning Values from a Function
A function can return a value using the return keyword, which allows the output of the function to be reused elsewhere.

Example: Function that adds two numbers and returns the result
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("The sum is:", result)
Output:

The sum is: 30
5. Default Parameter Values
You can define a default value for a parameter, which is used if no argument is passed when the function is called.

Example: Function with a default parameter
def greet(name="Student"):
    print(f"Hello, {name}! Welcome to the Python course.")

greet()  # Uses default value "Student"
greet("Geetha")  # Uses passed value "Geetha"
Output:

Hello, Student! Welcome to the Python course.
Hello, Geetha! Welcome to the Python course.
Here are the sections for Nested Functions and Local/Global Variables:

6. Local and Global Variables
Local Variables are defined inside a function and are only accessible within that function.
Global Variables are defined outside all functions and are accessible from anywhere in the code.
Example: Local vs Global variables
name = "Global Name"

def greet():
    name = "Local Name"
    print(name)

greet()  # Prints local variable
print(name)  # Prints global variable
Output:

Local Name
Global Name
In this example, the local variable name inside the function does not affect the global variable name.

