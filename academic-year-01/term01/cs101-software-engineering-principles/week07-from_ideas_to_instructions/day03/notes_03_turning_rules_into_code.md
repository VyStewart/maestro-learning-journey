### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 04: Turning rules into code
### Date: Jan - 15 - 2026

**Core Focus**
- Translating problem rules and constraints into clear, intentional control flow in code.

**Key Concepts**
- Most programs exist to enforce rules.
- Rules define what is allowed, restricted, or required.
- Rules should be identified before coding.

1. Rule Translation Principles
- Rules become conditions.
- Conditions become control flow.
- Control flow determines program behavior.

2. Common Rule Encodings
- if / else → enforce decisions
- while → repeat until a rule changes
- continue / return → stop or skip when a rule is violated

3. Why Placement Matters
- Rules must run at the correct time.
- Misplaced rules lead to valid syntax but incorrect behavior.
- Early validation prevents deeper logic errors.

**Key Takeaway**
Correct code starts with correct rules. If the rules are unclear, the logic will be fragile.

**Short Reflection**
This lesson helped me see code as a system of decisions rather than a sequence of calculations. By identifying rules first and then translating them into control flow, I gain more control over program behavior and reduce hidden bugs. It also explains why some programs “work” but still feel wrong—the rules were never clearly enforced.