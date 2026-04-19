### Course: Python 103 - Object-Oriented Programming
### Topic: Object Identity and Equality
### Date: April 19 - 2026

# This script demonstrates the concepts of object identity (is) and equality (==) in Python.
class Cart:
    pass

# One cart, two names (aliases)
cart1 = Cart()
cart2 = cart1

# Another, separate cart
cart3 = Cart()

print("cart1 is cart2:", cart1 is cart2)
print("cart1 is cart3:", cart1 is cart3)

# Give cart1 and cart3 the same "items" list
cart1.items = ["apple", "orange"]
cart3.items = ["apple", "orange"]

print("cart1.items == cart3.items:", cart1.items == cart3.items)
print("cart1.items is cart3.items:", cart1.items is cart3.items)

# Now mutate through cart1
cart1.items.append("banana")

print("cart1.items:", cart1.items)
print("cart2.items:", cart2.items)
print("cart3.items:", cart3.items)