### CS102 - Data structures & algorithms 
### Week 03 - A;gorithms analysis
### Date: March 22 - 2026

# Safe algorithms and handling edge cases

def safe_average(numbers):
    # Check if input is a list and not empty
    if not isinstance(numbers, list):
        return None
    if len(numbers) == 0:
        return None

    total = 0
    # loop through numbers and check if each element is a number
    for n in numbers:
        if not isinstance(n, (float, int)):
            return None
        total += n
    # return the average
    return total / len(numbers)

# Test cases
print(safe_average([1, 2, 6]))        # normal
print(safe_average([1, "a", 3]))      # bad element
print(safe_average([]))               # empty
print(safe_average("abc"))            # wrong type
print(safe_average(None))             # None


# Sae algorithms and handling edge cases with negative numbers
def first_positive(numbers):
    if not isinstance(numbers, list):
        return None
    if len(numbers) == 0:
        return None

    for num in numbers:
        if not isinstance(num, (int, float)):
            return None
        if num > 0:
            return num

print(first_positive([0, -3, 5, 2]))   # normal → 5
print(first_positive([]))              # empty → None
print(first_positive("abc"))           # wrong type → None
print(first_positive([0, "a", 3]))     # bad element → None
