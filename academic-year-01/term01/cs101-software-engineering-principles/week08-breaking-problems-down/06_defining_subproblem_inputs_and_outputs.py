### CS101:  Software Engineering Principles
### Week 08: Breaking problems down
## Lesson 06: Defining subproblems inputs and outputs
### Date: Jan 22 - 2026

# Example:
def minutes_to_hours(total_minutes):
    hours = total_minutes / 60
    return hours

result = minutes_to_hours(150)
print(f"Study time: {result} hours")

# Practice:
def classify_score(score):
    if score < 0:
        return "error"
    elif score >= 75:
        return "pass"
    else:
        return "fail"

result = classify_score(55)
print(result)

# Practice:
def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        return "Invalid input"

    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

result = celsius_to_fahrenheit("twenty")
print(result)
