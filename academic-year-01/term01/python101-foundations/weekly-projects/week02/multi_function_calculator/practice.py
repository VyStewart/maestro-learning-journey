#1. Ask for how long does it take to bake a batch of cookies.
print("----- Baking Time Calculator -----")

minutes_per_batch = int(input("How many minutes do you need to bake one batch of cookies? "))
batches_per_day = 20
total_minutes = minutes_per_batch * batches_per_day
full_hours = total_minutes // 60
remain_minutes = total_minutes % 60
hours_label = "hour" if full_hours == 1 else "hours"
minutes_label = "minute" if remain_minutes == 1 else "minutes"

print(f"You need {full_hours} {hours_label} and {remain_minutes} {minutes_label} to bake {batches_per_day} batches of cookies.")


# 2. Ask for cookies per day and estimate per month for a small bakery
# They can sell cookies by individual or by box ( 9 per box)

print("\n--------Daily Inventory Calculator-------")
baked_cookies = int(input("How many cookies do you bake every day? "))
sales_cookies = int(input("How many cookies do you sell per day? "))

full_box = sales_cookies // 9
remain_cookies = sales_cookies % 9
leftover_cookies = baked_cookies - sales_cookies

full_box_label = "box" if full_box == 1 else "boxes"
remain_cookies_label = "cookie" if remain_cookies == 1 else "cookies"
leftover_cookies_label = "cookie" if leftover_cookies == 1 else "cookies"

print(f"You sell {full_box} {full_box_label} and {remain_cookies} {remain_cookies_label} every day."
      f" And the leftover is {leftover_cookies} {leftover_cookies_label}.")

# 3. Ask for a number and check if it's even or odd using batches of cookies need to be backed daily.
# a batch = 15 cookies

print("\n--------Check even or odd batch-------")

cookies = int(input("How many of cookies do we need to bake today? "))
batched_cookies = cookies // 15
batched_label = "batches" if batched_cookies != 1 else "batch"
if batched_cookies % 2 == 0:
    print(f"You bake {batched_cookies} {batched_label} today. The workload is balanced between both ovens.")
else:
    print(f"You bake {batched_cookies} {batched_label} today. One oven needs to handle an extra batch.")

# Week 01 - Simple Bill Calculator

each_cookie = 2.49
quantity = 20
tax_rate = 0.085  # 8.5% tax

bill_amount = each_cookie * quantity
tax_amount = bill_amount * tax_rate
total_bill = bill_amount + tax_amount

print("\n----- Cookie Bill -----")
print(f"Price per cookie: ${each_cookie:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${bill_amount:.2f}")
print(f"Tax (8.5%): ${tax_amount:.2f}")
print(f"Total Bill: ${total_bill:.2f}")
