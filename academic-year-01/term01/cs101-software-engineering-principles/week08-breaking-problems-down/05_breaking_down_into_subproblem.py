### CS101:  Software Engineering Principles
### Week 08: Breaking problems down
## Lesson 05: Breaking down into subproblem
### Date: Jan 22 - 2026

# Example:

# 1. Set up the data for today's step total
total_steps = 0
print("Starting step counter for today")

# 2. Let user log how many steps they just walked
#    2.1 Ask user how many steps they walked
new_steps = int(input("How many steps did you walk? "))
print(" New Steps counted:", new_steps)

#    2.2 Add that amount to today's total
total_steps += new_steps

# 3. Show today's total steps
print("Total steps walking:", total_steps)

# 4. If total is at least 10_000, show a "goal reached" message

# Practice

# 1. Set up today's total study minutes
total_minutes = 0
print("Starting study time:")

# 2. Let the user enter how many minutes for this study session
#    2.1 Ask how many minutes this session
minutes = int(input("How many minutes did you study per session? "))
print("Study time:", minutes)

#    2.2 Add the minutes to today's total minutes
total_minutes += minutes

# 3. Show today's total minutes
print("Total minutes:", total_minutes)

# 4. Show a message when the total minutes reach at least 120
if total_minutes >= 120:
    print(" Great job! You reached your 120-minutesb goal")