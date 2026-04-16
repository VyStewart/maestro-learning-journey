### Maestro Challenge
### Course: Python101
## Date: Jan 31 - 2026

# for and while loop
"""
Task:
 Write a loop that counts how many multiples of 3 are 
 between two numbers, inclusive. (5 and 50 for example)
 if more than 10 are found, stop early
"""
# for loop
count = 0

for num in range(5, 51):
    if num % 3 == 0:
        count += 1
        
    if count > 10:
        break
    
print("Multiple of 3 found:", count)
        
# while loop
count = 0
num = 5

while num < 51:
    if num % 3 == 0:
        count += 1
        
    num += 1
    
    if count > 12:
        break
    
print("\nMultiple of 3 found:", count)



        
