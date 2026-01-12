### CS101 - Week 06
### Software Engineering Principles
### Lesson 15: The art of well_place error
### Date: Jan 11 2026

def price_or_none(quantity, unit_price):
    if quantity < 0:
        return None
    return quantity * unit_price

def price_or_error(quantity, unit_price):
    if quantity < 0:
        raise ValueError(f"Quantity must be non-negative, got {quantity}")

print("Using sentinel None:")
result1 = price_or_none(-3, 10)
print("Result:", result1)

print("\nUsing exception:")
try:
    result2 = price_or_error(-3, 10)
    print("Result:", result2)
except ValueError as e:
    print("Caught error:", e)