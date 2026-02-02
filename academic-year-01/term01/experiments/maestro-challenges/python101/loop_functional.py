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
        
# Adavnced version
def find_multiples_while(start, end, division, skip_ends, n_limit):
    n = start 
    n_count = 0
    nums_found = []
    
    while n <= end:
        # Skip numbers ending in any digit from skip_ends
        if n % 10 in skip_ends:
            n += 1
            continue
        
        # collect multiples of division
        if n % division == 0:
            n_count += 1
            nums_found.append(n)
            
            # stop immediately once limit is reached 
            if n_count >= n_limit:
                break
        
        n += 1
    
    return n_count, nums_found

# Example
a, b = find_multiples_while(10, 120, division=5, skip_ends=(0,), n_limit=5)
c, d = find_multiples_while(20, 100, division=3, skip_ends=(4,5), n_limit=10)

print("\n", a, b)
print("\n", c, d)
