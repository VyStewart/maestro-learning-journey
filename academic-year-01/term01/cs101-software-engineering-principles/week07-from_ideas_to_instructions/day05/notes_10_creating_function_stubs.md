### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 10: Creating function stubs for structure
### Date: Jan 17 - 2026

**Core Focus**
- Building program structure first by creating function stubs, then implementing logic incrementally.

**Key Concepts**
- A function stub is a placeholder function with the correct signature.
- Stubs allow end-to-end wiring before full implementation.
- Separating structure from details prevents getting stuck early.

**Stub Techniques**
- Use return 0.0 (or another placeholder return) when a numeric value is required to keep the program running.
- Use pass when the function should exist but does nothing yet (best for functions that do not need to return a value).
- Choose placeholders that preserve expected types to avoid downstream errors.

**Stub Triple-Check Method**
- Define the function
- Call the function
- Trace execution using print to confirm the control flow and data movement

This quickly detects naming, calling, and flow issues before real logic is written.

**Key Takeaway**
- Build the skeleton first. Once the structure runs, adding correct logic becomes straightforward and controlled.

**Short Reflection**
- This lesson showed me how to reduce debugging pressure by proving the program structure works before implementing details. Using stubs and trace prints turns uncertainty into a checklist: define it, call it, confirm the flow—then fill in logic with confidence.