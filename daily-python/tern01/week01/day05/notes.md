# Day 05 - Types, Conversions & User Input

### Concepts Learned
- Every value in Python has a **type** (string, int, float, bool).
- Use `type()` to check what type Python thinks a value is.
- Python does not allow mixing incompatible types (e.g., string + int).
- Conversion functions:
  - `int("30")` → 30
  - `float("3.14")` → 3.14
  - `str(2025)` → "2025"
- Converting types lets me perform math or build readable print statements.

---

### Type Checking
Examples I practiced:

```python
type("Vy")     # str
type(30)       # int
type(3.14)     # float
type(True)     # bool

This helps me understand why some operations fail and how to fix them.

Converting Values
I learned how to convert strings to numbers so I can do math:

age = int("30")
pi = float("3.14")
year_str = str(2025)

User Input (input())

I learned that:
. input() always returns a string, no matter what the user types.
. To do math with input, I must convert it:

num = int(input("Enter a number: "))
price = float(input("Enter a price: "))

Reflection
. Today I learned how to make Python programs interactive.
. Understanding types and conversions makes me feel more confident
 because I now understand why errors happen and how to fix them.
. Learning input() also made Python feel more “alive,”
 because my program can finally talk to the user.
