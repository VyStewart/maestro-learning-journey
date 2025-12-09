# Day 04 - Division, Modulo, Rounding & Money Formatting

# 1. Division modes: / vs // vs %

print("=== Basic division modes ===")
print("7 / 3  =", 7 / 3)    # exact decimal division
print("7 // 3 =", 7 // 3)   # whole number division (quotient)
print("7 % 3  =", 7 % 3)    # remainder

print()  # blank line for readability

# 2. Real-world example: sharing apples with friends

apples = 22
friends = 6

exact_share = apples / friends          # exact division
whole_apples_each = apples // friends   # quotient
leftover_apples = apples % friends      # remainder

print("=== Apples & friends example ===")
print("Total apples:", apples)
print("Total friends:", friends)
print("Each friend gets (exact):", exact_share)
print("Each friend gets (whole apples):", whole_apples_each)
print("Leftover apples:", leftover_apples)

print()

# 3. Modulo in practice: parity (even/odd)

print("=== Even / Odd check with modulo ===")
number1 = 10
number2 = 11

print(number1, "is even?", number1 % 2 == 0)
print(number2, "is even?", number2 % 2 == 0)

print()

# 4. Modulo in practice: simple cycle with % 3

print("=== Simple cycle with % 3 ===")
for i in range(10):
    print(i, "→", i % 3)

print()

# 5. Rounding and money formatting

print("=== Rounding and money formatting ===")
subtotal = 35.50
tax_rate = 0.0825  # 8.25% tax

tax = subtotal * tax_rate
total = subtotal + tax

print("Raw total:", total)
print("Rounded total (round):", round(total, 2))
print(f"Formatted total: ${total:.2f}")

# Another money example
salary = 3575.4571
print(f"Monthly salary (raw): {salary}")
print(f"Monthly salary (formatted): ${salary:.2f}")


# Using rounding and money format to built a mini calculator

meal_subtotal = 24.89
tax = meal_subtotal * 0.08
tip = meal_subtotal * 0.18

round_tax = round(tax, 2)
round_tip = round(tip, 2)

meal_total = meal_subtotal + tax + tip

print(f"Meal Subtotal: ${meal_subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(F"Tip: ${tip:.2f}")
print(f"Meal Total: ${meal_total:.2f}")
