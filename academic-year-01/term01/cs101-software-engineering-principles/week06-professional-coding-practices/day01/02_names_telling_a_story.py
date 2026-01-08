### CS101 - Week 06
### Software Engineering Principles
### Lesson 02: Naming that tells a story
### Date: Jan 05 2026

## Names that tell a story

# Functions use noun variables
player1_points = 12
player2_points = 8
lost_points = player1_points - player2_points

print("Points player 1 lost:",lost_points)

# Functions use verb name(action)
def calculate_price(eggs_price, milk_price):
    total_price = eggs_price + milk_price
    return total_price

result = calculate_price(3, 5)
print(f"\nThe total price of eggs and milk are: ${result}")

# Renaming existing code safely (variables or function)

# Original:
def f(s, t):
    u = s - t
    return u

x = 100
y = 30
z = f(x, y)

# Rename:
def calculate_money(account_balance, money_spent):
    remaining_money = account_balance - money_spent
    return remaining_money

account_balance = 100
money_spent = 30
result = calculate_money(account_balance, money_spent)
print(result)
