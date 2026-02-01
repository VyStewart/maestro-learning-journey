### Maestro Challenge
### Course: Python101
## Date: Jan 31 - 2026

# for and while loop
'''
Task: Print out all multiples of 7 between 20 and 110 (inclusive).
But: skip any number that ends with a 4 (like 34, 74, etc).
'''

# for loop
count = 0
numbers = []

for num in range(20, 111):
    if num % 10 == 4:
        continue
    
    if num % 7 == 0:
        count += 1
        
        numbers.append(num)
        
print(
    f"Multiples of 7 found: {count}"
    f"\nNumbers of multiples of 7 found: {numbers}"
)

# while loop
count = 0
number = 20

while number < 201:
    if number % 10 == 4:
        number += 1
        continue
    
    if number % 7 == 0:
        count += 1
        
    number += 1
    
    if count > 15:
        break         
      
print("\nMultiples of 7 found:", count)