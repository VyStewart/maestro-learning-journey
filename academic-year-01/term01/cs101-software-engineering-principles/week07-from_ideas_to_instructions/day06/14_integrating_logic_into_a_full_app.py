### CS101:  Software Engineering Principles
### Week 07: From ideas to instruction
## Lesson 14: Integrating logic into a full app
### Date: Jan 18 - 2026

# Example: 

# 1) Input
age = None  # we'll fill this in

# 2) Logic
ticket_price = None  # we'll fill this in

# 3) Output
print("Your ticket costs: ...")  # we'll improve this

# Integrating logic

# 1) Input
while True:
    age_text = input("Enter your age: ")

    if not age_text.isdigit():
        print("Please enter your age as a number")
        continue
    
    age = int(age_text)

    if age < 0:
        print("Age can not be negative")
        continue

    break

# 2) Logic
if age < 13:
    ticket_price = 8
elif age < 18:
    ticket_price = 10
elif age < 65:
    ticket_price = 12
else: 
    ticket_price = 7

# 3) Output
print(f"Your ticket costs: ${ticket_price}")  

# Using try/ excpet pair for validation check

# Step 1: Get a valid age (repeat until valid)
while True:
    age_text = input("Enter your age: ")

    try:
        age = int(age_text)
    except ValueError:
        print("Please enter your age as a whole number.")
        continue

    if age < 0:
        print("Age cannot be negative.")
        continue

    break

# Step 2: Apply ticket pricing rules
if age < 13:
    ticket_price = 8
elif age < 18:
    ticket_price = 10
elif age < 65:
    ticket_price = 12
else:
    ticket_price = 7

# Step 3: Display ticket price
print(f"Your ticket costs: ${ticket_price}")
