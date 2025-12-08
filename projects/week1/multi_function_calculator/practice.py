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


# 2. Ask for cookies per day and estimate per month
# 3. Ask for a number and check if it's even or odd
# 4. Ask for meal cost and calculate tax + tip
# 5. Show results with rounding and formatting

