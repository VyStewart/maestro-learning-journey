## Decision tables to branch
# Date: 12-14-2025

# Small decision table 
# Example 1: exam score

score = 89

if score >= 90:
    print("A")
elif score < 90 and score >= 60:
    print("Pass")
else:
    print("Fail")
    
# Example 2 - Simple shipping rule

order_total = 60
is_member = False

if order_total >= 50 and is_member:
    print("Free shipping")
elif order_total >= 50 and not is_member:
    print("$5 shipping")
elif order_total < 50 and is_member:
    print("$5 shipping")
else:
    print("$10 shipping")
    
# Example 3: ticket prices

age = 12

if age < 13:
    print("Child: $8")
elif age >= 65:
    print("Senior: $9")
else:
    print("Adult: $12")
    
# Challenge - Parking fee rules based on hours

hours = 4

if hours <= 1:
    print("Fee: $5")
elif hours <= 3:
    print("Fee: $10")
else:
    print("Fee $15 max")
    
# Challenge - Boss-level

cart_total = 120
has_coupon = True
is_vip = False

# Row 1
if cart_total >= 100 and has_coupon and is_vip:
    print("30% discount")
#Row 2
elif cart_total >= 100 and has_coupon and not is_vip:
    print("25% discount")
#Row 3
elif cart_total >= 100 and not has_coupon and is_vip:
    print("20% discount")
#Row 4
elif cart_total >= 100 and not has_coupon and not is_vip:
    print("10% discount")
#Row 5
elif cart_total < 100 and has_coupon and is_vip:
    print("15% discount")
#Row 6
elif cart_total < 100 and has_coupon and not is_vip:
    print("10% discount")
#Row 7
elif cart_total < 100 and not has_coupon and is_vip:
    print("5% discount")
#Row 8
else:
    print("No discount")

