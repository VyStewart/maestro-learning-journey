### Maestro Challenge
### Course: Python101
## Date: Jan 31 - 2026

# for and while loop
'''
Task: Print out all multiples of 7 between 20 and 100 (inclusive).
But: skip any number that ends with a 4 (like 34, 74, etc).
'''

start = 20
end = 100
n = start
limit = 10

# for loop
count = 0
numbers = []

for num in range(start, end +1):
    if num % 10 == 4:
        continue
    
    if num % 7 == 0:
        count += 1
        
        numbers.append(num)
    
    if count > limit:
        break         
        
print(
    f"Multiples of 7 found: {count}"
    f"\nNumbers of multiples of 7 are: {numbers}"
)

# while loop
while n <= end:
    if n % 10 == 4:
        n += 1
        continue
    
    if n % 7 == 0:
        count += 1
        
        numbers.append(n)
        
    n += 1
    
    if count > limit:
        break         
      
print(
    f"\nMultiples of 7 found:{count}"
    f"\nNumbers of multiples of 7 are: {numbers}"
)