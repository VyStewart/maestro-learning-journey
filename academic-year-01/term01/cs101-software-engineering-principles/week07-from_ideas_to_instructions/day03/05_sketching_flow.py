### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 05: Sketching flow
### Date: Jan - 15 - 2026

# Example
"""
    Full flown description (written in Python)
    IF age < 13 ➜ apply child discount
    IF 13 <= age <= 17 ➜ apply teen discount
    IF 18 <= age <= 64 ➜ pay full price
    IF age >= 65 ➜ apply senior discount
    
"""
# Step 1: Get input (data from the user)
age = int(input("Enter your age: "))

# Step 2: Apply rules in order from most specific to broad
if age < 13:
    # Rule: Children are under 13
    print("Apply child discount")

elif age <= 17:
    # Rule: Teens are ages 13–17
    print("Apply teen discount")

elif age <= 64:
    # Rule: Adults are ages 18–64
    print("Pay full price")

else:
    # Rule: Seniors are 65 and older
    print("Apply senior discount")



    