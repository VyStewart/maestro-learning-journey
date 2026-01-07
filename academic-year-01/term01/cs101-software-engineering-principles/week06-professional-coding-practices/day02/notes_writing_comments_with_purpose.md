### CS101 - Week 06
### Software Engineering Principles
### Lesson 04: Writing comments with real purpose
### Date: Jan 06 2026

Core Principle:
Comments should add meaning that code alone cannot express. Well-written code explains what it does; comments explain why it does it that way.

1. Purpose of Comments
- Comments exist to clarify intent, reasoning, or constraints.
- They should not restate obvious behavior already visible in the code.
- Effective comments provide context that improves long-term maintainability.
- Reasoning-style comments explain purpose, meaning, or assumption.

2. Separation of Responsibilities
- Code communicates behavior through structure and naming.
- Docstrings explain purpose at the function level.
- Comments explain decisions, trade-offs, or non-obvious logic.
- Each tool serves a distinct role and should not overlap unnecessarily.

3. When Comments Are Appropriate
- When logic is intentionally complex or non-intuitive.
- When a design decision was made due to a constraint or limitation.
- When changing the code without understanding the reason could introduce bugs.
- When future readers need guidance on safe modification.
- If a beginner can infer what the code does in less than 3 seconds, skip the comment.

4. Risks of Poor Comments
- Redundant comments increase noise without adding value.
- Outdated comments can mislead and cause errors.
- Misleading comments are worse than having no comments at all.

5. Professional Standard
- If a comment explains what the code does, the code likely needs better naming or structure.
- If a comment explains why the code exists or behaves a certain way, it is serving its purpose.

6. Comments vs docstrings
- Docstrings: Explain what a function/module/class does for external users (inputs, outputs, behavior).
- Comments: Explain why certain code exists for future readers inside the code (including future-you).

Short Reflection
This lesson reinforces the idea that clarity comes primarily from good code, not excessive commentary. Comments are a precision tool, used to preserve intent and protect important decisions. Writing fewer, higher-quality comments reflects professional judgment and a deeper understanding of code as a long-term communication medium.