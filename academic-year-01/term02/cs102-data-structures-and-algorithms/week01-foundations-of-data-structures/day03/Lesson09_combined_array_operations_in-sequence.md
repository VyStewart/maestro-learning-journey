### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures
### Date: March 15 - 2026
### lesson 09: Updating and replacing array values

1. Python lists & operation order
 
- Always be clear about the order of operations on a list:
    - 1)Access → 2) Update → 3) Remove

- Changing the list (update/remove) can shift indexes, so the order you do things really matters.

2. Access (read only)
 
- Access is just looking at a value in the list using an index.
- Access does not change the list.
- Often you store the accessed value in a variable or print it, but the list stays the same.

3. Update (mutation)
 
- Updating means changing the value at a specific index.
- After an update, the list has the same length, but one element’s value is different.
- You need a valid index; otherwise, Python raises an error.

4. Remove with pop (mutation + return)
 
- pop(index) does two things at once:
    - It removes the item at that index from the list (the list gets shorter).
    - It returns the removed value so you can store it.

- This is different from other operations that only mutate without returning anything.

5. Functions that both mutate and return
 
- A function can:
    - change a list that was passed in (mutate it),
    - and return useful information about what it did.

- Example pattern you used:
    - Do one or more operations on the list (access, update, remove).
    - Return:
        - the removed item, and
        - the final list.

6. Returning multiple values (tuples)
 
- In Python, a function can “return multiple values” by returning a tuple.
- Conceptually:
    - The function “packs” several values into a tuple.
    - The caller “unpacks” them into separate variables.

7. Tuple unpacking at the call site
 
- When a function returns multiple values:
    - The right side is the function call that returns a tuple.
    - The left side is a comma‑separated list of variables that receive each element.

- The number of variables on the left must match the number of values returned.

8. Key mental models from this lesson
 
- “First look, then change, then delete” when combining operations on a list.
- “A function can both change the list and tell you what it changed via its return values.”
- “Multiple return values in Python = tuple + unpacking, not multiple return lines.”
