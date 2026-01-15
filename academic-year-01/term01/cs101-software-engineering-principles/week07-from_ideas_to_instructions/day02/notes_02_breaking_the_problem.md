### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 02: Breaking the problem
### Date: Jan - 14 - 2026

**Core Focus**
- Turning a natural-language prompt into a clear, ordered execution plan before writing code.

**Key Concepts**
- Most bugs originate from misunderstanding the problem, not syntax.
- Breaking the problem means translating words into actions.
- Prompts can be decomposed using nouns and verbs.

1. Decomposition Technique
- Nouns identify:
    - Data
    - Variables
    - Collections
- Verbs identify:
    - Actions
    - Transformations
    - Control flow

2. Step Listing Method
- Convert verbs into a numbered list (1–2–3–4–5).
- Each step represents a concrete action the program must perform.
- Do not code until the steps are clear and complete.

3. utput Alignment Rule
- The program’s final output must correspond to the final step.
- Misalignment indicates:
    - A missing step
    - Incorrect execution order
    - Misinterpretation of the prompt

**Key Takeaway**
- Clear steps produce clear code. If the steps are wrong, the code will be wrong—even if it runs.

**Short Reflection**
- This lesson showed me that clarity comes before correctness. By pulling verbs and nouns from the prompt and turning them into steps, I reduce guesswork and rework. Coding from a clear list keeps me aligned with the problem and makes debugging more structured and less frustrating.