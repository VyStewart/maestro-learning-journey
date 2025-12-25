### lesson-Nested Structures & Safe Mutation
### Date: 12-21-2025


Key Concepts Learned
. Nested structures are data structures that contain other data structures
. Common examples include lists of lists and dictionaries containing lists or other dictionaries
. Nested data introduces additional complexity because inner objects may be shared
. Mutating nested data without awareness can cause unintended side effects

What “Nested” Means
. A list inside another list
. A dictionary containing lists or dictionaries
. Data organized in layers rather than a flat structure

Mental model:
. Boxes inside boxes — changing an inner box may affect multiple outer boxes.

Update & Copy Semantics in Nested Structures
. Assignment does not create a copy; it shares the same object
. Shallow copies create a new outer container but do not copy inner mutable objects
. Inner lists or dictionaries may still be shared across variables

Key distinction:
. Outer structure may be protected
. Inner mutable objects may not be

Safe Mutation Principles
. Always be aware of whether data is shared
. Avoid mutating nested data unless you fully control its scope
. Copy data before mutating when the original must be preserved
. Prefer intentional, localized updates over global changes

Common Risks
. Changes to nested objects propagating unexpectedly
. Bugs that appear far from the mutation point
. Difficulty tracing where data was modified

Defensive Practices to Remember
. Treat assignment as sharing, not copying
. Assume shallow copies protect only the surface
. Mutate at the correct level of the structure
. Choose safety over convenience when working with nested data

Short Reflection
This topic helped me understand why nested data structures require extra care. I learned that shallow copies do not fully protect inner objects and that safe mutation is about controlling side effects. This reinforced the importance of understanding how data is shared before updating it.