### Course: Python 103 - Object-Oriented Programming
### Week 09: When Objects Meet
### Lesson 02: Reading Objects' State
### Date: April 25 - 2026

'''In this lesson, we will learn how to read the state of an object 
by accessing its attributes.'''

class Pet:
    def __init__(self, name, hunger, energy):
        self.name = name
        self.hunger = hunger
        self.energy = energy

pet = Pet("Milo", 5, 3)
print("BEFORE:")
print(f"name: {pet.name}, hunger: {pet.hunger}, energy: {pet.energy}")

pet.hunger = 2   # Milo ate
pet.energy = 4   # Milo rested

print("AFTER:")
print(f"name: {pet.name}, hunger: {pet.hunger}, energy: {pet.energy}")

