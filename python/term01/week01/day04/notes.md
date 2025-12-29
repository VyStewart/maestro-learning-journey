# Day 04 - Division, Modulo, Rounding & Money Formatting

### Concepts Learned
- Normal division `/` gives a decimal (float) result.
- Floor division `//` gives only the whole number (quotient).
- Modulo `%` gives the remainder of a division.
- Modulo can be used for:
  - parity (even/odd)
  - cycles (repeating patterns)
  - positions inside a group
- `round(number, decimals)` rounds numbers to a specific number of decimal places.
- Money is usually shown with **2 decimal places** using formatting like `:.2f`.

---

### Division Modes Summary
Using `7` and `3` as an example:

- `7 / 3` → `2.3333333333` (exact decimal division)
- `7 // 3` → `2` (how many whole times 3 fits into 7)
- `7 % 3` → `1` (what is left over)

I also modeled a real-world example:

- `apples = 22`
- `friends = 6`
- `exact_share = apples / friends`
- `whole_apples_each = apples // friends`
- `leftover_apples = apples % friends`

This helped me see quotient and remainder as **real sharing**, not just math.

---

### Modulo in Practice
I used `%` to:

1. **Check even/odd (parity)**  
   - If `n % 2 == 0` → even  
   - If `n % 2 == 1` → odd  

2. **Create a simple cycle with `% 3`**  
   Using:

   ```python
   for i in range(10):
       print(i, "→", i % 3)


### F-String Money Formatting (Important Concept)

Today I learned how to use **f-strings** to format numbers as money in Python.

F-strings allow me to embed variables directly inside a string using `{ }` and also control how numbers are displayed.

Example:
```python
total = 44.56789
print(f"${total:.2f}")

### Using round and money format to buil a mini calculator.
