### Course: Python 103 - Object-Oriented Programming
### Topic: Object Identity VS Equality
### Date: April 19 - 2026

# Example to demonstrate the difference between object identity (is) and equality (==)

class Pet:
    def __init__(self, name):
        self.name = name
        
# Create two separate Pet objects with the same name
pet1 = Pet("Oreo")
pet2 = pet1                     # pet2 is an alias for pet1, they refer to the same object
pet3 = Pet("Oreo")              # pet3 is a different object with the same name 

print("Pet1 is Pet2", pet1 is pet2)
print("Pet1 is Pet3", pet1 is pet3)
print("Pet1 name is Pet3 name", pet1.name == pet3.name)

# Change pet1's name and see how it affects pet2 and pet3
pet1.name = "Lucky"

print("Pet1 name:", pet1.name)
print("Pet2 name:", pet2.name)      # pet2 is the same object as pet1, so it reflects the change
print("Pet3 name:", pet3.name)      # pet3 is a different object, so it retains its original name