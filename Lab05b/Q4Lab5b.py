#Q4
class Vehicle: 

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

if __name__ == '__main__':
    #1 Check type of an object
    School_bus = Bus("School Volvo", 180, 12)
    print(type(School_bus))
    #2 Determine if School_bus is also an instance of the Vehicle class
    print(isinstance(School_bus, Vehicle))

