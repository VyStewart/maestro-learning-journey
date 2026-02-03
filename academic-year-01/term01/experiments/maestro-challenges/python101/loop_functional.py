### Maestro Challenge
### Course: Python101
## Date: Feb 01 - 2026

# Loop & function
'''
Task: Print out all multiples of 7 between 20 and 100 (inclusive).
But: skip any number that ends with a 4 (like 34, 74, etc).
If more than 10 are found, stop early
'''

def find_multiples_for(start, end):
    count = 0
    limit = 10
    numbers = []
    
    for num in range(start, end +1):
        if num % 7 == 0 and num % 10 != 4:
            count += 1
            numbers.append(num)   
            
            if count >= limit:
                break        
    
    return count, numbers

count, numbers = find_multiples_for(20, 100)   

print(
    f"Multiples of 7 found: {count}"
    f"\nNumbers of multiples of 7 are: {numbers}"
)

# while loop
def find_multiples_while(start, end):
    number = start
    count = 0
    limit = 10
    numbers = []
    
    while number <= end:
        if number % 10 == 4:
            number += 1
            continue
        
        if number % 7 == 0:
            count += 1 
            numbers.append(number)  
          
            if count >= limit:
                break
        
        number += 1
        
    return count, numbers

count, numbers = find_multiples_while(20, 100)
print(
    f"\nMultiples of 7 found: {count}"
    f"\nNumbers of multiples of 7 are: {numbers}"
)       