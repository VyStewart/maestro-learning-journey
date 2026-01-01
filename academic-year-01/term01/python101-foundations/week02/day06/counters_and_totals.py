### Lesson: counters and totals
### Date: 12-14-2025

## dual accumulators: keeping a counter and a running total side by side in a loop
# Example 1:
count = 0
total = 0

for n in range(1,6):
    count += 1
    total += n
    
print(f"Count: {count}")    # 5
print(f"Total: {total}")    # 15

# Example 2: using for in range() loop
count = 0
total = 0

for n in range(1, 11):
    count = count + 1
    total = total + n

print("There are ", count, "numbers and their total is:", total)   # 10 and 55

# Example 2: using while loop
count = 0
total = 0
n = 1

while n <= 10:
    count += 1
    total += n
    n += 1

print("There are", count, "numbers and their total is:", total)     # 10 and 55

# Pactice
count = 0
total = 0

for n in range(1, 8):
    count += 1
    total += n

print("Count is", count, "and total is:", total)

# Challenge - Boss-level
count_even = 0
total_even = 0
count_odd = 0
total_odd = 0

for n in range(1, 21):
    if n % 2 == 0:
        count_even += 1
        total_even += n
    
    if n % 2 == 1:
        count_odd += 1
        total_odd += n

print("Even count:", count_even, "Even total:", total_even)     # 10 and 110
print("Odd count:", count_odd, "Odd total:", total_odd)         # 10 and 100

# Using if/ else
count_even = 0
total_even = 0
count_odd = 0
total_odd = 0

for n in range(1, 21):
    if n % 2 == 0:
        count_even += 1
        total_even += n
    else:
        count_odd += 1
        total_odd += n
        
print(f"Even count: {count_even} Even total: {total_even}")
print(f"Odd count {count_odd} Odd total: {total_odd}")
        
        



