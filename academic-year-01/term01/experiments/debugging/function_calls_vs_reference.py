### Maestro Challenge
### Course: Python101
## Date: Jan 29 - 2026

# Passing function as data
def greet(name):
    return f"Hello, {name}!"

def make_greeting(func, user):
    return func

result = make_greeting(greet, "Vy")
print(result)

"""
Output
<function greet at 0xa0b2c0>
"""

# Debugging
def greet(name):
    return f"Hello, {name}!"

def make_greeting(func, user):
    return func(user)

result = make_greeting(greet, "Vy")
print(result)

# Example
def double(x):
    return x * 2

def run_twice(f, val):
   return f(f(val))

test = run_twice(double, 5)
print(test)