### Date: 12-18-2025
## Day 4 — Mastering List Iteration & Common List Methods & 

Key Concepts Learned
-Lists can be traversed using index-based or value-based loops
-Index-based loops iterate over positions in a list
-Value-based loops iterate directly over list values
-Lists are mutable, allowing items to be added, removed, or modified
-Common list methods support controlled list modification

Important Rules to Remember
Iteration
-Use index-based loops when you need to modify list items or track positions
-Use value-based loops when you only need to read or inspect values
-Index-based loops provide more control but require boundary awareness
-Value-based loops are more readable and robust

Common List Methods
-append(item) adds one item to the end of a list
    Return: None
    To grow the list by one at the tail

-insert(index, item) adds an item at a specific position
    Shifts items at/after that index to the right
    Use when positions matter

-remove(value) deletes the first matching value
    Looks for value, not an index
    If the value is not found, it raise an error
    Use when to know the value to get rid of

-pop(index) removes an item by index (or the last item by default) and return it
    Removes by index and return the value
    If call pop() with no index, it removes and returns the last item
    Use when the position and the removed value matter

-extend(iterable) adds multiple items from another collection
    Unpack and adds a list as separate items
    Grows the list by each elements of the iterable
    Use to merge another sequence to the existing list

Key distinction:
-Some methods work by value (remove)
-Some methods work by position (insert, pop)
- All of these methods modify the original list instead of making a new one.

Short Reflection
Today I learned how to iterate through lists intentionally and how to modify them using built-in list methods. I understand when to choose index-based versus value-based loops and how methods like append, insert, and pop help manage list structure safely and clearly. This helped me think more deliberately about how data changes over time.
