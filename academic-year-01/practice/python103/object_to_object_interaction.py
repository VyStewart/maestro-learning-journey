### Maestro Challenge
### Topic: Object to Object Interaction
### Date: April 19 - 2026

"""
Simple coffee shop simulation using two classes: Barista and Order.

- Each Order object stores its own customer_name and drink.
- The Barista object prepares different orders by reading their attributes.
- Shows how separate objects keep their own data and interact through methods.

This practice helps understand how objects can have their own state and interact with each other.
"""

class Barista:
    """A class representing a barista who can prepare coffee orders."""
    
    def prepare_order(self, order):
        """Prepares a coffee order by reading the order's attributes."""
        print(f"I am preparing {order.drink} for {order.customer_name}.")
        
class Order:
    """A class representing a coffee order with customer name and drink type."""
    
    def announce_ready(self):
        """Announces that the order is ready."""
        print(f"Hi, {self.customer_name} and your {self.drink} is ready.")

barista = Barista()
order1 = Order()
order2 = Order()

order1.customer_name = "Josh"
order1.drink = "Macchiato"

order2.customer_name = "Marcus"
order2.drink = "Coffee"

barista.prepare_order(order1)
order1.announce_ready()

barista.prepare_order(order2)
order2.announce_ready()