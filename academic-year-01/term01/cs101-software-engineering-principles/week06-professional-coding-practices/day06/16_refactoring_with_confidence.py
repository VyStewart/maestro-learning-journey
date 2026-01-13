### CS101 - Week 06
### Software Engineering Principles
### Lesson 16: Refactoring with confidence
### Date: Jan 11 2026

# Before
def total_price(p,q,t):
    subtotal = p * q
    tax_amount = subtotal * t
    final = subtotal + tax_amount
    print("Final price:", final)

total_price(10, 3, 0.07)

# After 
def calculate_tax(subtotal, tax_rate):
    tax_amount = subtotal * tax_rate
    return tax_amount

def calculate_total_price(p,q,t):
    subtotal = p * q
    tax_amount = calculate_tax(subtotal, t)
    final = subtotal + tax_amount
    print("Final price:", final)

calculate_total_price(10, 3, 0.07)