### Course: Python 103 - Object-Oriented Programming
### Topic: Methods that change object state
### Date: April 21 - 2026

'''In this lesson, we will explore methods that change the state of an object. 
These methods modify the attributes of an object, allowing us to update its information 
after it has been created.'''

class Pet:
    """A class representing a pet."""
    
    def __init__(self, name):  
        """Initialize a pet with a name, hunger level, and happiness level."""
        self.name = name
        self.hunger = 5         # Hunger level from 0 (not hungry) to 10 (very hungry)
        self.happiness = 0      # Happiness level from 0 (sad) to 10 (very happy)                
        
    def feed(self):
        """Feeds the dog, reducing hunger"""
        if self.hunger > 0:
            self.hunger -= 1
            print(f"{self.name} has been fed. Hungeris now : {self.hunger}.")
        else:
            print(f"{self.name} is not hungry.")
            
    def play(self):
        """Plays with the dog, increasing happiness."""
        if self.happiness < 5:
            self.happiness += 1
            print(f"{self.name} is playing. Happiness is now: {self.happiness}.")
        else:
            print(f"{self.name} is already very happy!")
        
# Example usage
pet = Pet("Buddy")

print(f"Before feeding: {pet.hunger}.")
pet.feed()
print(f"After feeding: {pet.hunger}.")
print("-" * 10)
print("Before playing:", pet.happiness)
pet.play()
print("After playing:", pet.happiness)
