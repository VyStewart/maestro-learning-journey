# Week 02 – Day 04

## Logical Operators, Short-Circuiting, Booleans & Comparisons

---

## Concepts Learned

* **Logical operators** combine multiple conditions:

  * and → all conditions must be True
  * or → at least one condition must be True
  * not → flips a boolean value

* **Short-circuiting**:

  * A and B: if A is True, Python skips B
  * A or B : if A is True , Python skips B

* **Booleans** are a real data type (bool) with only two values: True and False

* **Comparisons** (==, !=, <, >, <=, >=) always produce a boolean.

* **Equality vs Identity**:

  * == compares **values**
  * is compares **object identity (same object in memory)**

* True, False, and None  are **singletons** in Python.

* Identity reuse for numbers or strings is an **optimization**, not a rule — never rely on it.

---

## Mental Model for Writing Conditions

1. **Say the rule in plain English first**
   Example: “User can log in if password is correct and user is not banned.”

2. **Map words → operators**

   * “and” → and
   * “or” → or
   * “not …” → not

3. **Write each comparison clearly**

age >= 18
password_entered == correct_password
not is_banned

4. **Group related logic with parentheses**


if (age >= 18 and has_ticket) or has_parent:

Parentheses improve readability and control evaluation order.

5. **Use "not" for simple booleans**

not is_banned      # preferred
is_banned == False # avoid

---

## Short-Circuiting Reference

* A and B

  * If A is "False" → Python skips B

* A or B

  * If A is True → Python skips B

Short-circuiting prevents unnecessary work and avoids errors.

---

## Equality vs Identity

x == y   # same value
x is y   # same object in memory

Rules:

* Use == for numbers, strings, and results of calculations
* Use is only for identity checks (most commonly "None")

if value is None:


---

## Debugging Tip

To see what actually runs, temporarily add prints:


print("checking A")
print("checking B")


Remove debug prints after confirming logic.

---

## Reflection

* I understand that Python evaluates **current state**, not real-world assumptions.
* I can translate real rules into explicit boolean logic.
* I understand how short-circuiting controls what code runs.
* I understand the difference between value (==) and identity (is).
* Logical conditions now feel structured instead of confusing.

---


