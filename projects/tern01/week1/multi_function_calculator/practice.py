# Week 1 – Multi-Function Calculator

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


# 3. Ask for a number and check if it's even or odd
# 4. Ask for meal cost and calculate tax + tip
# 5. Show results with rounding and formatting

