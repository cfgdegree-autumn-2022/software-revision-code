"""
REVISION TASK

1. Design a parent class Vehicle
    - Store the make and colour of the vehicle
    - Have a method called driving (where we’ll say by default it’s on 4 wheels)
2. Design a child class of Vehicle called Motorcycle
    - Needs to override driving (2 wheels)
    - Create a new method called coolFactor
3. Design a child class of Vehicle called Unicycle
    - Needs to override driving (1 wheel)
    - Create a new attribute - antique
    - Create a new method called coolFactor
"""


class Vehicle():
    def __init__(self, make, colour):
        self.make = make
        self.colour = colour

    def driving(self):
        return f"I drive in a {self.colour} {self.make} on 4 wheels "

class Motorcycle(Vehicle):
    def driving(self):
        return f"I drive in a {self.colour} {self.make} on 2 wheels "

    def coolFactor(self):
        return "I am very cool"

class Unicycle(Vehicle):
    def __init__(self, make, colour, antique):
        super().__init__(make, colour)
        self.antique = antique

    def driving(self):
        return f"I drive in a{'n old' if self.antique else ' new'} {self.colour} {self.make} on 1 wheel"

    def coolFactor(self):
        return "An incomparable level of cool"

Vehicle1 = Vehicle("Honda", "White")
Vehicle2 = Motorcycle("Honda", "White")
Vehicle3 = Unicycle("Honda", "White", False)

print(Vehicle1.driving())
print(Vehicle2.driving())
print(Vehicle3.driving())

