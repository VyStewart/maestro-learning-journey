### Lesson i: creating lists
### Date: 12-17-2025

## A list is a single variable that hold several values, written in square brackets.
# Example:
numbers = [4, 7, 10]
print(numbers)          # [4, 7, 10]

## turn a range() to a list and count items with lens
# Example 1:
scores = list(range(1, 6))

print(scores)           # [1, 2, 3, 4, 5]
print(len(scores))      # 5

# Example 2:
values = [10, 20, 30, 40]

print(values)
print(len(values))

## Lists can change, being mutable
# Example :
scores = [12, 15, 18]
print(scores)               # [12, 15, 18]

scores[0] = 99
print(scores)               # [99, 15, 18]

# Example :
numbers = [3, 6, 9]
print(numbers)              # [3, 6, 9]

numbers[1] = 100
print(numbers)              # [3, 100, 9]

# Practice
scores = [50, 60, 70, 80]
print(scores)                       # [50, 60, 70, 80]
print(len(scores))                  # 4

more_scores = list(range(10, 16))   

print(more_scores)                  # [10, 11, 12, 13, 14, 15]                  
print(len(more_scores))             # 6

scores[3] = 93                  
print(scores)                       # [50, 60, 70, 93]

# Boss-level Challenge — List Practice

scores = [55, 70, 85, 90, 40, 100]

print(scores)
print(len(scores))

# Update specific scores by index
scores[2] = 32
scores[4] = 45

print(scores)

# Create a list of even numbers using range(start, stop, step)
even_numbers = list(range(2, 13, 2))

print(even_numbers)      # [2, 4, 6, 8, 10, 12]
print(len(even_numbers)) # 6
