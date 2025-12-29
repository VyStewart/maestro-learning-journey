# Day 03 – Scope, Local Variables & If/Else Preview

### Concepts Learned
- **Scope** controls where a variable exists and where it can be used.
- Variables created **inside** a function are **local** to that function.
- Variables created **outside** any function are **global** and can be read inside (unless shadowed by a local variable with the same name).
- Assigning to a name inside a function makes it **local**, which can cause `UnboundLocalError` if you try to use it before assigning.
- A clean pattern is: **pass values into the function → compute → return the result**, instead of mutating global variables.
- `if / else` lets the program choose between two paths based on a condition.
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) are used to build conditions.

---

### Local vs Global Scope

A **local variable** is defined inside a function and exists only there.

def study(hours):
    label = "hour" if hours == 1 else "hours"
    return f"I study {hours} {label} every day."


## Scope Rules & Clean Pattern
Key rules:
- Local variables are created inside a function and disappear when the function ends.
- Global variables live outside functions and can be read inside (unless a local variable with the same name exists).
- Assigning to a variable inside a function makes it local by default.
- Best practice: pass in values, compute, return the result.

## UnboundLocalError with Global Names
Problem scenario:

value = 50

def mystery(x):
    y = x + value
    value = 10
    return y

This causes:
UnboundLocalError: local variable 'value' referenced before assignment

Because:
- Python sees value = 10 and treats value as a local variable.
- It then tries to evaluate y = x + value before the local value is assigned.
- The global value is ignored inside the function once Python decides value is local.

Fix options (conceptually):
- Read only the global value (remove the local assignment), or
- Assign the local variable before using it, or
- Use the clean pattern: pass values in and return results instead of modifying globals.

## Nested Scope (Enclosing Function)

x = 1

def outer():
    x = 2           # local to outer()
    def inner():
        print(x)    # reads x from outer(), not global x
    inner()

outer()
print(x)

### If/Else Preview (Decision Making)
## Comparison Operators
Using:
x = 5
y = 7

print("x == y:", x == y)   # False
print("x != y:", x != y)   # True
print("x < y:", x < y)     # True
print("x > y:", x > y)     # False
print("x <= y:", x <= y)   # True
print("x >= y:", x >= y)   # False

These comparisons are the building blocks for if conditions.


### Reflection
Today I learned how scope affects where variables can be seen and used.
- I understand that local variables are safer and cleaner for function logic.
- I saw how local variables can shadow global ones without changing them.
- I understand that assigning inside a function can cause UnboundLocalError if not done carefully.
- Previewing if/else and comparison operators feels easier now because I already understand how functions flow and return values.

