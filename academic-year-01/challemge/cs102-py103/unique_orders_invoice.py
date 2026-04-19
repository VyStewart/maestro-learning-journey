### Maestro Challenge
### Topic: Uniques Orders Invoice without Duplicates using Stack
### Date: April 18 - 2026

'''
Unique Orders Invoice Challenge

This script demonstrates a mini-app for processing and invoicing customer orders:

- Removes duplicate orders by order_id, keeping only the first instance
- Uses a custom Stack class to store unique orders for processing
- Pops each order off the stack and prints a formatted invoice, including each item, quantity, and price

This challenge blends data filtering, object-oriented programming, and real-world workflow organization.
'''

orders = [
    {
        "order_id": 101,
        "items": [
            {"item": "apple", "quantity": 2, "price": 3},
            {"item": "orange", "quantity": 1, "price": 4}
        ]
    },
    {
        "order_id": 203,
        "items": [
            {"item": "banana", "quantity": 3, "price": 2}
        ]
    },
    {
        "order_id": 101,
        "items": [
            {"item": "kiwi", "quantity": 5, "price": 1}
        ]
    },
    {
        "order_id": 108,
        "items": [
            {"item:": "mango", "quantity": 6, "price": 1.5},
            {"item": "water melon", "quantity": 1, "price": 4}
        ]
    }
]

def find_unique_orders(orders):
    seen_ids = set()
    unique_orders = []

    for order in orders:
        if order["order_id"] not in seen_ids:
            unique_orders.append(order)
            seen_ids.add(order["order_id"])

    return unique_orders

unique_orders = find_unique_orders(orders)
print(unique_orders)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError ("Pop from an empty stack.")

    def is_empty(self):
        return len(self.items) == 0

# Now push each unique order onto the stack
stack = Stack()
for order in unique_orders:
    stack.push(order)

# Pop each order and print an invoice using while loop
while not stack.is_empty():
    order = stack.pop()
    print(f"Invoice for order {order['order_id']}:")
    for item_detail in order["items"]:
        name = item_detail.get("item") or item_detail.get("item:")
        qty = item_detail["quantity"]
        price = item_detail["price"]
        print(f"  {name}: qty={qty}, price=${price}")
    print("-" * 20)
