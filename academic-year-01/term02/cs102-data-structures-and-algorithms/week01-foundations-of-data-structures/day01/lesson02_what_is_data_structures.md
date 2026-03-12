### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures
### Date: March 02 - 2026
### lesson 02: What is the data structure?
_________________

1. Core principle

A data structure is a specific way of organizing data so certain actions like:
 - findings, adding, or avoiding duplicates
become easier to use.

2. Why we need data structures?

Because different problems requires different ways of prganizing data.

- In Python:

    - list: when order matters and duplicates allowed
        - Example: sign-up order for an event
            signups = ["Vy", "Alex", "Vy"]   

    - set: when order does not matter and duplicates should be blocked
        - Example: unique usernames or coupon codes
            usernames = {"Vy_01", "coder123", "Vy_01"}     # {"Vy_01", "coder123"}

    - dict: map key and value, need to look things up by a key
        - Example: student name - grade
            grades = {"Vy": 95, "Josh": 88}

3. Insight

If I can look at a problem and say:

 -  “I’ll use a list because order matters and duplicates are allowed.”
 - “I’ll use a set because I only care about uniqueness.”
 - “I’ll use a dict because I need fast lookup by a key.”

then I understand the basic idea of data structures.

    Understanding data structures means choosing the structure that best supports 
    the required operations of a problem.




