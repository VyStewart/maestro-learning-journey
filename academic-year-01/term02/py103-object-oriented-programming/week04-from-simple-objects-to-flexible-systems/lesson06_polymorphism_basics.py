### Course: Python 103 - Object-Oriented Programming
### Week 10: From Simple Objects to Flexible Systems
### Lesson 06: Polymorphism Basics: one action, different behaviors.
### Date: May 17 - 2026

'''In this lesson, we will learn about polymorphism, which is the ability of different 
classes to be treated as instances of the same class through inheritance. 
We will see how polymorphism allows us to write code that can work with 
objects of different classes as long as they share a common interface.'''

# --- Example of Polymorphism ---
class Printer:
    def run(self):
        print("the printer prints the documnet.")

class Scanner:
    def run(self):
        print("the scanner scans the document.")

office_machines = [Printer(), Scanner()]

for machine in office_machines:
    machine.run()
