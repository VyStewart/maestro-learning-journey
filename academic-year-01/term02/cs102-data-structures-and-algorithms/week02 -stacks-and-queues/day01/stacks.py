### CS102 - Data structures & algorithms 
### Week 02 - Stacks and queues
### Date: March 21 - 2026

# Stack operations: push and pop
books = []
books.append("The Magic of Believing")
print("\n",books)

books.append("The Book of Enoch")
print("\n", books)

books.append("You Are The Way")
print("\n",books)

removed_book = books.pop()
print(f"\nThe removed book is: {removed_book}")
print(f'\nThe collection of books is: {books}')

# Building a stcak using lists
stack = []
stack.append("home")
stack.append("about")
stack.append("contact")

while stack:
    page = stack.pop()
    print("\nPopped:", page)

print("\nFinal stack:", stack)

# Implementing queues wiht deques from the collections module
from collections import deque

ice_cream_line = deque()
ice_cream_line.append("Damien")
ice_cream_line.append("Marcus")
ice_cream_line.append("Josh")
ice_cream_line.append("Sunshine")

served1 = ice_cream_line.popleft()
print("\nServed:", served1)

served2 = ice_cream_line.popleft()
print("\nServed:", served2)

served3 = ice_cream_line.popleft()
print("\nServed:", served3)

served4 = ice_cream_line.popleft()
print("\nServed:", served4)

print("\nFinal Line:", ice_cream_line)
