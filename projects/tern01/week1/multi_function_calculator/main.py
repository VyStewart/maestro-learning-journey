# Week 1 - Multi-Function Calculator
# Author: Vy S
# Description: Small tools for daily life (study time, cookies, etc.)

# Description: Small tools for daily life (study time, cookies, etc.)
"""
print("----- Study Time Calculator -----")

study_time = int(input("How many minutes do you spend on studying Python every day? "))
full_hours = study_time // 60
remain_minutes = study_time % 60

hour_label = "hour" if full_hours == 1 else "hours"
minute_label = "minute" if remain_minutes == 1 else "minutes"

print(f"You study {full_hours} {hour_label} and {remain_minutes} {minute_label} every day.")

"""
# 2. Ask for cookies per day and estimate per month for a small bakery
# They can sell cookies by individual or by box ( 9 per box)

print("--------Daily Invetory Calculator-------")
baked_cookies = int(input("How many cookies do you bake every day? "))
sales_cookies = int(input("How many cookies do you sell per day? "))

full_box = sales_cookies // 9
remain_cookies = sales_cookies % 9
leftover_cookies = baked_cookies - sales_cookies

full_box_label = "box" if full_box == 1 else "boxes"
remain_cookies_label = "cookie" if remain_cookies == 1 else "cookies"
lefover_cookies_label = "cookie" if leftover_cookies == 1 else "cookies"

print(f"You sell {full_box} {full_box_label} and {remain_cookies} {remain_cookies_label} every day."
      f" And the leftover is {leftover_cookies} {lefover_cookies_label}.")

# 3. Ask for a number and check if it's even or odd using batches of cookies need to be backed daily.
# a batch = 15 cookies
cookies = int(input("How many of cookies do we need to bake today? "))
batched_cookies = cookies // 15
batched_label = "batches" if batched_cookies != 1 else "batch"
if batched_cookies % 2 == 0:
    print(f"You bake {batched_cookies} {batched_label} today. The workload is balanced between both ovens.")
else:
    print(f"You bake {batched_cookies} {batched_label} today. One oven needs to handle an extra batch.")
