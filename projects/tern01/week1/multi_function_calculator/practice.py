# Week 1 – Multi-Function Calculator
"""
# 1. Ask user for minutes and convert to hours
study_time = input("How many minutes do you study Python per day? ")
study_time_num = float(study_time)
study_hour = study_time_num / 60

print(f"You study {study_hour:.2f} hours a day")

study_time = float(input("How many minutes do you study Python every day? "))
study_hour = study_time / 60

print(f"You study {study_time} minutes, which is {study_hour:.2f} hours.")

study_time = float(input("How long do you study Python everyday? "))
full_hours = int(study_time)// 60
remain_minutes = int(study_time) % 60

print(f"You study {full_hours} hours and {remain_minutes} minutes a day.")

"""
minutes_per_batch = int(input("How many minutes do you need to bake one batch of cookies? "))
batches_per_day = 20
total_minutes = minutes_per_batch * batches_per_day
full_hours = total_minutes // 60
remain_minutes = total_minutes % 60
hours_label = "hour" if full_hours == 1 else "hours"

minutes_label = "minute" if remain_minutes == 1 else "minutes"

print(f"You need {full_hours} {hours_label} and {remain_minutes} {minutes_label} to bake {batches_per_day} batches of cookies.")
"""""
# 2. Ask for cookies per day and estimate per month for a small bakery
# They can sell cookies by individual or by box ( 9 per box)

baked_cookies = int(input("How many cookies did you bake every day? "))
sales_cookies = int(input("How many cookies do you sell every day? "))
full_box = sales_cookies // 9
remain_cookies = sales_cookies % 9
left_over = baked_cookies - sales_cookies

full_box_label = "box" if full_box == 1 else "boxes"
remain_cookies_label = "cookie" if remain_cookies == 1 else "cookies"

print(f"You sell {full_box} {full_box_label} and {remain_cookies} {remain_cookies_label}. The leftover is {left_over} {remain_cookies_label} every day.")

# 3. Ask for a number and check if it's even or odd.
# a batch = 15 cookies
cookies = int(input("How many of cookies do we need to bake today? "))
batched_cookies = cookies // 15
batched_label = "batches" if batched_cookies != 1 else "batch"
if batched_cookies % 2 == 0:
    print(f"You bake {batched_cookies} {batched_label} today. The workload is balanced between both ovens.")
else:
    print(f"You bake {batched_cookies} {batched_label} today. One oven needs to handle an extra batch.")
    


# 4. Ask for meal cost and calculate tax + tip
# 5. Show results with rounding and formatting

"""