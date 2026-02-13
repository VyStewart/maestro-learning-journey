### Maestro Challenge
### Course: Python101
### Date: Feb 02 - 2026

## Loop & function 

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

# Add guard clause to loop_function
def find_muiltiples(start, end, num_division, skip_ends, num_limit):
    
    # Add guard clause - stop bad input immadiately 
    if start < 0 or end <= 0:
        return None
    
    if start > end:
        return None
    
    if num_division <= 0 or num_limit <= 0:
        return None
    
    if not isinstance(skip_ends, tuple):
        return None
    
    num_count = 0
    found_numbers = []
    
    for num in range(start, end + 1):
        if num % 10 in skip_ends:
            continue
        
        if num % num_division == 0:
            num_count += 1
            found_numbers.append(num)
            
            if num_count >= num_limit:
                break
            
    return num_count, found_numbers

# Example
result = find_muiltiples(10, 400, 6, (8,), 10)

if result is None:
    print("Invalid input. Input values must be >= 0")
else:
    c1, d1 = result
    print("\n",c1, d1 )

# test call   
test = find_muiltiples(0, 600, 3, (5,0,), 15)

if test is None:
    print("Invalid input. Input values must be >= 0")
else:
    a1, b1 = test
    print("\n", a1, b1)    