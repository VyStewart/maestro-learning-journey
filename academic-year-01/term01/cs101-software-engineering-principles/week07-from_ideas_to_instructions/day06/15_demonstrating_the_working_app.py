### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 15: Demonstrating the working app
### Date: Jan 18 - 2026

# Example
def get_ticket_price(age):
    if age < 13:
        return 8
    elif age < 18:
        return 10
    elif age < 65:
        return 12
    else:
        return 7

while True:
    age_text = input("Enter your age: ")

    try:
        age = int(age_text)
    except ValueError:
        print("Please enter your age as a whole number.")
        continue

    if age < 0:
        print("Age cannot be negative.")
        continue

    break

# --- tests ---

# T-01: child under 13
assert get_ticket_price(5) == 8

# T-02: teen 13–17
assert get_ticket_price(15) == 10

# T-03: adult 18–64
assert get_ticket_price(30) == 12

# T-04: senior 65+
assert get_ticket_price(70) == 7

print("All demo tests passed ✅")

# A clean, professional version
def get_ticket_price(age):
    """Return ticket price based on age rules."""
    if age < 13:
        return 8
    elif age < 18:
        return 10
    elif age < 65:
        return 12
    else:
        return 7

# --- demonstration tests (logic verification) ---
assert get_ticket_price(5) == 8      # child
assert get_ticket_price(15) == 10    # teen
assert get_ticket_price(30) == 12    # adult
assert get_ticket_price(70) == 7     # senior

# --- application flow (input boundary + output) ---
while True:
    age_text = input("Enter your age: ")

    try:
        age = int(age_text)
    except ValueError:
        print("Please enter your age as a whole number.")
        continue

    if age < 0:
        print("Age cannot be negative.")
        continue

    break

print(f"Your ticket costs: ${get_ticket_price(age)}")
