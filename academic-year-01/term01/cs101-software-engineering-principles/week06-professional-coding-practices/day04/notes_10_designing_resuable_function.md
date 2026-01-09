### CS101 - Week 06
### Software Engineering Principles
### Lesson 10: Designing Functions that can be resued anywhere
### Date: Jan 08 2026

Core Principle:
Reusable functions are designed as independent components. They rely on inputs, return outputs, and expose clear interfaces that allow them to be used in multiple contexts.

1. Parameters vs. Arguments
- Parameters define what a function expects in its definition.
- Arguments are the actual values passed when the function is called.
- Clear separation between the two encourages flexible, reusable logic.
- Functions should depend on parameters rather than hardcoded values.

2. Print vs. Return
- print is used for displaying information to a human.
- return is used to pass data back to the program.
- Functions that return values are reusable, testable, and composable.
- Overusing print tightly couples a function to a single use case.

3. Function Signature as a Mini-API
- A function’s name, parameters, and return behavior form its interface.
- The signature defines how the function can be safely used.
- Good signatures are explicit, predictable, and minimal.
- Treating a function as a mini-API promotes disciplined design thinking.

4. Chaining Functions
- Functions that return values can be combined together.
- Chaining enables clear data flow from one function to the next.
- This approach encourages separation of responsibilities.
- Well-chained functions create programs that are easier to read and extend.

5. Professional Design Outcome
- Reusable functions reduce duplication and complexity.
- They support testing, refactoring, and long-term maintenance.
- Function design shifts from “solving a problem once” to “solving it well.”

Short Reflection
This lesson reinforces a key transition from writing functional code to designing flexible systems. By focusing on inputs, outputs, and clear interfaces, functions become building blocks rather than one-off solutions. Designing with reuse in mind improves code quality, composability, and professional maturity.