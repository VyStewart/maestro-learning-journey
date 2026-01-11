### CS101 - Week 06
### Software Engineering Principles
### Lesson 11: Debugging step by step
### Date: Jan 08 2026

Core Principle:
Effective debugging is a disciplined, repeatable process. Professional debugging replaces guesswork with controlled observation, evidence, and incremental testing.

Bugs vs how we debug
- A bug is the underlying mistake un the code(toot cause)
- The error message or wrong output is just the system
- The goal in debugging:  ove from "what went wrong?" to "why did it go wrong?"

1. Reproduce the Bug Reliably
- A bug must be reproducible to be fixed with confidence.
- Consistent reproduction establishes a stable baseline.
- Reliable reproduction prevents false fixes and intermittent errors from being overlooked.

2. Read the Exact Error or Wrong Output
- Error messages and incorrect outputs are primary diagnostic signals.
- Precise reading of errors narrows the search space.
- Bugs often originate earlier than the point where failure becomes visible.

3. Trace Program Flow and Inputs at the Failure Point
- Tracing reveals actual execution paths and state changes.
- Observing inputs, branches, and variable values exposes violated assumptions.
- This step validates or disproves mental models of how the code runs.

4. Reduce to the Smallest Failing Case
- Simplifying the problem isolates the true cause.
- Removing unrelated code reduces noise and speeds reasoning.
- The smallest failing case is easier to test, explain, and fix.

5. Form and Test One Hypothesis at a Time
- A hypothesis is a single, testable explanation for the failure.
- Testing one hypothesis at a time keeps changes controlled.
- This prevents cascading errors and makes conclusions reliable.

6. Clean Up Tracing, Retest, and Keep the Fix
- Temporary debugging code should be removed after fixing the issue.
- Retesting confirms the fix under the original failure conditions.
- Final code should be clean, readable, and free of debugging artifacts.

7. Professional Debugging Outcome
- Debugging becomes systematic rather than emotional.
- Problems are solved faster with less risk of regression.
- The process scales to larger, more complex systems.

Short Reflection
This lesson formalizes debugging as a methodical practice rather than an improvisational activity. By treating bugs as controlled experiments—observed, reduced, hypothesized, and tested—debugging becomes predictable and efficient. This structured approach directly supports confident problem-solving and reinforces the kind of challenge-driven work that leads to deeper technical mastery.