### Lesson: Loop control: break and continue
### Date: 12-14-2025

## Two "emergency controls" inside the loop
# break: stop the whole loop right now
# continue: skip the rest of this one turn and jump to the next turn

# break in a for loop
# Example 1:
for number in range(1,21):
    print("Checking number:", number)
    if number == 7:
        print("Found 7! Breaking out of the loop.")
        break

print("Loop finished maybe early.")

# ontinue - skip just this iteration, keep looping
for n in range(1, 11):
    print("Top of loop, n =", n)

    # if n is even, we will SKIP the rest of this turn
    if n % 2 == 0:
        print("n is even, will continue here.")
        continue

    print("Bottom of loop, n =", n)

print("Loop done.")

# Challenge: Using continue to print only numbers are not multiple of 3
for x in range(1,16):
    if x % 3 == 0:
        
        print(x ,"is a multiple of 3, skipping.")
        continue

    print("Processing:", x)
    
# Challenge: mixed continue and break

for n in range(1, 21):
    if n % 2 == 0:
        print(f"{n} is even skipping with continue.")
        continue

    if (n % 2 == 1) and (n > 15):   # n > 15 because even numbers are skipped.
        print(f"Found odd number over 15: {n}, break here.")
        break

    else:
        print(f"Processing odd: {n}")

