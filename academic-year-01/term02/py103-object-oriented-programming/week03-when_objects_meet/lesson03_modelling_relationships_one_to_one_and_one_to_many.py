### Course: Python 103 - Object-Oriented Programming
### Week 09: When Objects Meet
### Lesson 03: modelling Relationships - One-to-One and One-to-Many
### Date: April 27 - 2026

'''In this lesson, we will learn how to model relationships between objects,
specifically one-to-one and one-to-many relationships.'''

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5

    def feed(self):
        print(f"Feeding {self.name}")
        self.hunger = 0

class PetOwner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

owner = PetOwner("Alex")

pet1 = Pet("Luna")
pet2 = Pet("Milo")

owner.add_pet(pet1)
owner.add_pet(pet2)

# Check the pets owned by Alex:
print(f"{owner.name} owns the following pets:")
print(", ".join(pet.name for pet in owner.pets))
print(f"First pet's name: {owner.pets[0].name}")       # Accessing the name of the first pet    

print("--" * 20)
# let's check the hunger level of pet1 before feeding:
print(f"{pet1.name}'s hunger level before feeding: {pet1.hunger}")
owner.pets[0].feed()
print(f"{pet1.name}'s hunger level after feeding: {pet1.hunger}")
