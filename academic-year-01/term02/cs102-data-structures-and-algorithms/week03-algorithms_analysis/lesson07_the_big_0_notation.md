### CS102: Data structures & algorithms 
### Week 03: Data structures & algorithms
### Date: MMarch - 22 2026
### lesson 07: Introduce the bogOnotation

 
1. What is Big O?

- Big O notation is a way to describe how the number of steps an algorithm needs grows 
    as the input size n  gets bigger.

2. What is n?

- n = size of the input
    - number of items in a list
    - number of cards to sign
    - number of people, etc.
    
3. Common growth rates:
- O(1) – constant time
    - Work basically stays the same, no matter how big n is.
    - Example: getting numbers[0] from a list.

- O(n) – linear time
    - Work grows in proportion to n.
    - Double n → about double the work.
    - Example: loop over each item in a list once.

- O(n^2) – polynomial time
    - Work grows faster than linear.
    - Example idea: everyone in a group shaking hands with everyone else.

- O(2^n) – exponential time
    - Work can double when n increases by 1.
    - Grows very fast, becomes unusable quickly for large n.

4. How to “feel” them (from slowest growth to fastest):
- O(1) → O(n) → O(n^2) → O(2^n)
