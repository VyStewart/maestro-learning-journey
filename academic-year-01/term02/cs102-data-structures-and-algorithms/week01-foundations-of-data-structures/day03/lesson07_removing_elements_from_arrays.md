### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures
### Date: March 15 - 2026
### lesson 07: Removing elements from arrays

1. What pop() does
 
    - pop() removes an element from a list.
    - At the same time, it returns the value it removed.
    - You can use that returned value later (for printing, storing, logic, etc.).

2. Two ways to use pop()
 
    - list.pop()
    → Removes the last element in the list.

    - list.pop(index)
    → Removes the element at that specific index (start, middle, or end).
 
So:
 
- No index → always the last item.
- With index → any item you choose, as long as the index is valid.

3. Index shifts after removal (most important idea)
 
When you remove an element at some index:
 
- All elements to the right of that index move one position left.
- The list becomes shorter by 1.
- The maximum valid index decreases by 1.
- Any indices you remember from before the pop might no longer point to the same elements.

This matters a lot when you:
 
- Do multiple pop operations in a row.
- Use pop first and then later access items by index.
- Compute an index (like “middle”) after removing something.

4. How to think about chained pops

When you see several pop calls one after another:
- Handle them step by step in order.
- After each pop, mentally:

    - Remove that element.
    - Slide everything to the right one step left.
    - Update the indices before looking at the next pop.
