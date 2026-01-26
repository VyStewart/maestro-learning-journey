### CS101:  Software Engineering Principles
### Week 08: Breaking problems down
### Lesson 08: Matching subroblems to patterns
### Date: Jan 25 - 2026

## Most subproblems fit into a small set of patterns 
## Pattern is a coomon "shape" of code that sloves a common type of mini problem

# Pattern 01: [LOOKUP] using a dictionary
"""
 [LOOKUP] pattern = “I have a small fixed set of keys, and for each key 
 I want a specific value. If the key is missing, I might want a default.”   
"""
colors = {
    "R": "Red",
    "G": "Green",
    "B": "Blue",
    "P": "Purple"
}

code1 = "X"
code = "P"
message1 = colors.get(code1, "Unknown")
message2 = colors.get(code)

print(message1)
print(message2)


# Pattern 02: [ACCUULATOR]
"""
[ACCUMULATOR] pattern = “I need to keep a running total or running count while I loop.”
"""
total = 0

for number in [10, 20, 5]:
    total += number

print("Total of numbers is:", total)

# Pattern 03: [FLAG]
"""
[FLAG] pattern = “I just need to remember whether something ever happened in the loop 
(True/False).”
"""
found_long_word = False          # start flag

for word in ["hi", "welcome", "ok"]:
    if len(word) > 5:
        found_long_word = True   # flip the flag
        
if found_long_word:
    print("There was at least one long word.")
else:
    print("No long words found.")

# Example
has_negative = False

for num in [3, 0, -2, 7]:
    if num < 0:
        has_negative = True

if has_negative:
    print("List has a negative number.")
else:
    print("All numbers are non-negative.")
    
# Practice 
total_expense = 0

transactions = [50, -10, -5, 20, -30]

for num in transactions:
    if num < 0:
        total_expense += num

print(total_expense)

# Challegen:
scores = [10, 0, 5, 8]
total = 0
has_zero = False

for score in scores:
    if score >= 0:
        total += score
        
        if score == 0:
           has_zero = True 
       
print("Total:", total)

if has_zero:
    print("At least one score was 0")        
else:
    print("No zero scores")