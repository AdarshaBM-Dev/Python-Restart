class Car:
    def __init__(self, car_id, name, year, price_per_day, status="available", rented_days=0):
        self.car_id = car_id
        self.name = name
        self.year = year
        self.price_per_day = price_per_day
        self.status = status
        self.rented_days = rented_days

    def display_details(self):
        print(f"Car ID: {self.car_id}, Name: {self.name}, Year: {self.year}, Status: {self.status}")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Car ID: {self.car_id} status updated to {self.status}.")

    def calculate_rental_price(self):
        total_price = self.price_per_day * self.rented_days
        print(f"Total rental price for {self.name}: ${total_price}")


# Creating objects
car1 = Car(1, "Swift", 2019, 50)
car2 = Car(2, "Civic", 2020, 60, "rented", 3)
car3 = Car(3, "Mustang", 2021, 80)

# Calling methods
car2.display_details()
car2.calculate_rental_price()
car2.update_status("available")
car2.display_details()


Introduction to OOP Concepts & Classes/Objects
In this video, we will begin our journey into Object-Oriented Programming (OOP) with the foundational concepts of classes and objects.

1. What is Object-Oriented Programming (OOP)?
OOP is a programming paradigm that organizes software design around data, or objects, rather than functions and logic.
It allows for better modularity and code reusability by creating objects that model real-world entities.
Procedural vs Object-Oriented Programming:
Procedural Programming: Based on functions, where the main focus is on performing actions.

Example: Writing multiple functions to process data.
Object-Oriented Programming: Based on objects and classes. The main focus is on objects (data) and the methods (functions) that manipulate this data.

2. Classes and Objects
Class:
A class is a blueprint for creating objects. It defines the attributes and behaviors of the objects created from it.

Object:
An object is an instance of a class. Each object has its own attributes (data) and can perform actions through methods (functions).

Example:
class Car:
    # Attributes
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable

    # Method
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating an object of the class
my_car = Car("Toyota", "Corolla")
my_car.display_info()
Output:

Car Brand: Toyota, Model: Corolla
Here:

Car is the class.
my_car is an object of the Car class.
brand and model are attributes of the object.
display_info() is a method that displays the car's details.
3. Attributes (Instance Variables) and Methods
Attributes: Characteristics that define an object. For example, in the Car class, brand and model are attributes.
Methods: Functions defined inside a class that describe the behaviors of an object.
Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects
person1 = Person("Arjun", 30)
person2 = Person("Megha", 25)

person1.greet()
person2.greet()
Output:

Hello, my name is Arjun and I am 30 years old.
Hello, my name is Megha and I am 25 years old.
In this example:

The Person class defines two attributes: name and age.
The method greet() prints a greeting message using these attributes.
4. Creating Multiple Objects from a Class
One of the main advantages of OOP is that you can create multiple objects from a class, each with its own unique attributes.

Example:
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Creating multiple objects
dog1 = Dog("Rex", "Golden Retriever")
dog2 = Dog("Bolt", "Beagle")

dog1.bark()
dog2.bark()
Output:

Rex is barking!
Bolt is barking!
Here:

dog1 and dog2 are different objects of the Dog class, each with its own name and breed.
