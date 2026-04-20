### Course: Python 103 - Object-Oriented Programming
### Topic: Self Parameter and Methods that Use Attributes
### Date: April 19 - 2026

class Phone:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def display_info(self):
        print(f"My phone is an {self.brand} and its a {self.model} and the color is {self.color}.")
 
# Example usage       
phone = Phone("Apple", "iPhone 14 Pro Max", "Deep Purple")
phone.display_info()

# Now let's change the model and color of the phone and display the info again
phone = Phone("Apple", "iPhone 15 Pro Max", "Deep Blue")
phone.display_info()