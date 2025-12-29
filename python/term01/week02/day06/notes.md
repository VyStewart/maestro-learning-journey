# Week 02 – Day 06
# Date: 12-14-2025

## Decision Tables, Loops, and Control Flow

---

## Core Focus of Day 06

Day 06 is about **controlling flow over time**:

* making decisions repeatedly
* stopping or skipping work intentionally
* tracking quantities and totals

This day connects **decision logic** with **iteration logic**.

---

## Decision Tables → Branching Logic

* A **decision table** lists all meaningful combinations of conditions and their outcomes.
* Writing the table first prevents:

  * missing cases
  * duplicated logic
  * unintended multiple outcomes

Mental workflow:

1. Identify the input conditions (booleans or states)
2. List all possible combinations
3. Decide the outcome for each combination
4. Translate into `if / elif / else`

Key rule:

* If only one outcome should happen, use a single decision chain.

---

## `for` Loops

* A `for` loop repeats an action over a **known sequence**.
* It is best used when the number of iterations is known in advance.

Mental model:

> “For each item in this sequence, do this.”

---

## `range()` Mental Model

* `range()` generates a sequence of numbers.
* The stop value is always **excluded**.

Forms:

* `range(stop)` → start at 0
* `range(start, stop)` → custom start
* `range(start, stop, step)` → custom step (including reverse)

Rule to remember:

> Start is inclusive, stop is exclusive.

---

## Modulo (`%`) for Classification

* `%` returns the remainder of a division.
* It is commonly used to classify numbers.

Examples of meaning:

* remainder `0` → divisible evenly
* remainder not `0` → not divisible evenly

Used for:

* even / odd checks
* multiples of a number
* filtering numeric sequences

---

## `while` Loops

* A `while` loop repeats **as long as a condition remains True**.
* It is best used when the number of iterations is **not known in advance**.

Mental model:

> “Keep going while this condition is true.”

Critical rule:

* A `while` loop must change something that affects its condition.

---

## Boolean Flags for Loop Control

* A **boolean flag** is a variable that controls whether a loop continues.
* Flags make exit conditions explicit and readable.

Pattern:

* Start flag as `True` (or `False`)
* Flip the flag when exit conditions are met

Key idea:

> The loop ends when the flag changes state.

---

## `break`

* `break` immediately stops the **entire innermost loop**.
* Execution continues after the loop.

Important points:

* `break` must be inside the loop body
* Its position determines when it can be reached
* If code execution never reaches `break`, the loop does not stop

---

## `continue`

* `continue` skips the **current iteration only**.
* The loop itself continues to the next iteration.

Important points:

* State updates must still occur to avoid infinite loops
* Often used for filtering unwanted cases

---

## `break` vs `continue`

* `break` → stop looping entirely
* `continue` → skip this iteration and move on

Use based on intent:

* Stop early → `break`
* Ignore certain cases → `continue`

---

## Counters

* A **counter** tracks how many times something happens.
* Usually starts at `0`.

Mental model:

> “Each time this condition happens, add 1.”

Counters answer:

* “How many?”

---

## Totals (Accumulators)

* A **total** accumulates numeric values over time.
* Usually starts at `0`.

Mental model:

> “Add this value to what I already have.”

Totals answer:

* “How much?”

---

## Combined Counter + Total Pattern

* It is common to track both:

  * how many values qualify
  * and the sum of those values

This pattern is widely used in:

* analytics
* statistics
* data preprocessing
* AI pipelines

---

## Core Mental Takeaways

* Design decisions before writing loops
* Use `for` when counts are known, `while` when they are not
* Control flow intentionally with flags, `break`, and `continue`
* Counters measure frequency
* Totals measure magnitude
* Clear intent leads to clean logic

---

**Day 06 Theme:** intentional repetition, controlled exits, and measurable outcomes.
