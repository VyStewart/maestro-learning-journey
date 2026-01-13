### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 01: Balancing planning and coding
### Date: Jan - 12 - 2026

## The planning spectrum
# Build something fast to see if the idea works
# Minimum Visabe Prototype (MVP)

# Example: planning before coding

# set a numbers list
numbers = []
# set even_number to 0
even_count = 0

# Ask user for a number
while True:
    number = int(input("Enter a number: "))

    # Stop when number = 0
    if number == 0:
        break
    # Add number entered to number list
    numbers.append(number)

    # if number is even, add 1 to counter
    if number % 2 == 0:
        even_count += 1
        
print("Numbers enterd:", numbers)
print("Even numbers entered:", even_count)