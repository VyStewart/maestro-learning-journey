### Maestro Challenge
### Topic: Combining core programming skills to solve a multi-step, real-world problem
### Date: April 17 - 2026

"""
stack duplicates finder practice challenge

Practice challenge combining duplicate detection and stack usage.

- Finds duplicate numbers in a list
- Pushes only unique numbers onto a custom Stack class
- Demonstrates stack operations (push, pop, view items)

This code shows how to blend data cleaning and classic data structure skills to solve a multi-step programming problem.
"""

numbers = [101, 103, 203, 101, 405, 106, 108, 103, 369, 106, 93, 80]

def find_duplicates(numbers):
    "Return a list of duplicates from the input list."
    seen = []
    duplicates = []
    
    for num in numbers:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen.append(num)
            
    return duplicates

duplicates = find_duplicates(numbers)
print("Duplicate numbers:", duplicates)         # Output: Duplicate numbers: [101, 103]

class Stack():
    
    def __init__(self):
        "Initialize an empty stack."
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        '''Add a guard phase to check if the stack is empty'''
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack.")

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
for num in numbers:
    if num not in duplicates:
        stack.push(num)

print("Unique numbers:", stack.items)
print("Removed number:", stack.pop())
print("Removed number:", stack.pop())
print("Remaining in stack:", stack.items)