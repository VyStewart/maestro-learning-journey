### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 06: Understanding common solution patterns
### Date: Jan - 16 - 2026

**Core Focus**
- Recognizing when conditional logic represents a mapping problem and replacing if / elif chains with dictionary lookups.

**Key Concepts**
- Not all decisions require conditional chains.
- Some problems are simple key-to-value mappings.
- Dictionaries encode mappings directly.

**When to Use Dictionary Lookup**
- One input maps to one output.
- Conditions are independent.
- Order of evaluation does not matter.

**Benefits Over if / elif**
- Fewer branches
- Clearer intent
- Easier to extend and maintain

**Design Insight**
- Choosing a dictionary is a design decision, not a syntax trick. It reflects understanding the structure of the problem.

**Key Takeaway**
- If the problem is selection, not decision, a dictionary is often the cleanest solution.

**Short Reflection**
- This lesson helped me see conditional chains as a potential design smell rather than a default solution. By recognizing mapping patterns, I can simplify logic, reduce branching, and make my code easier to extend without rewriting control flow.