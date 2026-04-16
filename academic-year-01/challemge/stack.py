### Maestro Challenge
### Topic Stack
### Date: April 15 - 2026

"Build a custom stack data structure with push, pop, and check if the stack is empty."

class Stack:
    def __init__(self):
        '''Initializes an empty stack.'''
        self.items = []
    
    def push(self, item):
        '''Adds an item to the top of the stack.'''
        self.items.append(item)
    
    def pop(self):
        '''Removes and returns the item from the top of the stack.'''
        return self.items.pop()

    def is_empty(self):
        '''Returns True if the stack is empty, False otherwise.'''
        return len(self.items) == 0

# Example usage:
stack = Stack()
stack.push("banana")
stack.push("apple")
stack.push("orange")

print(stack.pop())          # Output: orange
print(stack.pop())          # Output: apple
print(stack.items)          # Output: ['banana']
print(stack.is_empty())     # Output: False
print(stack.pop())          # Output: banana
print(stack.is_empty())     # Output: True