### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures
### Date: March 15 - 2026
### lesson 06: Updating and replacing array values

Key ideas: updating list elements in Python
- Any elements in a list can be modified using its index
 
- A Python list is mutable → you can change its elements without creating a new list.

- To replace a value, use direct index assignment:
    list_name[index] = new_value

- First element index:
    first_index = 0

- Last element index:
    last_index = len(lst) - 1

- Middle element index (for any length):
    mid_index = len(lst) // 2

- Updating elements this way is an in-place update:
    - the order of elements stays the same (unless you change specific positions)
    - the length of the list does not change

- Valid index rule to avoid errors:
    0 <= index < len(lst)