### Date: 12-18-2025

Ordering Lists — sort() vs sorted()
Key Concepts
-Python provides two ways to order lists: in-place sorting and out-of-place sorting
-Ordering can be customized using key and reverse

list.sort()
-Sorts the list in place
-Modifies the original list
-Return: None
-Use when:
    You want to permanently change the list
    Memory efficiency matters
    You do not need the original order
-Key idea:
    sort() changes the list itself.
    Return None, not a new list

sorted(iterable)
-Returns a new sorted list
-oes not modify the original iterable
-Works on any iterable (lists, tuples, strings, ranges)
-Use when:
    You want to preserve the original data
    You need a temporary ordered version
-Key idea:
    Called as a function: sorted(iterable)
    sorted() produces a new list and leaves the original unchanged.

Sorting with key=len
-tells Python what to sort by
-pass a function that takes 1 item and returns a value to sort on
-key defines how items are compared
-key=len sorts items based on their length, not their values
Common use cases:
    Sorting strings by length
    Ordering lists of collections by size
-Key idea:
    key transforms items before comparison.

Sorting with reverse=True
-Control direction of sort
-Reverses the sorting order
-Works with both sort() and sorted()
-Common use cases:
    Descending order
    Longest-to-shortest sorting
Key idea:
    reverse=True is descending order, flips the final order, not the comparison logic.
    reverse=False(default) is the ascending order

Important Rules to Remember
-sort() modifies the original list; sorted() does not
-sort() returns None; sorted() returns a new list
-key controls comparison logic
-reverse=True controls ordering direction
-Choose based on whether you need to preserve original data

Stability (stable sort)
-Python’s sort is stable
-If two items have the same key value, their left‑to‑right order is preserved

Mental checklist
-need to change the exact list : use .sort()
-need a new sorted list and keep original: use sorted()
-need a custome rule(length, lowercase....): use key=
-need descending: add reserve=True to key=len



