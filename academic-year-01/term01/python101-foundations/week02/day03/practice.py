


# Week 02 – Day 03 Practice
# Scope, Local Variables & If/Else Preview


# ----------------------------------------
# Practice 1 — Local vs Global Scope
# ----------------------------------------

value = 10  # global variable

def change():
    value = 20  # local variable, shadows global
    print(f"inside: {value}")

change()
print(f"outside: {value}")  # global remains 10



# ----------------------------------------
# Practice 2 — Clean Pattern: Pass In → Compute → Return
# ----------------------------------------

total = 0

def add(current_total):
    new_total = current_total + 1
    print(f"inside: {new_total}")
    return new_total

total = add(total)
total = add(total)
total = add(total)

print(f"outside: {total}")  # should be 3



# ----------------------------------------
# Practice 3 — Shadowing Global with Local
# ----------------------------------------

n = 3  # global variable

def multiply(x):
    n = 5  # local variable shadows global
    return x * n

result = multiply(n)

print(n)       # 3 (global)
print(result)  # 15 (3 * local 5)



# ----------------------------------------
# Practice 4 — Nested Scope (Enclosing Function)
# ----------------------------------------

x = 1  # global variable

def outer():
    x = 2           # local to outer()
    def inner():
        print(x)    # uses x from outer(), not global
    inner()

outer()
print(x)  # global x → 1



# ----------------------------------------
# Practice 5 — Sum of Even Numbers (Preview: loop + if)
# ----------------------------------------

def sum_even(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total = total + n
    return total

result = sum_even([1, 2, 3, 4, 5, 6])
print(result)  # Expected: 12



# ----------------------------------------
# Practice 6 — Count Positive Numbers (Preview)
# ----------------------------------------

def count_positive(numbers):
    count = 0
    for n in numbers:
        if n > 0:
            count = count + 1
    return count

result = count_positive([-1, 0, 3, 5, -1])
print(result)  # Expected: 2



# ----------------------------------------
# Practice 7 — Simple if/else: Cookies
# ----------------------------------------

cookies = 0

if cookies > 0:
    print("You still have cookies!")
else:
    print("No cookies left.")



# ----------------------------------------
# Practice 8 — Comparison Operators
# ----------------------------------------

x = 5
y = 7

print("x == y:", x == y)   # False
print("x != y:", x != y)   # True
print("x < y:", x < y)     # True
print("x > y:", x > y)     # False
print("x <= y:", x <= y)   # True
print("x >= y:", x >= y)   # False



# ----------------------------------------
# Practice 9 — Boss-Level If/Else Challenge
# ----------------------------------------

my_points = 18
friend_points = 22

if my_points > friend_points:
    print("I have more points than my friend.")
else:
    print("My friend has at least as many points as me.")
