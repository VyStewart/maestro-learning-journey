### Maestro Challenge
### Course: Python101
## Date: Jan 28 - 2026

# function/return debugging
def safe_divide(a, b):
    if b == 0:
        print("Error: division by zero")
    return a / b

#print(safe_divide(5,0))

"""
Error: division by zero
Traceback (most recent call last):
ZeroDivisionError: division by zero
"""

# debugging
def safe_divide(a, b):
    if b == 0:
        print("Error: division by zero")
        return None
    return a / b

print(safe_divide(5, 0))

# advanced version
def safe_divide(a,b):
    if b == 0:
        raise ValueError("division by zero")
    return a/b

try:
    print(safe_divide(10, 0) +1)
except ValueError:
    print("\nCannot divide")
    
    

