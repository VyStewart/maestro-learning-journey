### Course: Python 103 - Object-Oriented Programming
### Topic: Methods that Use Object State
### Date: April 21 - 2026

class Dog:
    """A class representing a dog, tracking name and age."""
    
    def __init__(self, name, age):
        """Initialize a dog with a name and age."""
        self.name = name
        self.age = age

    def describe(self):
        """Prints a short description of this dog."""
        print(f"{self.name} is {self.age} years old.")  
        
    def get_discription(self):
        """Returns a string description of this dog."""
        return f"{self.name} is {self.age} years old."
    
# Example usage
dog1 = Dog("Buddy", 5)
dog1.describe()                 # use print inside the function to print the description directly
text = dog1.get_discription()   # method returns a string, so we can store it in a variable and print it later
print(text)                     # main program prints the description returned by the method

print("-" * 20)

# Create another expample class and object methods.
class Book:
    """A class representing a book, tracking title and author."""
    
    def __init__(self, title, author):
        """Initialize a book with a title and author."""
        self.title = title
        self.author = author

    def info (self):
        """Prints basic info about this book."""
        print(f"'{self.title}' by {self.author}.")  
        
    def get_info(self):
        """Returns a string with basic info about this book."""
        return f"'{self.title}' by {self.author}."  
        
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book1.info() 
text = book1.get_info()
print(text)                    

