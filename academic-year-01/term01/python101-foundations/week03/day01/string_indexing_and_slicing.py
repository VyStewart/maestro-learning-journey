### Lesson: String skills upgrade i: Indexing and slicing
### Date 12-15-2025

## zero-based indexing for strings
# Example 1:
text = "Python"

print(text[0])      # P
print(text[1])      # y
print(text[5])      # n

# Example:
word = "Interaction"

print(word[0])      # I
print(word[2])      # t
print(word[4])      # r

## Basic slicing with [start:stop] and start:
## Rule: start is included, stop is excluded

# Example :
text = "Programming"

print(text[0:3])    # Pro
print(text[3:7])    # gram
print(text[8:])     # ing

## Full form of slicing: text[start:stop:step]
## Rule: step tells Python how much to move each time

# Example: Print every second character starting from A, using sigle slice with step
code = "ABCDEFGHIJ"

print(code[0:10:2])     # ACEGI

## Nefative indices count from the end

# Example:
name = "Maestro"

print(name[-1])     # o
print(name[-2])     # r

## Combine negative indicies with slicing

# Example:
# Print the last 3 characters using a slice with negative indices.
# Print everything except the last 2 characters, also using a slice with negative indices.
title = "Introduction"

print(title[-3:])       # ion
print(title[:-2])       # Introducti

# Exercise 
text = "HelloWorld"

print(text[0:5])            # Hello
print(text[-10:-5])         # Hello
print(text[:-5])            # Hello
print(text[-5:])            # World
print(text[5:10])           # World
print(text[-10:-1:2])       # Hlool
print(text[0:9:2])          # Hlool


