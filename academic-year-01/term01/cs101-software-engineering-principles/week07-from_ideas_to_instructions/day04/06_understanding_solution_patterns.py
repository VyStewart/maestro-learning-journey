### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 06: Understanding common solution patterns
### Date: Jan - 16 - 2026

## Pattern: Using dictionary lookup instead of long if/elif chains
# Example
day = "Wednesday"

open_hours = {
    "Monday": "9-5",
    "Tuesday": "9-5",
    "Wednesday": "10-6",
    "Sunday": "Closed"
}

hours = open_hours.get(day, "Unknown")
print(hours)

# Build a grade-message lookup using a dictionary
grade = "B"

message = {
    "A": "Exellent",
    "B": "Good",
    "C": "Fair"
}

message["D"] = "Fail"

final = message.get(grade, "Invalid grade")
print(final)

