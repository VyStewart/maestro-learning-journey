# Day 05 - Checking Facts, Type Conversion, User Input

# 1. Checking value types with type()
print("=== Checking Types ===")
print(type("Vy"))        # string
print(type(30))          # int
print(type(3.14))        # float
print(type(True))        # bool

print()

# 2. Converting between types
age_str = "30"
age_int = int(age_str)
print("Age as string:", age_str, type(age_str))
print("Age as int:", age_int, type(age_int))

pi_str = "3.14"
pi_float = float(pi_str)
print("Pi as float:", pi_float, type(pi_float))

print()

# 3. Converting int → string for printing
year = 2025
print("The year is " + str(year))

print()

# Example of checking facts, convert int -> str and str to-> int for prinitng

a = "10"
b = "4.5"
c = 3

sum1 = int(a) + float(b) + 3
sum2 = a + "-" + b + "-" + str(c)

print(sum1)
print(sum2)

print(type(sum1))
print(type(sum2))

# 4. User input examples

# Example 1: Using Inout for counting the cookies

daily_cookies = input("How many cookies did you eat today?")
daily_cookies_num = int(daily_cookies)
monthly_cookies = daily_cookies_num * 30

print(f"You ate {daily_cookies_num} cookie today.")
print(f"That would be {monthly_cookies} cookies in 30 days.")

# Ecample 2: Using Input for calculating gas per mileage 

miles_driven = input("How many miles did you drive today?")
gas_usage =input("How many gallons of gas did you use?")
miles = float(miles_driven)
gas = float(gas_usage)
mpg = miles / gas

print(f"You drove {miles} miles using {gas} gallons.")
print(f"Your gas mileage is {mpg:.2f} miles per gallon.")
