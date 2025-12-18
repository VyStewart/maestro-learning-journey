### Lesson: Lists ii - indexing and slicing
### Date: 12-17-2025

## Simple indexing
# Example: positve

colors = ["red", "green", "blue", "yellow"]

print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])

# Example: negative

animals = ["cat", "dog", "bird", "fish"]

print("animals[0]", animals[0])
print("animals[-1]", animals[-1])
print("animals[-2]", animals[-2])

## Slicing
# Example: [start:stop]

temperatures = [18, 20, 21, 19, 22, 24]

print("Full list:", temperatures)               # [18, 20, 21, 19, 22, 24]
print("First three:", temperatures[0:3])        # [18, 20, 21]
print("Slices:", temperatures[1:4])             # [20, 21, 19]

# Example: [start:stop:step]

temperatures = [18, 20, 21, 19, 22, 24]

print("Every second values from start:", temperatures[1:6:2])       # [20, 19, 24]
print(f"Every second values from start: {temperatures[: : 2]}")     # [18, 21, 22]

# Changing list elements by index (in-place)
# Example: 

scores = [50, 60, 70, 80]
print("Before:", scores)

scores[1] = 65
scores[3]= 90

print("After:", scores)

# Example: 

scores = [10, 20, 30, 40, 50]
print("Before:", scores)

scores[2] = 99
scores[-1]= 0

print("After:", scores)

# Seeing and preventing IndexError using if/else
# Example: 

numbers = [1, 2, 3]

index = 3
if index < len(numbers):
    print(numbers[index])
else:
    print("Index out of range, max valid index is", len(numbers) - 1)
    
# All-in-one Exercise

# create list
items = ["a", "b", "c", "d", "e"]

# Acces elements by index
print(items[0])         # first element
print(items[-1])        # last element using negative index

# Slice a portion of the list (index 1 to 3)
print(items[1:4])

# Update an element using its index
items[2] = "X"
print(items)

# Safely access an index using if/else
index = 10
if index < len(items):
    print(items[index])
else:
    print(f"Index out of range, max valid index is: {len(items)-1}")