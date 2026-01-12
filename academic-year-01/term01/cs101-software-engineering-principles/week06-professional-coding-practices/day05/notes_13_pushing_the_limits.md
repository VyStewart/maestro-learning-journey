## CS101 - Week 06
## Software Engineering Principles
## Lesson 12: Pusing the limits
## Date: Jan 10 2026

Core Principle:
Robust code is built by defining and enforcing clear boundaries. By systematically testing limits, developers prevent subtle bugs and make function behavior predictable and safe.

1. Clear Input and Output Boundaries
- Every function operates within defined limits, whether explicit or implicit.
- Boundaries specify:
- Valid inputs
- Guaranteed outputs
- Responsibility scope
- Small, focused functions make boundaries easier to define and verify.
- Clear boundaries support reuse, testing, and confident refactoring.

2. Boundary Catalogue as a Thinking Tool
- A boundary catalogue provides a structured way to test limits:
- Lower bound: smallest valid input
- Upper bound: largest valid input
- Just inside: valid values near the boundary
- Just outside: invalid values near the boundary
- Empty: absence of data (e.g., empty list)
- This approach replaces ad-hoc testing with deliberate coverage of edge conditions.

3. Using Assert Tests to Enforce Boundaries
- Assert statements encode assumptions directly in code.
- They fail immediately when a boundary is violated.
- Asserts prevent invalid states from propagating through the program.
- Their role is to protect correctness during development, not handle user errors.

4. Avoiding Off-by-One Errors (< vs <=)
- Off-by-one bugs often result from unclear boundary definitions.
- Choosing between < and <= reflects whether a boundary is exclusive or inclusive.
- Explicit boundary thinking makes comparison operators intentional.
- This is especially critical in loops, indexing, and conditional logic.

5. Professional Outcome
- Boundary-driven design reduces hidden assumptions.
- Bugs are caught at the edges instead of surfacing unpredictably.
- Code becomes more precise, reliable, and easier to reason about.

Short Reflection
This lesson emphasizes precision over intuition. By deliberately defining and testing boundaries, code becomes safer and more predictable. Pushing logic to its limits exposes weaknesses early and transforms edge-case handling into a systematic design practice. This mindset supports confident debugging and reinforces disciplined, professional software development.