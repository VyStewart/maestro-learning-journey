### Course: Python 103 - Object-Oriented Programming
### Week 10: From Simple Objects to Flexible Systems
### Lesson 03: Keeping it in the family - Introducing Inheritance
### Date: May 17 - 2026

'''In this lesson, we will learn about inheritance, which is a fundamental concept 
in object-oriented programming that allows us to create new classes 
based on existing ones.'''

# --- Parent class ---
class Pet:
    """A basic pet that can be fed and can speak."""
    
    def speak(self):
        """Make the pet speak."""
        print("The pet makes a sound.")
    
    def feed(self):
        """Feed the pet."""
        print("You feed the pet.")


# --- Subclass ---
class Dog(Pet):
    """A dog that is a kind of pet."""
    pass

class Cat(Pet):
    """A dog that is a kind of pet."""
    pass

# --- Using the subclass ---
my_dog = Dog()
my_dog.feed()
my_dog.speak()

print("-" * 10) 
my_cat = Cat()
my_cat.feed()
my_cat.speak()