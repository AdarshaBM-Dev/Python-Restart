def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    print("\n===== MENU =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting program...")
        break

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))

    else:
        print("Invalid choice! Please select between 1-5.")




class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: ₹{self.balance}")


# Create Account
name = input("Enter Account Holder Name: ")
account = BankAccount(name)

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using our bank system!")
        break

    else:
        print("Invalid choice! Please select 1-4.")






class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")


students = []

while True:
    print("\n===== STUDENT MENU =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        student = Student(roll, name, marks)
        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for student in students:
                student.display()

    elif choice == "3":
        roll = input("Enter Roll No to search: ")
        found = False
        for student in students:
            if student.roll_no == roll:
                student.display()
                found = True
                break
        if not found:
            print("Student not found!")

    elif choice == "4":
        roll = input("Enter Roll No to delete: ")
        for student in students:
            if student.roll_no == roll:
                students.remove(student)
                print("Student deleted successfully!")
                break
        else:
            print("Student not found!")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")







class Car:
    def __init__(self, car_id, name, year, price_per_day):
        self.car_id = car_id
        self.name = name
        self.year = year
        self.price_per_day = price_per_day
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Rented"
        print(f"ID: {self.car_id}, Name: {self.name}, Year: {self.year}, "
              f"Price/Day: ₹{self.price_per_day}, Status: {status}")


cars = []

while True:
    print("\n===== CAR RENTAL MENU =====")
    print("1. Add Car")
    print("2. View Cars")
    print("3. Rent Car")
    print("4. Return Car")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        car_id = input("Enter Car ID: ")
        name = input("Enter Car Name: ")
        year = input("Enter Year: ")
        price = float(input("Enter Price per Day: "))
        car = Car(car_id, name, year, price)
        cars.append(car)
        print("Car added successfully!")

    elif choice == "2":
        if not cars:
            print("No cars available.")
        else:
            for car in cars:
                car.display()

    elif choice == "3":
        car_id = input("Enter Car ID to rent: ")
        for car in cars:
            if car.car_id == car_id:
                if car.is_available:
                    car.is_available = False
                    print("Car rented successfully!")
                else:
                    print("Car already rented!")
                break
        else:
            print("Car not found!")

    elif choice == "4":
        car_id = input("Enter Car ID to return: ")
        for car in cars:
            if car.car_id == car_id:
                if not car.is_available:
                    car.is_available = True
                    print("Car returned successfully!")
                else:
                    print("Car was not rented!")
                break
        else:
            print("Car not found!")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
