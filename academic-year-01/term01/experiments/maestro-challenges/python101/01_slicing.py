### Maestro Challenge
### Course: Python101
## Date: Jan 26 - 2026

# Slicing using index
"""
Task: write one-line sclice expressions that print these three words
- 'cash'
- 'shed'
- 'rash'
"""

letters = ["c", "r", "a", "s", "h", "e", "d"]

# To skip a specific index, combine slices
# To skip index 1
print(letters[0:1] + letters[2:5])
print(letters[3:])
print(letters[1:5])

print("\nUsing "".join() to convert Lists to Words")
print("".join(letters[0:1] + letters[2:5]))
print("".join(letters[3:]))
print("".join(letters[1:5]))