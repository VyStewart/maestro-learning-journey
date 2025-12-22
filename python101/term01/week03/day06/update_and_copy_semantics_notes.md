### Lesson-Update and copy semantics
### Date:12-21-2025

Key Concepts Learned
. Assignment shares a reference to the same object
. Copying creates a new container
. Shallow copies duplicate only the outer structure
. Inner mutable objects may still be shared
. Update semantics depend on whether data is copied or referenced
. Variables are references, not boxes of data
    . A variable name points to an object

Important Rules to Remember
. Assigning a list or dictionary does not create a copy
. Shallow copies prevent unintended changes to the original container
. Shallow copies do not protect nested mutable objects
. Bugs often arise from unintended shared references
. Copying before updating is a defensive programming practice

Short Reflection
Today I learned why copying data structures matters before updating them. I understand that assignment shares the same object and that shallow copies only protect the outer structure. This helped me see how unintended side effects can happen and why careful copy semantics are important for writing robust code.