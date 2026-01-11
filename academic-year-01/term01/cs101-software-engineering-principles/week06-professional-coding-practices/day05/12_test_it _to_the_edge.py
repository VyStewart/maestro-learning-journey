### CS101 - Week 06
### Software Engineering Principles
### Lesson 12: Test it to the Edge
### Date: Jan 10 2026

# Example

def cart_total(prices): 
    total = prices[0]
    for price in prices[1:]:
        total += price
    return total

print("Non-empty:", cart_total([10, 20, 5]))
print("Empty:", cart_total([]))

# Adding the the validation for the list 

def cart_total(prices):
    if len(prices) == 0:
        return 0.0

    total = prices[0]
    for price in prices[1:]:
        total += price
    return total

assert cart_total([10, 20, 5]) == 35
assert cart_total([]) == 0.0
assert cart_total([10]) == 10
    
print("Non-empty:", cart_total([10, 20, 5]))
print("Empty:", cart_total([]))