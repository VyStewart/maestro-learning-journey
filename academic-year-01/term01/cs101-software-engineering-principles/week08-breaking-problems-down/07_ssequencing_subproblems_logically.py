### CS101:  Software Engineering Principles
### Week 08: Breaking Down the probles
## Lesson 07: Sequencing subproblems logically
### Date: Jan 22 - 2026

# Example

# H. Greet the user and explain the tracker
# D. Set the running total of glasses to 0 at the start of the day
# B. Ask the user how many glasses of water they just drank
# A. Add the new water amount to the running total
# G. Tell the user their current total after each entry
# F. While the day is not over, repeat the tracking steps
# E. Decide whether to ask again or finish (e.g., is the day over?)
# C. At the end of the day, print the total number of glasses drunk

# Implement the codes:

print(" Hello. This app to track how much water you drink within a day.")

total_glasses = 0
day_over = False

while not day_over:
    glass_of_water = int(input("How many glasses of water did you drink? "))
    total_glasses += glass_of_water
    print("Total glasses of water:", total_glasses)

    answer = input("Is the day over? Y/N ")
    if answer == "Y":
        day_over = True

print("Final total:", total_glasses)
