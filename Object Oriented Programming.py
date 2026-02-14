class Car:
    def __init__(self ,car_id, name, year, price_per_day, status="avilable=0", rented_days=0):
        self.car_id = car_id
        self.name = name
        self.year = year
        self.price_per_day = price_per_day
        self.status = status
        self.rented_days = rented_days

        def display_details(self):
            print(f"Car ID: {self.car_id},Name: {self.name}, year: {self.year}, status: {self.status} ")

        def update_status(self, new_status):
            self.status = new_status
            print(f"Car ID: {self.car_id}, status updated to {self.status}. ")

        def calculate_rental_price(self):
            total_price = self.price_per_day * self.rented_days
            print(f"Total rental price for {self.name}: $(total_price)")

    car1 = Car(1, "Swift", 2019, 50)
    car2 = Car(2, "Civic", 2020, 60, "rented", 3)
    car3 = Car(3, "Mustang", 2021, 80)

    car2.display_deatails()
    
    car2.calculate_rental_price()

    car2.update_status("available")
    car2.display_detils()