### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 04: Turning rules into code
### Date: Jan - 15 - 2026

# Example: Turning rules into code
"""
    Problem (plain English):
    1) Start a counter at 0
    2) Repeatedly ask the user for a number
    3) Stop when the user enters 0
    4) Count how many of the entered numbers were even
    5) Print the final count
"""

def count_evens_until_zero():
    even_count = 0

    # 1) Repeat until sentinel is entered
    while True:
        # 1.1) Ask for a number
        number = int(input("Enter a number (0 to stop): "))

        # 1.2) If number is 0, stop
        if number == 0:
            break

        # 1.3) If number is even, add to count
        if number % 2 == 0:
            even_count += 1

    # 2) Print the final count
    print(f"Even numbers entered: {even_count}")

count_evens_until_zero()

    