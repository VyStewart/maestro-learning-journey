### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 07: Reviewing the plan
### Date: Jan - 16 - 2026

# Example of gap and overlap
age = int(input("Enter age: "))

if age < 13:
    print("child ticket")
elif age <= 18:
    print("teen ticket")
elif age >= 18 and age < 65:
    print("adult ticket")
else:
    print("senior ticket")

# Fixing using rules
'''
Under 13 → child
13 - 17 → teen
18 - 64 → adult
65+ → senior
'''
age = int(input("Enter age: "))

if age < 13:
    print("child ticket")
elif age >= 13 and age <= 17:
    print("teen ticket")
elif age >= 18 and age <= 64:
    print("adult ticket")
else:
    print("senior ticket")
    
# Short version and also check againts invalid age and non numeric input

# Using while loop to check non numeric number and ask until iput unmber
while True:
    try:
        age = int(input("Enter age: "))
        break
    except ValueError:
        print("Invalid input: please enter a number.")  
                      
# guard against invalid age
if age < 0 or age > 120:
    print("invalid age")
    exit()
elif age < 13:
    print("child ticket")
elif age <= 17:
    print("teen ticket")
elif age <= 64:
    print("adult ticket")
else:
    print("senior ticket")