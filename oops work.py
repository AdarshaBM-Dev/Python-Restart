#work:

class Mobile:
    def __init__(self, brand, price ):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"{self.brand} costs {self.price}")

m1 = Mobile("Nokia", 10000)
m2 = Mobile("iPhone", 70000)
m1.display()


m2.display()


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"{self.name} has scored {self.marks} marks")

s1 = Student("Adarsha", 10)
s2 = Student("Krishna", 7)
s1.display_info()
s2.display_info()


class Movie:
    def __init__(self, title, rating ):
        self.title = title
        self.rating = rating

    def display(self):
        print(f"{self.title} rivew {self.rating}")

t1 = Movie("KGF", 10000)
t2 = Movie("Devil", 70000)
t2.display()
t1.display()

class Employee:
    def __init__(self, name, designation, salary=30000):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display(self):
        print(f"{self.name} is {self.designation} - {self.salary}")

e1 = Employee("Adrsha","CEO", 1000000)
e2 = Employee("Devil", "clerk")
e2.display()
e1.display()


#piiler of oops
class BankAccocunt:
    def __init__(self, acc_no, balance):
        self.__acc_no = acc_no
        self.__balance = balance         #privte attribute

    def check_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance<amount:
            print("Insufficiant funds")
            return
        self.__balance -= amount
        print(f"withdraw successfll - Balnce:{self.__balance}")

a = BankAccocunt(acc_no=123, balance=100)
a.check_balance()
a.deposit(100)
a.check_balance()
a.withdraw(1000)
a.withdraw(100)
a.check_balance()



class Phone:
    def take_piture(self):
        #call OS api  o open camara
        #wait for user click
        #proces image
        #store mage in memory
        #return preview
        print("Picture Taken")

p = Phone()
p.take_piture()


#inheritance
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Bike(Vehicle):
    def __init__(self, name):
        self.name = name
    def ride(self):
        print("Riding")
b = Bike("BE")

b.start()
b.ride()



#polimorphishm
class shape:
    def calc_area(self):
        print("Area Calculated")

class Circle(shape):
    def __init__(self, radius):
        self.radius =radius

    def calc_area(self):
        print(f"Area of circle: {(22/7)*self.radius*self.radius}")

class Rectngle(shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calc_area(self):
        print(f"Area of Rectangle: {self.l*self.b}")

c = Circle(5)
r = Rectngle(3,2)

c.calc_area()
r.calc_area()



class Bank_Accout:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, updted_balance):
        if updted_balance<0:
            print("ERRoR: Balance cannot be nagative value")
            return
        self.__balance = updted_balance




class shape:
    def draw(self):
        print("Drawing Shape")

class Circle(shape):
    def draw(self):
        super().draw()
        print("drawing Circle")



from abc import ABC, abstractmethod
class Employee(ABC):
    def calculate_salary(self):
        pass

class Manager(Employee):
    def calculate_salary(self):
        print("Manger's salary is calculated")