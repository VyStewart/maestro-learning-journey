### CS101:  Software Engineering Principles
### Week 08: Breaking problems down
### Lesson 10: Assembling functions into pipelines
### Date: Jan 25 - 2026

# Example: three independent calls
def minutes_to_hours(m):
    return m / 60

def hours_to_days(h):
    return h / 24

def format_days(d):
    return f"{d:.2f} day(s)"

print(minutes_to_hours(120))
print(hours_to_days(48))
print(format_days(2))

# Connect 3 separate functions into 1 single pioeline using nested calls
print(format_days(hours_to_days(minutes_to_hours(2880))))

# Using chained with variables
def minutes_to_hours(m):
    return m / 60

def hours_to_days(h):
    return h / 24

def format_days(d):
    return f"{d:.2f} day(s)"

def round_up_days(d):
    # round days up to the next whole day
    return int(d + 0.9999)

mins = 4500
hours = minutes_to_hours(mins)
days = hours_to_days(hours)
rounded_day = round_up_days(days)
print(format_days(rounded_day))

