### CS101:  Software Engineering Principles
### Week 08: Breaking problems down
### Date: Jan 26 2026


**Week Objective**
- Week 08 emphasizes disciplined thinking before writing code. The goal is to learn how to take a vague feature request and systematically transform it into clear, solvable, and testable parts.
- This week prioritizes clarity, structure, and restraint over execution speed.

**Core Themes and Skills**
1. Clarity Before Code
- Before implementation begins, the problem must be clearly understood and articulated.
    - Define the feature goal in plain language
    - Identify the target user
    - Provide contextual motivation
    - Capture intent without referencing technical details
- A well-defined problem reduces rework and misaligned solutions later.

2. Separating Purpose from Technical Details
- Purpose answers what the program should do.
- Technical details answer how it does it.
- Practices introduced:
    - Clear titles and purpose statements at the top of a file
    - Measurable success criteria (verb + object + condition)
    - Self-describing programs that explain themselves when run
- This separation improves readability, maintainability, and collaboration.

3. Defining Example Input and Output
- Abstract requirements are grounded using concrete examples.
    - Define representative inputs
    - Specify exact expected outputs
    - Use examples as early correctness targets
- This step removes ambiguity and acts as a precursor to testing.

4. Breaking Features into Subproblems
- Large features are decomposed into smaller, manageable units.
    - Translate a feature request into discrete subproblems
    - Write numbered and indented outlines
    - Ensure every requirement maps to a subproblem
    - Avoid extra or unrelated steps
- Each subproblem becomes independently solvable and testable.

5. Defining Subproblem I/O Contracts
- Each subproblem is treated as a black box with clear boundaries.
    - Explicitly define inputs and outputs
    - Consider normal, edge, and invalid cases
    - Create small I/O tables
    - Start with function stubs before full implementation
- Clear contracts prevent hidden assumptions and fragile logic.

6. Sequencing Subproblems Logically
- Subproblems must be executed in the correct order.
    - Identify dependencies between steps
    - Ensure required data exists before use
    - Treat the program as a pipeline (input → processing → output)
- Correct sequencing ensures reliable execution and simpler debugging.

7. Matching Subproblems to Patterns
- Recurring solution structures are recognized and reused.
    - LOOKUP: mapping inputs to known outputs
    - ACCUMULATOR: building results over multiple steps
    - FLAG: tracking state changes or conditions
- Pattern recognition reduces cognitive load and implementation errors.

8. Prioritizing Tasks
- Not all work is equally important.
    - Identify critical path tasks
    - Defer non-essential refinements
    - Resolve high-risk or uncertain areas early
    - Aim for early, working versions
- Prioritization accelerates progress and minimizes late-stage rewrites.

9. Assembling Functions into Pipelines
- Subproblems are composed into complete programs.
    - Use nested calls for simple, direct fl ows
    - Use step-by-step chained variables for clarity and debuggability
- Programs are designed as data flowing through stages, not isolated functions.

**Key Takeaway**
- Week 08 trains professional problem-solving discipline.
- Instead of jumping straight into code, you learn to:
    - Define intent
    - Decompose complexity
    - Establish boundaries
    - Sequence logic
    - Apply known patterns deliberately

This foundation supports faster, cleaner coding and more effective debugging in later weeks.