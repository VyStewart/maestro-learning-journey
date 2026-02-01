### Maestro Challenge
### Course: Python101
## Date: Jan 31 - 2026

# while loop
count = 0
num = 5

while num < 51:
    if num % 3 == 0:
        count += 1

        num + 1 
        
    if count > 10:
        break

#print("Multiples of 3 found:", count)

"""
Create an infinitive loop
"""

# Debugging
count = 0
num = 5

while num < 51:
    if num % 3 == 0:
        count += 1
        
    num += 1   # ← always moves the loop forward
   
    if count > 10:
        break     

print("Multiples of 3 found:", count)

