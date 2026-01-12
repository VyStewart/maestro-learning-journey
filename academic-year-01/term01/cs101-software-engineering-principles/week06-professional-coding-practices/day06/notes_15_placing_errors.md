### CS101 - Week 06
### Software Engineering Principles
### Lesson 15: The art of well_paced error
### Date: Jan 11 2026

Core Principle:
Errors should be intentional, informative, and placed as close as possible to the source of failure. Well-designed errors stop invalid execution early and clearly communicate how to recover.

1. What Makes a Good Error Message
- A good error message explains what went wrong in plain language.
- It also tells what action to take next.
- Error messages are part of the interface, not just internal diagnostics.
- Clear errors reduce confusion and speed up resolution.

2. Errors as Communication Tools
- Errors exist to protect correctness, not to punish mistakes.
- Silent failures hide the real cause and create downstream bugs.
- Loud, clear failures make incorrect assumptions visible immediately.

3. Error Placement in Helper Functions
- Helper functions enforce internal correctness.
- When an assumption fails inside a helper function, raising an exception is preferred.
- Exceptions stop execution immediately and prevent misuse of invalid results.
- Returning silent special values shifts responsibility outward and increases risk.

4. Exceptions vs. Sentinel Values
- Exceptions are appropriate when:
- An assumption is violated
- Continuing execution would be incorrect
- The error represents a programmer mistake
- Sentinel values (e.g., None) are appropriate when:
- Failure is expected and normal
- The caller is responsible for deciding what to do next
- Choosing between them is a deliberate design decision.

5. Professional Outcome
- Well-placed errors localize failures.
- Debugging becomes faster and more reliable.
- Code communicates intent and constraints clearly.

Short Reflection
This lesson reframes errors as a design tool rather than a problem to avoid. By placing errors deliberately and making them informative, failure becomes controlled and useful instead of disruptive. Clear error handling improves trust in the code and reinforces disciplined, professional system design.

