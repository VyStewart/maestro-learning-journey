### CS101 - Week 06
### Software Engineering Principles
### Lesson 03: Crafting Docstrings that explain the why
### Date: Jan 05 2026

# Example: 

def to_celsius(fehrenheit):
    return (fehrenheit -32) * 5 / 9

# Adding docstring
def to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius.

    fahrenheit: temperature value in degrees Fahrenheit.
    Returns the same temperature converted to degrees Celsius.
    """
    return (fahrenheit - 32) * 5 / 9

result = to_celsius(86)
print(round(result))
