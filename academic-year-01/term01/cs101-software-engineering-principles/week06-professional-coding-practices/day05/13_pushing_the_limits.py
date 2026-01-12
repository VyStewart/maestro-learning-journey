### CS101 - Week 06
### Software Engineering Principles
### Lesson 13: Pushing the limits
### Date: Jan 10 2026

# Choosing < vs <=
def is_working_age(age):
    # Return TRue if age is between 13 and 64 inclusive. else False
    if age >= 13 and age <= 64:
        return True
    else:
        return False             

# Test - dont change yet
assert is_working_age(13) == True
assert is_working_age(64) == True
assert is_working_age(12) == False
assert is_working_age(65) == False

print("All tests passed")


# Example
def is_valid_username_length(length):
    # Return True if length is between 3 and 10 inclusive, else False
    if length >= 3 and length <= 10:
        return True
    else:
        return False

# Boundary tests:
assert is_valid_username_length(3) == True   # lower bound
assert is_valid_username_length(10) == True  # upper bound
assert is_valid_username_length(2) == False  # just below
assert is_valid_username_length(11) == False # just above
assert is_valid_username_length(4) == True   # just inside above lower
assert is_valid_username_length(9) == True   # just inside below upper

print("All tests passed")