### CS101 - Week 06
### Software Engineering Principles
### Lesson 04: Writing Comments With Real Purpose
### Date: Jan 06 2026

# Example 

lives = 5
lives = lives - 1  # subtract 1 from lives


# Changing to good comment
lives = 5
lives = lives - 1   # Player lost a live in the game
print(lives)

# Example: before 
login_count = 0  # set login_count to 0
limit = 100      # set limit to 100

login_count = login_count + 1  # increase login_count by 1

# After change to good comments
login_count = 0     # first time log in
limit = 100         # maximum allowed log in per day

login_count = login_count + 1   # add the current log in into total log in count
print(login_count, limit)
