# Week 01 Notes – Python Foundations

## Overview
This week I completed Days 1–6 of Maestro’s PY101. I learned Python fundamentals including printing, variables, types, type casting, math operations, modulo, rounding, formatting, user input, and debugging with tracebacks. This week established the foundation for everything I will build in the coming weeks.

---

## Day 01 — Printing & Basic Output
- Learned `print()` as the main way Python displays information.
- Printed multiple values using:
  - commas → `print("Hello", "World")`
  - plus → `"Hello" + "World"`
  - multiplication → `"Ha" * 3`
- Practiced writing small multi-line programs.

---

## Day 02 — Variables & Text
- Variables store information using names and values.
- Python assigns using `=`.
- Practiced naming rules, descriptive variable names, and updating variables.
- Worked with strings (text) and learned simple concatenation.
- Avoided mixing strings with numbers without conversion.

---

## Day 03 — Numbers, Math, and Real-World Calculations
- Used `+ - * / // %` for math.
- Modeled real costs:
  - ticket purchases
  - snack totals
  - daily → monthly calculations
- Practiced multiple versions (simple + professional style).
- Built my own restaurant/tip calculator using rounding and f-strings.

---

## Day 04 — Division, Modulo, Rounding, Money Formatting
- `/` → normal division  
- `//` → quotient (whole number)  
- `%` → remainder  
- Used modulo to identify cycles (0 → 1 → 2 → repeat) and even/odd.
- Learned `round(number, decimals)`.
- Learned money formatting: `f"${total:.2f}"`.
- Built multiple tools: bill calculator, mpg calculator, and study time converter.

---

## Day 05 — Types, Casting, and User Input
- Every value has a type: `str`, `int`, `float`, `bool`.
- `type()` shows what Python believes the type is.
- Learned type casting:
  - `int("10")`
  - `float("4.5")`
  - `str(25)`
- Learned that `input()` ALWAYS returns a `str`.
- Built multiple interactive mini-tools:
  - cookie counter
  - gas mileage calculator
  - study time → hours converter

---

## Day 06 — Type Casting + Tracebacks + Debugging
- Combined multiple conversions in a single program.
- Practiced mixing numeric and string results.
- Learned how Python errors (tracebacks) work.
  - Line number  
  - Error type  
  - Explanation  
- Learned **TypeError**: happens when mixing incompatible types.
- Debugging flow:
  1. Read traceback  
  2. Find the line  
  3. Identify wrong type  
  4. Convert properly  
  5. Re-run  
- Gained confidence: mistakes are part of growth, not failure.

## Day 7 - Practice + Review

### Important Note on Division
In Python, using `/` always produces a float — even when the result is a whole number.
Example:
7 / 1 → 7.0
20 / 5 → 4.0
This is normal behavior and helps Python stay consistent with numeric types.

### Using Math Inside f-Strings vs. Storing Values in Variables
I learned that Python allows me to perform math directly inside an f-string, or I can assign the results to variables first to make my code cleaner and easier to read.

Example:

# Direct math inside print()
print("Row:", 28 // 6, "Leftover:", 28 % 6)

# Direct math inside an f-string
print(f"Row: {28 // 6} Leftover: {28 % 6}")

# Using variables to improve clarity
row = 28 // 6
leftover = 28 % 6
print(f"Row: {row} Leftover: {leftover}")

### Three Ways to Format Money in Python (Showing $54.99 Exactly)

I learned that Python can display money values in multiple ways. Here are three different methods to show the value **54.99** exactly:

#### 1. Using round()
num = 54.987
print(round(num, 2))     # → 54.99

### 2. Using f-string with .2f
num = 54.987
print(f"${num:.2f}")     # → $54.99

### 3. Using the format function
num = 54.987
print("${:.2f}".format(num))   # → $54.99

### Python Displays Full Float Precision When Printing Numbers

I learned that when I print a raw float value in Python, such as:
print(total)

Example:
total = 10.1 + 44.89
print(total)       # Python may show 54.9899999999995

To display a clean money value, I must format it using one of these methods:
round(total, 2)
f"{total:.2f}"
"${:.2f}".format(total)
These methods ensure Python prints exactly $54.99, even if the underlying float contains many more decimal digits.
---

## What I Built in Week 1
- Bill calculator  
- Tip calculator  
- MPG calculator  
- Cookie tracker  
- Study time → hours converter  
- Type conversion challenge  
- Error experiments with intentional tracebacks  

These practical exercises deepened my understanding and helped me think like a developer.

---

## Reflection
This week transformed my relationship with coding. I learned:

- how to read errors calmly  
- how to fix mistakes through type conversion  
- how to use f-strings professionally  
- how to build real mini-tools  
- how to think in small, clear steps  

I feel confident moving into Week 2 and ready to begin my Week 1 projects.
