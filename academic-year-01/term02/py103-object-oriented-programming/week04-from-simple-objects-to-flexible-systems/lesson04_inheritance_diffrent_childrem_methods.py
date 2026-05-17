### Course: Python 103 - Object-Oriented Programming
### Week 10: From Simple Objects to Flexible Systems
### Lesson 04: Inheritance - Different Child Classes, Different Methods
### Date: May 17 - 2026

'''In this lesson, we will see how different child classes can have different methods,
even though they inherit from the same parent class. This allows us to create more 
specific behaviors for each subclass while still sharing common functionality from the parent class.'''

# --- Parent class ---
class Pet:
    def speak(self):
        print("The pet makes a sound.")

class Dog(Pet):
    def speak(self):
        """Dog speaks by barking."""
        print("Woof!")

    def fetch(self):
        print("Dog is fetching the ball!")

class Cat(Pet):
    def speak(self):
        """Cat speaks by meowing."""
        print("Meow!")

# --- Using the subclasses ---
generic = Pet()
buddy = Dog()
whiskers = Cat()

#--- Testing the speak method for each class ---
generic.speak()
buddy.speak()
buddy.fetch()
whiskers.speak()