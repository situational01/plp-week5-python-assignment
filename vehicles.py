# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚤")

# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat()]

# Polymorphism in action
for v in vehicles:
    v.move()
