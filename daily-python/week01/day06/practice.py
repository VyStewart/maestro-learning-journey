# Day 06 - Type Casting (Converting Data Types)

# 1. Basic conversions
print("=== Basic Type Casting ===")
a = "10"
b = int(a)       # convert string → int
c = "4.5"
d = float(c)     # convert string → float
e = 21
f = str(e)       # convert int → string

print("Original:", a, type(a))
print("As int:", b, type(b))
print("Original:", c, type(c))
print("As float:", d, type(d))
print("Original:", e, type(e))
print("As string:", f, type(f))

print()

# 2. Mixing conversions in calculations
print("=== Mixing Types in Calculations ===")
x = "25"
y = "4.5"
z = 3

sum1 = int(x) + float(y) + z
sum2 = x + "-" + y + "-" + str(z)

print("Numeric sum:", sum1)
print("String combination:", sum2)

print()

# 3. Examples

# Example A: Convert minutes to hours
minutes = input("How many minutes did you study today? ")
minutes_num = int(minutes)
hours = minutes_num / 60
print(f"You studied {minutes_num} minutes today.")
print(f"That is {hours:.2f} hours of study time.")

# Example B: Convert price input to float
price = float(input("Enter a price: "))
print(f"You entered: ${price:.2f}")

print("User input examples included (commented out for GitHub).")

print()

# Challenge: Convert Int, Str, Float 
# using type casting with right conversation on purpose

apples_text = "4"
oranges_text = "2.5"

apples_num = int(apples_text)
oranges_decimal = float(oranges_text)
total_fruits = apples_num + oranges_decimal

print(total_fruits)
print(f"Total apples and oranges is: {total_fruits} of {apples_num} apples and {oranges_decimal} oranges.")



# 4. Checking types directly
print("=== Type Checking ===")
print(type(a))        # str
print(type(b))        # int
print(type(d))        # float
print(type(f))        # str

