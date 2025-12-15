### Meet the while loop
### Date 12-14 - 2025

# while loops are for unknow duration, a while loop repeats as long as condition stays True

# Control while loop: with a counter
# Example 1
counter = 1

while counter <= 4:
    print(counter)
    counter += 2
    
# Example 2:
num = 10

while num >= 6:
    print(num)
    num -= 1
    
# Control while loop : with a Boolean flag
# Example 3: stop while loop
running = True

while running:
    print("Still running")
    running = False
    
# Comoare for loop and while loop
# for loop
for i in range(1,4):
    print(i)

# while loop
counter = 1

while counter <= 3:
    print(counter)
    counter += 1

# Challenge: while loop counts by 2s
num = 2

while num <= 10:
    print(num)
    num += 2
    
# Mixed challenge with counter and Boolean flag
running = True
count = 1

while running:
    print("Loop number:", count)

    if count == 3:
        running = False
    count += 1
        
