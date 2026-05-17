### Course: Python 103 - Object-Oriented Programming
### Week 10: From Simple Objects to Flexible Systems
### Lesson 01: Encapsulation - Owning Object State
### Date: May 10 - 2026

'''In this lesson, we will learn about encapsulation, 
which is the concept of owning an object's state and controlling access to it.'''

# Let's create a simple Book class to represent a book with title and pages

class Book:
    """A simple Book class that represents a book with a title and number of pages."""
    def __init__(self, title, pages):
        self.title = title
        self._pages = pages
        
    '''The _pages attribute is intended to be private, 
    and we will provide a method to access it.'''
    def get_pages(self):
        """Returns the pages from Book"""
        return self._pages
    
#-------Main program-------
# Let's create a book object and access its pages using the get_pages method.
book = Book("You Are The Way", 258)

print(f"The book {book.title} has {book.get_pages()} pages.")