### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures
### Date: March 12 - 2026
### lesson 04: Understanding arrays

1. What an array is (in this course)
 
In Python, we’ll treat a list as our version of an array.

planets = ["Mercury", "Venus", "Earth", "Mars"]

- It’s an ordered collection of items.
- The order matters and is kept.
- Each item has a fixed numeric position called an index.

2. Indexes (positions) — zero-based
 
In Python, indexes start at 0, not 1.
 
For:

planets = ["Mercury", "Venus", "Earth", "Mars"]

The mapping is:

- planets[0] → "Mercury" (1st item)
- planets[1] → "Venus" (2nd item)
- planets[2] → "Earth" (3rd item)
- planets[3] → "Mars" (4th item)
 
So:
 
- “Third item” → index 2
- “Element #3” (if we’re counting from 0) → array[3]

3. Fixed positions (why that matters)
 
Fixed position: once an element is at index i, that index is its “seat number” in the array’s order.
 
Like theater seats:
 
- Seat 0, seat 1, seat 2, seat 3 🎟️

- If "Earth" is at index 2, you always get "Earth" by using planets[2] (unless you later change the list in some other lesson).
 
This is powerful because :
 
- Jump straight to any element by index.

- Think “go to locker #3” → array[3].

4. Arrays vs. “unordered” / key-based structures (high level)
 
- Array/list → ordered, use indexes like 0, 1, 2, 3.

- Other structures (like dicts/sets you may see elsewhere) → 
often use keys or are unordered, not simple 0–N positions.
 
For this lesson, the main contrast is:
 
Arrays/lists care about order + index.

5. Core takeaway

An array (Python list) is an ordered collection where each element lives at a fixed numeric index, starting from 0.
