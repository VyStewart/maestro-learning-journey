### Lesson-Update and copy semantics
### Date: 12-21-2025

## Variable as references with list and dict
## In Python, a variable acts like a reference (apointer) to that object in memory
# Example

numbers = [1, 2, 3]
other = numbers

print("Before change:")
print("numbers:", numbers)
print("other:", other)


numbers.append(4)
print("\nAfter numbers.append(4):")
print("numbers:", numbers)
print("other:", other)

## Shallow-copy patterns
# Using slicing[:] to make a new lit (seperate object)
# [:] takes a slice of the whole list, from start to end
# Example

numbers = [1, 2, 3]
copy1 = numbers[:]

numbers.append(4)
copy1.append(5)

print("\nnumbers:", numbers)
print("copy1", copy1)

# h = list(a) and h = a.copy()

a = [10, 20, 30]

h1 = list(a)            # constructor copy
h2 = a.copy()           # method copy
alias = a               # same list, diffrent name

print("\nBefore change:")
print("a:       ", a)
print("h1:      ", h1)
print("h2:      ", h2)
print("alias:   ", alias)

a.append(40)
h2.append(60)

print("\nAfter a.append(40):")
print("a:     ", a)
print("h1:    ", h1)
print("h2:    ", h2)
print("alias: ", alias)

## Dict shalow copy 
# Example:

person = {"name": "Vy", "age": 22,}

alias = person          # NO copy
copy1 = dict(person)    # construct copy
copy2 = person.copy()    # method copy

print("\nBefore change:")
print("person:",    person)
print("alias:",     alias)
print("copy1:",     copy1)
print("copy2:",     copy2)

person["age"] = 25

print("\nAfter change person age to 25")
print("person:",    person)
print("alias:",     alias)
print("copy1:",     copy1)
print("copy2:",     copy2)





