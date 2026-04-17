### Maestro Challenge
### Topic: Printing and Oragizing and simple invoice
### Date: April 16 - 2026

'''
Creating a simple invoice by splititing responsibilities into 
reusable functions. The invoice will include item names, quantities, prices, 
and a total amount.
'''

def print_items(items):
    """Print item lines and return the total amount"""
    total = 0
    for item, qty, price in items:
        print(f"{item:8} {qty:4}  ${price}")
        total += price * qty

    return total

def print_invoice(customer, items):
    """Print the whole invoice for a customer"""
    print(f"Invoice for {customer}")
    print("Item     Qty   Price")
    total = print_items(items)
    print("-" * 20)
    print(f"Total: ${total}")


items = [("apple", 2, 3), ("banana", 1, 1)]
print_invoice("Vy", items)