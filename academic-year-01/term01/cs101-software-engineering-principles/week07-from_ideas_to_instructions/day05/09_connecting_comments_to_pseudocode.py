### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 09: Kepping comments that connect to pseudocode
### Date: Jan 17 - 2026

# 1. Get user age
age = int(input("Enter age: "))

# 2. Determine ticket type based on age rules
if age < 13:
    ticket = "child ticket"
elif age <= 17:
    ticket = "teen ticket"
elif age <= 64:
    ticket = "adult ticket"
else:
    ticket = "senior ticket"

# 3. Print ticket type
print(ticket)
