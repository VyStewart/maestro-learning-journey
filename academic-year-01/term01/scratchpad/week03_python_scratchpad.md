### Week 03

## Thinking, Observations, and Learning Process

## Purpose

This scratchpad captures thinking patterns, edge cases, and reasoning traps encountered in Week 3.
It is for understanding and debugging—not final documentation.

String Reasoning Notes
- Indexing = one character
- Slicing = range of characters
- start : stop : step is forgiving when bounds exceed length
- Negative step reverses direction
- Methods return new strings (immutability)

List Mutation & Safety
- Indexing modifies a single position
- Slicing can replace multiple items safely
- IndexError only occurs with indexing, not slicing
- Always check len() mentally before using indexes

Iteration Reasoning
- If modifying → use index-based loop
- If inspecting → use value-based loop
- If tracking position → index-based loop
- Choose clarity over cleverness

⚠️ .append() While Running a Loop (Important)
- Mental model:
    . The loop’s range is determined before the loop starts
    . Appending changes the list length during execution
    . This can cause:
        . unexpected growth
        . infinite loops
        . logic errors
Safe rule of thumb:
- Do not append to the same list you are iterating over
- If needed:
    . iterate over a copy
    . or append to a different list
Why this matters:
 You think you are looping over a fixed structure, but you are silently changing it.

Copy Semantics (Common Pitfall)
- Two variables can reference the same list or dictionary
- Shallow copies protect the container, not nested items
- Nested mutation bugs are hard to trace
Mental check before mutating:
- “Who else can see this data?”

Dictionary Reasoning
- Keys are stable; indexes are not
- Missing keys raise errors
- Iteration pattern should match intent:
    . keys → labels
    . values → data
    . key + value → relationships

Debugging Questions to Ask Yourself
- Am I mutating or reading?
- Is this object shared?
- Do I need the original preserved?
- Is slicing safer than indexing here?
- Should this loop care about position or value?