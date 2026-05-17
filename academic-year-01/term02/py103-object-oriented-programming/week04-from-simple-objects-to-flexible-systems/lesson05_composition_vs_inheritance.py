### Course: Python 103 - Object-Oriented Programming
### Week 10: From Simple Objects to Flexible Systems
### Lesson 04: Composition vs Inheritance: a practical decision rule.
### Date: May 17 - 2026

'''In this lesson, we will discuss the practical decision rule for choosing between 
composition and inheritance when designing our classes. We will see how to apply this rule 
in real-world scenarios to create flexible and maintainable code.'''

# -- Example ---
class Pet:
    def __init__(self, name):
        self.name = name

class PetOwner():
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)
        
# Using composition to create a PetOwner with multiple pets
owner = PetOwner("Vy")
pet1 = Pet("Eiliko")
pet2 = Pet("Emo")
pet3 = Pet("Ebo")

# Adding pets to the owner using composition
owner.add_pet(pet1)
owner.add_pet(pet2)
owner.add_pet(pet3)

# Displaying the owner's pets
print(f"{owner.owner_name} has {len(owner.pets)} pets.")

# Listing the names of the pets
for pet in owner.pets:
    print(pet.name)

