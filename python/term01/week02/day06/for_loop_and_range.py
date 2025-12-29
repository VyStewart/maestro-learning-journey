## Lesson: For loop and range(): counting iterations
## Date: 12-14-2025

# A for reapeat some code in a fixed number of times
# Example 1: range(stop)
for i in range(5):
    print(i)
    
# Example 2: range(start, stop)
for num in range(2, 7):
    print(num)

# Example 3: range(start, stop, step)
for x in range(0, 10, 2):   # started with 0, stopped by 10, and jumped by 2 each time
    print(x)
    
# Example using for loop with range()
# Building a running total
total = 0
for n in range(1, 6):
    total = total + n
print(total)

total = 0
for m in range(1, 11):
    total += m
print(total)

# Example using for loop plus % 2 
# To generate even numbers
for n in range(0, 11):
    if n % 2 == 0:
        print(n)

# To generate odd numbers
for m in range(0, 12):
    if m % 2 == 1:
        print(m)
        
# To countdowns with negative step
for x in range(5, -1, -2):
    print(x)

# All in one practice
for i in range(1, 11):
    print(i)

for n in range(1, 11):
    if n % 2 == 0:
        print(n)

for x in range(10, 0, -1):
    print(x)