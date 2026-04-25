### Course: Python 103 - Object-Oriented Programming
### Week 09: When Objects Meet
### Lesson 01: Many Objects, One Class
### Date: April 25 - 2026

'''In this lesson, we will explore how to create multiple objects from the same class.'''

class Pet:
    """A class representing a pet."""
    
    def __init__(self, name):  
        """Initialize a pet with a name, hunger level, and happiness level."""
        self.name = name   # Hunger level from 0 (not hungry) to 10 (very hungry)
        self.happiness = 50      # Happiness level from 0 (sad) to 10 (very happy)                
              
    def play(self):
        """Plays with the dog, increasing happiness."""
        self.happiness += 10
            
pet1 = Pet("Lucky")
pet2 = Pet("SHadow")

pet1.play()
pet1.play()
pet2.play()

print(pet1.name, "happiness:", pet1.happiness)
print(pet2.name, "happiness:", pet2.happiness)

print("-" * 20)
# Create another example class and objects
class Car:
    def __init__(self):
        self.fuel = 100

    def drive(self):
        self.fuel -= 30

car1 = Car()
car2 = Car()

car1.drive()

print("car1 fuel:", car1.fuel)
print("car2 fuel:", car2.fuel)
