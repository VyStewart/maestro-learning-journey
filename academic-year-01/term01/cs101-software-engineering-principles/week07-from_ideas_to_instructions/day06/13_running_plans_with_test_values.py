### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 13: Running plans with test values
### Date: Jan 18 - 2026

# Example: Ask for score
def classify_score(score):
    """
    Rules (in order):
    1) If score < 0 → "error"
    2) If score >= 60 → "pass"
    3) Otherwise → "fail"
    """
    if score < 0:
        return "error"
    elif score >= 60:
        return "pass"
    else:
        return "fail"
    
# Boundary and edge cases (dry-run verified)

assert classify_score(-1) == "error"   # invalid input
assert classify_score(0) == "fail"     # lowest valid score

assert classify_score(59) == "fail"    # just below pass
assert classify_score(60) == "pass"    # passing boundary
assert classify_score(61) == "pass"    # just above pass

# Typical values
assert classify_score(40) == "fail"
assert classify_score(75) == "pass"

