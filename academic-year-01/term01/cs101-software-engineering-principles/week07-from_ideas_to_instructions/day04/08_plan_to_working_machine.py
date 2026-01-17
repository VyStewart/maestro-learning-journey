### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 07: From plan to working machine
### Date: Jan - 16 - 2026

# Example
n = int(input("Enter a number: "))
counter = 1
while counter <= n:
    if counter % 2 == 0:
        print(counter)
    counter +=1
    
# Using .isdigit to guard non numeric input
while True:
    user_input = int(input("Enter a number: "))
    if user_input.isdigit():
        number = int(user_input)
        break
    else:
        print("Invalid Input: please enter a number")
        
count = 1
total = 0
while count <= number:
    total += count
    count += 1
print(total)

# Using try/ expect to check non numeric input
# Also prevent negative input
while True:
    try:
        num = int(input("Enter a number: "))
        if num <= 0:
            print("Invalid Input: number need to be greater than zero")
        else:
            break
    except ValueError:
        print("Invalid input: please enter a number")
        
count = 1
total = 0

while count <= num:
    total += count
    count += 1

print(total)

