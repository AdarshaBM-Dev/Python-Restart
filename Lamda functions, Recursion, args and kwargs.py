# def add(a, b):
#     return a+b

# c= add(1, 2)
# print(c)


# def add(*numbers):
#     return sum(numbers)

# print(add(1,100,1))

# def student_info(**details):   #keyword arguments
#     for key, value in details.items():
#         print(f"{key}:{value}")

# student_info(name="Anand", age=22, course="Python")


# add = lambda a,b : a+b
# print(add(1,2))

# double = lambda x: 2*x
# print(double(200))


# def factorial(n):
#     if n==1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(3))

def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    def div():              
        print(a/b)
    add()   
    sub()
    mul()
    div()
calculate(10,5)