### CS101 - Week 06
### Software Engineering Principles
### Lesson 14: Validating inputs before they break things
### Date: Jan 11 2026

Core Principle:
Many bugs originate from bad or unexpected input. Validating inputs early prevents invalid data from propagating through the program and causing subtle, hard-to-trace failures.

1. The Risk of Bad or Unexpected Input
- Programs often fail silently when inputs are incorrect.
- Errors caused by invalid input may appear far from their source.
- Early validation localizes failure and simplifies debugging.
- Defensive input handling improves reliability and predictability.

2. Guard Clauses
- Guard clauses are early checks that exit a function when its contract is violated.
- They prevent unnecessary nesting and keep control flow flat.
- Guard clauses make assumptions explicit at the top of a function.
- This pattern improves readability and reduces error-prone complexity.

3. Type and Range Checks
- Type checks ensure inputs are of the expected kind.
- Range checks ensure values fall within acceptable limits.
- These checks formalize a function’s expectations and constraints.
- In a dynamically typed language, explicit validation is critical for correctness.

4. Simple Helper Functions for Validation
- Validation logic is often repeated across functions.
- Helper functions centralize and standardize validation rules.
- This reduces duplication and improves consistency.
- Separating validation from core logic improves testability and clarity.

5. Sentinel Returns (e.g., None)
- Sentinel values deliberately signal the absence of a valid result.
- Returning None allows functions to fail safely without crashing.
- Sentinel behavior must be documented and handled by the caller.
- Ignoring sentinel values reintroduces silent failure risks.

6. Professional Outcome
- Input validation prevents corrupted state.
- Functions become safer and more reusable.
- Failures occur early, clearly, and predictably.

Short Reflection
This lesson reinforces a defensive mindset: inputs are the most common source of failure, so they must be handled explicitly. By validating inputs early—using guard clauses, checks, and sentinel returns—code becomes more resilient and easier to reason about. This approach shifts failure from being hidden and delayed to being visible and controlled, which is essential for building reliable systems.