### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures
### Date: March 10 - 2026
### lesson 03: Index-based data structures

1. What is an index?
 
An index is a position number in a sequence (like a list).
Python uses zero-based indexing:
1st element → index 0
2nd element → index 1
3rd element → index 2

- Example

seats = ["Anna", "Ben", "Cara", "Diego"]
# index:       0       1       2       3

2. Accessing elements with an index
 
Syntax: list[index]
Using the index in square brackets to get the value at that position.

- Think: index = seat number, element = person in that seat.

3. Direct (index-based) access
 
Direct access = jump straight to an element using its index.

- Example

    seats = ["Anna", "Ben", "Cara", "Diego", "Ella", "Farah"]

    person = seats[4]   # jump directly to index 4 → "Ella"
    print(person)       # Ella

4. Sequential (linear) access
 
Sequential access = visit elements one-by-one in order. 
 
Two common patterns:
 
- By value:
    for person in seats:
        print(person)

- By index:
    for index in range(len(seats)):
        print(index, seats[index])

- You start from the beginning and move step by step:
    - index 0 → index 1 → index 2 → …

- You may pass many elements you don’t care about, but you still step over them.

5. Key difference: index vs sequential
 
- Index-based (direct) access
    - seats[5]
    - Jump straight to position 5.
    - Use when you already know the index.

- Sequential access
    - for x in seats: ...
    - Go one-by-one in order.
    - Use when you want to visit everything or don’t know which index you need yet.

