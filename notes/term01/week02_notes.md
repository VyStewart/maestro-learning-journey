## Control Flow, Logic, and Iteration

## Week 02 Focus

Week 02 centers on **control flow and reasoning**:

* making decisions
* repeating actions
* controlling execution paths
* tracking state over time

The emphasis is on **predictability**, not memorization.

---

## Functions (I, II, III)

* Functions organize logic and reduce repetition.
* A function has:

  * a purpose (why it exists)
  * internal logic (what happens inside)
  * an output (`return`)

### `return` vs `print`

* `print` displays information.
* `return` sends a value back to the caller.
* Only returned values can be reused in later logic.

### Early Return

* `return` immediately exits a function.
* Useful for guard conditions and validation.

---

## Scope and Local Variables

* Variables inside a function are **local**.
* Variables outside are **global**.
* Assigning to a variable inside a function makes it local by default.

Best practice:

> Pass values in → compute → return results.

---

## Booleans and Logical Operators

* Booleans represent True / False states.
* Comparisons always produce booleans.

Logical operators:

* `and` → all conditions must be True
* `or` → at least one condition must be True
* `not` → flips a boolean

---

## Short-Circuit Evaluation

* `A and B`: if A is False, B is skipped
* `A or B`: if A is True, B is skipped

Short-circuiting prevents unnecessary work and errors.

---

## Equality vs Identity

* `==` compares values
* `is` compares object identity

Rules:

* Use `==` for numbers and strings
* Use `is` for `None` and true singletons

---

## Decision Making (`if / elif / else`)

* Conditions are evaluated top to bottom.
* Python executes the first True branch and stops.
* Order matters.

Use `elif` when conditions are mutually exclusive.

---

## String Membership

* `in` checks existence
* `not in` checks absence
* Membership is case-sensitive

Membership expressions return booleans.

---

## Decision Tables

* Decision tables map inputs to outcomes.
* Writing them first prevents missing cases.

Workflow:

1. Identify inputs
2. List combinations
3. Define outcomes
4. Translate into branching logic

---

## Loops

### `for` Loops

* Used when iteration count is known.

### `range()`

* Start is inclusive
* Stop is exclusive
* Step controls increment or decrement

---

### `while` Loops

* Used when iteration count is unknown.
* Loop continues while a condition is True.

Critical rule:

> The loop must update something that affects its condition.

---

## Loop Control

### Boolean Flags

* Explicit variables controlling loop continuation.

### `break`

* Immediately exits the innermost loop.
* Must be reached by execution path to take effect.

### `continue`

* Skips the current iteration only.

---

## Modulo (`%`)

* Returns remainder of division.
* Used for classification (even/odd, multiples).

---

## Counters and Totals

* Counters answer: How many?
* Totals answer: How much?

Both typically start at 0.

---

## Core Takeaways

* Code follows execution paths, not intent.
* One outcome → `if / elif / else`.
* Multiple outcomes → separate `if`s.
* Design logic before writing loops.

---

