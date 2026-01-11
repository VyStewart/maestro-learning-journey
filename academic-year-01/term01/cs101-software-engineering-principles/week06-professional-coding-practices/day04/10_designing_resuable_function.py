### CS101 - Week 06
### Software Engineering Principles
### Lesson 10: Designing Functions that can be resued anywhere
### Date: Jan 08 2026

# Function with return
def double(num):
    result = num * 2
    return result

value = double(5)
print(value)

# Compare print inside the function and function with return
def double_print(number):
    print(number * 2)

def double_return(number):
    return number * 2

print("\nCalling double_print:")
a = double_print(9)
print("a is:", a)

print("\nCalling double_return:")
b = double_return(9)
print("b is:", b)

# chaining functions 
def double(number):
    return number * 2

def add_three(number):
    return number + 3

result = add_three(double(4))
print(result)

# Challenge: design chain functions
def apply_discount(amount, discount_percent):
    # discount_percent is like 10 for 10%
    discount = amount * (discount_percent / 100)
    return  amount - discount

def add_tax(amount, tax_rate):
    # tax rate is like 0.07 for 7%
    tax = amount * tax_rate
    return amount + tax

final_total = add_tax(apply_discount(100, 10), 0.07)
print(final_total)

# Challenge:
# Create the function to convert Fahrenheit to Kelvin

def to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Returns None if the value is below absolute zero.
    """
    if fahrenheit <= -459.67:
        print("Error: Fahrenheit must be above absolute zero.")
        return None  # Stop the chain safely

    return (fahrenheit - 32) * 5 / 9


def to_kelvin(celsius):
    """
    Convert Celsius to Kelvin.
    If input is None, return None to preserve chain safety.
    """
    if celsius is None:
        return None

    return celsius + 273.15


def format_temperature(kelvin):
    """
    Format the Kelvin temperature for display.
    """
    return f"\nThe temperature is: {kelvin} K"


# Chained execution with safety preserved
result = format_temperature(to_kelvin(to_celsius(77)))
print(result)
