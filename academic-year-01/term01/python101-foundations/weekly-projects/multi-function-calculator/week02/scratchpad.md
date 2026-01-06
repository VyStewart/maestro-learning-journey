# Week 2 - Multi-Function Calculator
# Author: Vy S
# Description: A calculator for Bakery Management.

Debug & Learning Highlights (Scratchpad)

1. Function definition vs execution
- Mistake: Left function calls in practice.py
- Result: Tools ran automatically on import
- Fix: Remove all execution from imported files
- Rule: practice.py = definitions only, main.py = execution

2. Scope misunderstanding
- Mistake: Expected variables inside one function to be usable elsewhere
- Fix: Use parameters or return values
- Rule: Function variables are local and do not persist

3. Validation logic (and vs or)
- Mistake: Used and when validating inputs
- Fix: Use or when either condition is invalid
- Rule: Validation usually triggers on any bad input

4. Incorrect membership checks
- Mistake: Wrote "y" and "n" not in answer
- Fix: Check membership explicitly
- Rule: Each in condition must be written out

5. Counters vs totals
- Mistake: Used += 1 when accumulating values
- Fix: Use += value for totals
- Rule: Count iterations vs sum quantities are different patterns

6. Loop structure errors
- Mistake: Calculated totals outside or incorrectly inside loops
- Fix: Accumulate inside loop, summarize after
- Rule: Loop = collect, After loop = report

7. print vs return
- Mistake: Mixed printing inside value-returning functions
- Fix: Functions either return values or print, not both
- Rule: Caller decides what to print

8. Menu validation logic
- Mistake: Compared input directly to tuple
- Fix: Use membership check with in
- Rule: User input is validated with in, not equality

9. Indentation & execution scope
- Mistake: Misplaced indentation caused code to run at wrong time
- Fix: Align prints and logic under correct branches
- Rule: Indentation defines execution in Python

Key takeaway
Most bugs came from misunderstanding execution order and scope, not syntax.
Once execution was traced line-by-line, fixes became obvious.