### Course: Python 103 - Object-Oriented Programming
### Week 10: From Simple Objects to Flexible Systems
### Lesson 07: Making objects readable: the __str__ method.
### Date: May 17 - 2026

"""In this lesson, we will learn about the __str__ method, which is a special method 
in Python that allows us to define how an object should be represented as a string. 
We will see how to implement the __str__ method in our classes to make our objects 
more readable and easier to understand when printed."""

# --- Example of __str__ method ---
class Spell:
    def __init__(self, spell_name, power_level):
        self.spell_name = spell_name
        self.power_level = power_level

    def __str__(self):
        return f"Spell '{self.spell_name}' (power level {self.power_level})"

thunderstorm = Spell("Thunder Storm", 8)
print(thunderstorm)

# Output: Spell 'Thunder Storm' (power level 8)

print("\n")
# --- Example of __str__ method with a list of objects ---

class Dragon:
    def __init__(self, name, element, level):
        self.name = name
        self.element = element
        self.level = level

    def __str__(self):
        return f"Dragon '{self.name}' (element: {self.element}, level: {self.level})"   
    
dragons = [Dragon("Smaug", "Fire", 10), Dragon("Fafnir", "Earth", 9), Dragon("Tiamat", "Water", 8)]

for dragon in dragons:
    print(dragon)
    
# Output:
# Dragon 'Smaug' (element: Fire, level: 10)
# Dragon 'Fafnir' (element: Earth, level: 9)
# Dragon 'Tiamat' (element: Water, level: 8)