### CS101:  Software Engineering Principles
### Week 08: Breaking problems down
### Lesson 12: Writing a full problem statement
### Date: Jan 25 - 2026

# Example
# Title: Grade Average Calculator
# Purpose: Calculate a student’s final average and letter grade from several scores.

# Assumptions:
# - All scores are integers from 0 to 100 inclusive
# - The program will receive a list of different scores

# Constraints:
# - only standard Python with console input/output
# - scores can not be negative

# Success Criteria:
# - Calculate average score from a non-empty list of integers between 0 and 100 inclusive
# - Return both the average score and the letter grade based on the average score scaled from A-F

# Example I/O:
# - Input: [80, 90, 100]
#   Output: average = 90, letter = 'A'
# - Input: [80, 65, 75]
#   Output: average = 73, letter = 'C'
# - Input: [65, 50, 70]
#   Output: average = 62, letter = 'D'

# Sub-problems:
# 1) Receive a non-empty list of integer scores (0–100).
# 2) Compute the numeric average of the scores.
# 3) Map the average to a letter grade using the A–F scale.
# 4) Return both the average and the letter grade.


def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    average_score = total/ len(scores)
    return round(average_score)
    
print(calculate_average([80, 90, 100]))
print("avg 1:", calculate_average([80, 90, 100]))
print("avg 2:", calculate_average([80, 65, 75]))
print("avg 3:", calculate_average([65, 50, 70]))

assert calculate_average([80, 90, 100]) == 90
assert calculate_average([80, 65, 75]) == 73
assert calculate_average([65, 50, 70]) == 62

print("All average tests passed!")

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

assert get_letter_grade(90) == "A"
assert get_letter_grade(73) == "C"
assert get_letter_grade(62) == "D"

print("All letter-grade tests passed!")
