### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 12: Creating test tables for pseudocode plans
### Date: Jan 17 - 2026

# Example: 
def classify_score(score):
    # Rule 1: Invalid input
    if score < 0:
        return "error"

    # Rule 2: Passing score
    if score >= 60:
        return "pass"

    # Rule 3: Everything else is failing
    return "fail"

# Invalid input
assert classify_score(-1) == "error"

# Boundary around passing
assert classify_score(59) == "fail"
assert classify_score(60) == "pass"
assert classify_score(61) == "pass"

# Typical cases
assert classify_score(40) == "fail"
assert classify_score(75) == "pass"



