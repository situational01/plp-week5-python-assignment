# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name} 💥, my power is {self.power}, and I protect {self.city}!")

    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

# Inherited class
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flying_speed):
        super().__init__(name, power, city)
        self.flying_speed = flying_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flying_speed} km/h ✈️!")

    # show polymorphism
    def attack(self):
        print(f"{self.name} swoops in from the sky and attacks with {self.power}!")

# Creating objects
hero1 = Superhero("Shadow Ninja", "Invisibility", "Tokyo")
hero2 = FlyingSuperhero("SkyFlash", "Lightning Bolts", "New York", 900)

# Using the methods
hero1.introduce()
hero1.attack()

print()  # Just to separate outputs

hero2.introduce()
hero2.fly()
hero2.attack()
