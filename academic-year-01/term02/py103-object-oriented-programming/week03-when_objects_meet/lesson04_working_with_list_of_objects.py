### Course: Python 103 - Object-Oriented Programming
### Week 09: When Objects Meet
### Lesson 04: Working with Lists of Objects
### Date: April 27 - 2026

'''In this lesson, we will learn how to work with lists of objects,
which is a common scenario when we have multiple instances of a class.'''

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greet(self):
        print(f"{self.name} is the {self.species}")

    def play(self):
        print(f"{self.name} is playing.")

pets = [
    Pet("Luna", "dog"),
    Pet("Milo", "cat"),
    Pet("Lucky", "rabbit")
]

# Greet each pet in the list
for pet in pets:
    pet.greet()

# Accessing attributes of each pet in the list
for pet in pets:
    print("-" * 20)
    print(f"Pet name: {pet.name}")
    print(f"Pet species: {pet.species}")

# Let's make each pet play:
print("-" * 20)
for pet in pets:
    pet.play()
    
# Let's find the pet named "Milo" and make it greet:
for pet in pets:
    if pet.name == "Milo":
        pet.greet()
        
print("-" * 20)
# Create another exxample 
class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def roar(self):
        print(f"{self.name} the {self.color} dragon roars!")

dragons = [
    Dragon("Smaug", "red"),
    Dragon("Toothless", "black"),
    Dragon("Luna", "silver")
]

for dragon in dragons:
    print("-" * 20)
    print(f"Dragon name: {dragon.name}")
    print(f"Dragon color: {dragon.color}")
    dragon.roar()