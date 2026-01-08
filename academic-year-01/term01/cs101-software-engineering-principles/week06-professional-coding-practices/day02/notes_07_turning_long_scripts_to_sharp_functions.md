### CS101 - Week 06
### Software Engineering Principles
### Lesson 07: Turning Long Scripts Into Sharp Functions
### Date: Jan 06 2026

Core Principle:
Functions are units of intent. Breaking long scripts into well-defined functions improves readability, maintainability, and design clarity.

1. Limitations of Long Scripts
- Long, linear scripts mix multiple responsibilities.
- Intent becomes hidden inside execution order.
- Small changes increase the risk of unintended side effects.
- Debugging and reasoning become more difficult as scripts grow.

2. Functions as Units of Responsibility
- Each function should perform one clear, focused task.
- A function’s purpose should be explainable in a single sentence.
- Meaningful function names allow understanding without inspecting implementation details.

3. Improving Readability Through Structure
- Functions allow code to be read top-down as a high-level outline.
- Low-level details are hidden behind clear abstractions.
- Readers can understand program flow before examining specifics.

4. Separation of Concerns
- Each function handles a distinct responsibility.
- Changes are localized, reducing the chance of breaking unrelated logic.
- Clear boundaries make refactoring safer and easier.

5. Reuse and Safety
- Functions prevent duplication of logic.
- Isolated behavior simplifies testing and debugging.
- Well-designed functions protect the codebase as it grows.

Short Reflection
This lesson emphasizes a shift from writing code that simply executes to designing code with clear structure and intent. Turning long scripts into focused functions makes programs easier to understand, safer to change, and more scalable over time. Functions become the building blocks of clean, professional software design.