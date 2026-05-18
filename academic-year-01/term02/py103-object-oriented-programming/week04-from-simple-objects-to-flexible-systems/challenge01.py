### Course: Python 103 - Object-Oriented Programming
### Week 10: From Simple Objects to Flexible Systems
### Challenge 01: Building a tiny Mini-Zoo Manager with OOP.
### Date: May 17 - 2026

"""In this challenge, you will apply the concepts of object-oriented programming to build 
a tiny Mini-Zoo Manager."""

"""
a base Animal class
a couple of subclasses
encapsulation with getters/setters
overriding methods
a list of mixed animals that all respond to the same method
a __str__ method to make the animals readable when printed 
"""  
# Create a base Animal class
class Animal:
    def __init__(self, name, species, health):
        self._name = name
        self._species = species
        self._health = 0
        self.set_health(health)
        
# Encapsulation with getters and setters
    # Getters and setters for name, species, and health
    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_health(self):
        return self._health
    
    # Setter for health with validation
    def set_health(self, new_health):
        if new_health < 0:
            self._health = 0

        elif new_health > 100:
            self._health = 100

        else:
            self._health = new_health
            
    # Method to interact with the animal (to be overridden in subclasses)
    def interact(self):
        # TODO: this will be overridden in subclasses
        pass

    # Method to display animal information when printed
    def __str__(self):
        return f"{self.get_name()} the {self.get_species()} (health: {self.get_health()})"

# Subclasses for different types of animals
class Dog(Animal):
    def interact(self):
       print(f"{self.get_name()} the {self.get_species()} wags its tail! (health: {self.get_health()})")

class Cat(Animal):
    def interact(self):
        print(f"{self.get_name()} the {self.get_species()} purrs softly. (health: {self.get_health()})")

# Create a list of mixed animals that all respond to the same method
dog1 = Dog("Buddy", "Dog", 80)
cat1 = Cat("Misty", "Cat", 60)
print(dog1)
dog1.interact()
print(cat1)
cat1.interact()

# Create a list of mixed animals that all respond to the same method
animals = [dog1, cat1]

print("-" * 20)
for animal in animals:
    print(animal)
    animal.interact()