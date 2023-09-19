import requests


class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  

class Human(Pet):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        print(f"{self.name} says: AlsalamuAleikum!")

class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says: Woof! Woof!")

class Cat(Pet):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} says: Meow Meow Nigga!")

wael = Human("Wael", 23)
sully = Dog("Suleyman", "Turkish Pitbull")
silver = Cat("Silver", "Sølv")

# Using object methods
wael.speak()
sully.speak()
silver.speak()
