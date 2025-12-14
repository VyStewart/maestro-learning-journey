### Lesson: Elif and refactoring nested decisions.
### Date: 12-13-2025

## Example flattening
# Example 1: Using to check age
age = 16

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")
    
# Example 2: Deciding ticket prices with logic first TRUE wins
age = 70

if age >= 65:
    print("Senior ticket")
elif age >= 18:
    print("Adult ticket")
else:
    print("Child Ticket")

# Example 3: nested if and flattening
role = "member"
paid = True

if role == "admin":
    print("Full access")
elif role == "member" and paid:
    print("Standard access")
elif role == "member" and paid is False:
    print("Limited access")
else:
    print("Guest access")
    
# Shipping options based on country and order total
country = "USA"
total = 120

if country == "USA" and total >= 100:
    print(" Free shipping (USA)")
elif country == "USA":
    print("Standard shipping (USA)")
elif total >= 150:
    print("Discount international shipping") 
else:
    print("Full-price international shipping")
    
## Challenge
# Game difficulty lables
# Nested version

level = 12

if level >= 20:
    print("Expert")
else:
    if level >= 10:
        print("Advanced")
    else:
        if level >= 5:
            print("Intermediate")
        else: 
            print("Beginner")
            
# flatten version

level = 12

if level >= 20:
    print("Expert")
elif level >= 10:
    print("Advanced")
elif level >= 5:
    print("Intermediate")
else:
    print("Beginner")
    
## Challenge 
# Using age to decide the ticket prices

age = 27

if age >= 65:
    print("Senior discount ticket")
else:
    if age >= 18:
        print("Adult ticket")
    else:
        if age >= 5:
           print("Child ticket")
        else:
            print("Free ticket")

age = 70

if age >= 65:
    print("Senior discount ticket")
elif age >= 18:
    print("Adult ticket")
elif age >= 5:
    print("Child ticket")
else:
    print("Free ticket")

