# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100
    

# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage, capacity)

    def __str__(self):
        return "{ max speed: " + str(self.max_speed) + ", mileage: " + str(self.mileage) + "}"


class Car(Vehicle):
    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage, capacity)
    def __str__(self):
        return "{ max speed: " + str(self.max_speed) + ", mileage: " + str(self.mileage) + "}"
    def fare(self):
        return "Car: " + str(self.capacity * 100)
    
b = Bus(120, 20, 20)
c = Car(180, 25, 5)

for vehicle in (b, c):
    print(vehicle.fare())