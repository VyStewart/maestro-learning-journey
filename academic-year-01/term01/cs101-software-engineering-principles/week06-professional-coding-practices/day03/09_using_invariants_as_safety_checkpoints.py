### CS101 - Week 06
### Software Engineering Principles
### Lesson 09: Using Invariants as Safety Checkpoints
### Date: Jan 07 2026

## invariant check using assert.
## assert infore the rules ad crash early if the rules're broken

# Example with posstive value
balance = 10
assert balance >= 0, "Balance should never be negative"
print("After assert: program still running")

# Example with negative value
balance = -5
assert balance >= 0, "Balance should never be negative"
print("After assert: program still running")

# add invariants in a function
def sum_positive(numbers):
    # 1) Pre-condition, invariant: numbers should be a list
    assert isinstance(numbers, list), "number must be a list"
    total = 0
    for n in numbers:
        if n > 0:
            total += n
     # 2) Post-condition, invariant: total should never be negative
    assert total >= 0, "total should never be negative"

    return total

# Practice:
temperature = 80
name = "Joshua"

assert temperature <= 100, "temperature should always below 100"
assert len(name) > 0, "name must not be empty"

print(" All invariants passed")
   