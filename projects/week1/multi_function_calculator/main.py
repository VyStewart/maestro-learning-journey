# Week 1 - Multi-Function Calculator
# Author: Vy S
# Description: Small tools for daily life (study time, cookies, etc.)

# Description: Small tools for daily life (study time, cookies, etc.)

print("----- Study Time Calculator -----")

study_time = int(input("How many minutes do you spend on studying Python every day? "))
full_hours = study_time // 60
remain_minutes = study_time % 60

hour_label = "hour" if full_hours == 1 else "hours"
minute_label = "minute" if remain_minutes == 1 else "minutes"

print(f"You study {full_hours} {hour_label} and {remain_minutes} {minute_label} every day.")
