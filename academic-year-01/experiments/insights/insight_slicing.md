### Maestro Challenge
### Course: Python101
### Date: Jan 26 - 2026
_________________________________________________

**Slicing using Index**
- slicing format: letters[start : stop : step]
- step controls skipping patterns (e.g every 2nd element)
- to skip a specific index, combine slices
- List holds characters ["c", "a", "s", "h"]
- Strings are immutable
- "".join() = "glue list of string into string"
- split() = string to list

Use: letters[0:1] + letters[2:5] to skip index 1
__________________________________________________

**Example**

- Using "".join() 

letters = ["c", "r", "a", "s", "h", "e", "d"]

parts = letters[0:1] + letters[2:5]

print(parts)          # ['c', 'a', 's', 'h']

print("".join(parts)) # cash


