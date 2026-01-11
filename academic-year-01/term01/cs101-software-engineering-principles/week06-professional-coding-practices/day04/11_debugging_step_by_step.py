### CS101 - Week 06
### Software Engineering Principles
### Lesson 11: Debugging step by step
### Date: Jan 08 2026

# Example:
def parse_price(text):
    parts = text.split("$")
    amount_text = parts[1]
    return float(amount_text)

def total_cart(prices):
    total = 0
    for p in prices:
        total += parse_price(p)
    return total

cart = ["$10", "$5.50", "free", "$3"]
print("Cart total:", total_cart(cart))

# Tracing and fixing errors

def parse_price(text):
    print("parse_price called with:", text)
    parts = text.split("$")
    print("part is:", parts)

    if len(parts) < 2:
        return 0.0
        
    amount_text = parts[1]
    return float(amount_text)

def total_cart(prices):
    total = 0
    for p in prices:
        total += parse_price(p)
    return total

print(parse_price("free"))

cart = ["$10", "$5.50", "free", "$3"]
print("Cart total:", total_cart(cart))

# Clean up tracing/ asserts, retest, and documents fix

def parse_price(text):
    print("parse_price called with:", text)
    parts = text.split("$")
    print("part is:", parts)

    if len(parts) < 2:
        return 0.0

    amount_text = parts[1]
    return float(amount_text)

def total_cart(prices):
    total = 0
    for p in prices:
        total += parse_price(p)
    return total

print(parse_price("free"))

cart = ["$10", "$5.50", "free", "$3"]
print("Cart total:", total_cart(cart))




