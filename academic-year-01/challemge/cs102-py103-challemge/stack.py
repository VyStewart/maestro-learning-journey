### Maestro Challenge
### Topic: Stack
### Date: April 15 - 2026

"Build a custom stack data structure with push, pop, and check if the stack is empty."

class Stack:
    def __init__(self):
        "Initialize an empty stack."
        self.items = []
    
    def push(self, item):
        "Add an item to the top of the stack."
        self.items.append(item)
    
    def pop(self):
        "Remove and return the item from the top of the stack."
        if not self.is_empty():
            '''Add a guard phase to check if the stack is empty before popping.'''
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack.")
    
    def is_empty(self):
        "Check if the stack is empty."
        return len(self.items) == 0
    
# Example usage
stack = Stack()
stack.push("banana")
stack.push("apple")
stack.push("orange")

print(stack.pop())          # Output: orange
print(stack.pop())          # Output: apple
print(stack.items)          # Output: ['banana']
print(stack.pop())          # Output: banana
print(stack.pop())          # Raises IndexError: Pop from an empty stack.
print(stack.is_empty())     # Output: True