### Maestro Challenge
### Course: Python101
## Date: Feb 03 - 2026

# if/elif/else 
'''
Write Python branching (if/elif/else) that:
Takes an age variable,
Prints the correct price for that age.
'''

def ticket_price(age):
    if not isinstance(age, int):
        return None
    
    if age < 0 or age > 130:
        return None
    
    if age <= 3:
        return 0
    elif age <= 12:
        return 10
    elif age <= 64:
        return 20
    else:
        return 15

# Example     
ticket_age = 36
result = ticket_price(ticket_age)


if result is None:
    print("\nAge must be an integer between 0 and 130")
else:
    print(f"Ticket costs: ${result}")
    
# test call
test_age = "twenty" 
test = ticket_price(test_age) 
 
if test is None:
    print("\nAge must be an integer between 0 and 130")

else:
    print(f"\nTcket costs: ${test}")
        
