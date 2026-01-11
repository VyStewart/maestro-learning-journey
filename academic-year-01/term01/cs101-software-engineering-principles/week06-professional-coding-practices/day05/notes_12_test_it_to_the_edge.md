## CS101 - Week 06
## Software Engineering Principles
## Lesson 12: Test it to the Edge
## Date: Jan 10 2026

Core Principle:
Correct code must handle not only normal inputs, but also edge cases and invalid inputs. Boundary testing exposes hidden assumptions and prevents subtle logic errors from going unnoticed.

1. Normal Inputs vs. Edge Cases
- Normal inputs represent the most common, expected use of a function.
- Edge cases are valid inputs that occur at the boundaries of logic.
- Common edge cases include:
- Empty collections
- Single-item collections
- Extremely large or small values
- Edge cases often reveal flaws in loop logic, indexing, and assumptions.

2. Invalid Inputs
- Invalid inputs fall outside a function’s intended contract.
- Examples include:
- Incorrect data types
- Missing values
- Mixed or inconsistent structures
- Functions should fail clearly and early when receiving invalid inputs.
- Silent failure or undefined behavior is more dangerous than explicit failure.

3. Assert Tests as Defensive Checks
- An assert encodes an assumption about program state.
- If the assumption is false, execution stops immediately.
- Asserts are developer-facing tools used to:
- Catch bugs early
- Validate assumptions
- Prevent error propagation
- Assert tests are not user error handling; they are correctness guards.

4. Testing to the Edge
- Testing to the edge means deliberately validating boundaries and unusual cases.
- Small, targeted tests provide high diagnostic value.
- Edge testing complements tracing, invariants, and systematic debugging.

5. Professional Outcome
- Boundary testing improves reliability and robustness.
- It encourages disciplined, defensive thinking.
- Code becomes safer to reuse, refactor, and extend.

Short Reflection
This lesson reinforces a shift from trusting “happy path” behavior to actively challenging assumptions. Testing to the edge transforms debugging from a reactive activity into a proactive design practice. By validating boundaries early, code becomes more predictable, reliable, and resilient—especially as systems grow in complexity.
