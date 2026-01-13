### CS101 - Week 06
### Software Engineering Principles
### Lesson 16: Refactoring with confidence
### Date: Jan 11 2026

Core Principle:
Refactoring improves the structure and clarity of code without changing its external behavior. Safe refactoring relies on evidence, not intuition.

1. What Refactoring Is
- Refactoring changes how code is written, not what it does.
- Inputs and outputs remain consistent.
- Only structure, readability, and design improve.
- Behavior changes indicate a feature change, not refactoring.

2. Why Confidence Is Required
- Fear of breaking working code prevents improvement.
- Confidence comes from safety checks, not risk-taking.
- Refactoring is low-risk when done incrementally and verified continuously.

3. Safety Nets That Enable Refactoring
- Refactoring is safe when supported by:
- Assertions that protect invariants
- Edge-case tests that validate boundaries
- Clear function contracts and signatures
- Well-placed errors that stop invalid execution
- Tracing tools for observing behavior if needed
- These mechanisms ensure correctness is preserved.

4. Small, Incremental Changes
- Change one thing at a time.
- Keep each change small and reversible.
- Common refactors include renaming, extraction, and simplification.
- Large, unstructured changes increase risk and uncertainty.

5. Verification After Each Change
- Re-run tests and asserts after every refactor.
- Re-check edge cases and boundaries.
- Immediate verification makes failures easy to diagnose.

6. Refactoring as a Professional Habit
- Refactoring is continuous, not occasional.
- It prevents code decay over time.
- Clean structure supports maintainability and future growth.

Short Reflection
This lesson reframes refactoring from a risky activity into a disciplined, evidence-driven practice. With proper safety nets and incremental changes, improving code becomes routine rather than intimidating. Refactoring with confidence allows codebases to evolve without sacrificing correctness or stability.