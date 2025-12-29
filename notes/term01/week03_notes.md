### Week 03

### Strings, Lists, Dictionaries, and Safe Data Handling

Core Themes
- Working with text, collections, and mappings
- Understanding mutation vs immutability
- Iterating safely and intentionally
- Preventing unintended side effects

Key Concepts Learned
- Strings (Advanced Usage)
- Zero-based indexing
- Slicing with start : stop : step
- Negative indexing
- String methods for cleaning and transforming data
- Strings are immutable

Lists
- Creating lists
- Converting range() to lists
- Using len() to reason about size
- Lists are mutable
- Items can be replaced by index or slice
- Slicing is safer than indexing (no IndexError)

List Iteration
- Index-based loops for modification and position tracking
- Value-based loops for inspection and readability
- Iteration choice depends on intent

Common List Methods
- append() adds one item to the end
- insert() adds an item at a specific index
- remove() deletes the first matching value
- pop() removes and returns an item by index
- extend() merges another iterable into the list

Ordering Lists
- sort() modifies the list in place
- sorted() returns a new sorted list
- key=len sorts by length
- reverse=True reverses ordering

Dictionaries
- Store data as key–value pairs
- Keys act as labels (anchors of meaning)
- Values store the associated data
- Accessing a missing key raises KeyError

Dictionary Iteration Patterns
- Looping over keys (default behavior)
- Looping over values (data-focused)
- Looping over key–value pairs (full context)

Copy & Update Semantics
- Assignment shares references
- Shallow copies create a new container but share inner objects
- Nested structures increase mutation risk

Nested Structures & Safe Mutation
- Lists or dictionaries inside other structures
- Inner mutable objects may be shared
- Safe mutation requires awareness of scope and ownership

Important Rules to Remember
- Start index is included; stop index is excluded
- Slicing never raises IndexError
- Lists and dictionaries are mutable; strings are not
- Assignment is not copying
- Shallow copies protect only the outer structure
- Always choose the simplest iteration pattern that fits the goal
- Be cautious when mutating data inside loops

Short Reflection

Week 3 helped me shift from simple data handling to structured, intentional data manipulation. I learned how mutation, iteration, and copying interact, and why safe practices matter when working with real-world data. I now think more deliberately about how data changes over time.