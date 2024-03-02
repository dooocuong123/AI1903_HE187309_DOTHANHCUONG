#Q1
#1 Creating a list in PythonCreate a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car = Vehicle(240, 18)
print(car.max_speed, car.mileage)
#2 Create a Vehicle class without any variables and methods
class Vehicle:
    pass

car = Vehicle()
