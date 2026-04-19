### Maestro Challenge
### Topic: Class and Instance Attributes
### Date: April 19 - 2026


"""
Practice session to master key Python OOP concepts:
- Understand difference between class and instance (object)
- Create and use class and instance attributes
- Build classes with constructors (__init__)
- Track class-wide data vs object-specific data
- Validate and update object state
- Correctly use equality (==) vs identity (is)
- Debug common bugs with shared mutable class attributes
This prepares for review questions about writing and reasoning with classes, objects, and attributes.
"""

class Student:
    """A class representing a student, tracking name, age, 
    and class-wide total count."""
    
    total = 0

    def __init__(self, name, age):
        """
        Initialize a student with a name and age.
        If the given age is negative, sets age to 0.
        Increments the total student count.
        """
        if age < 0:
            self.age = 0
        else: 
            self.age = age
        self.name = name 
        Student.total += 1

    def greet(self):
        """Prints a greeting with the student's name and age."""
        print(f"Hi, I'am {self.name}, and I'm {self.age} yrs.")
        
# Example usage
student1 = Student("Dana", -3)
student2 = Student("Lee", 20)

student1.greet()
student2.greet()
print(Student.total)
        