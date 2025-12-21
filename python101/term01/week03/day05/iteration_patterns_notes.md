#### Lesson - Dictionaries ii: Iretation Patterns
### Date: 12-20-2025

Key Concepts Learned
. Dictionaries store data as key–value pairs
. Keys act as labels that anchor meaning
. Dictionaries can be iterated in different ways depending on intent
. Iteration can focus on keys, values, or full key–value relationships

Mental models
. Looping over keys
    . Default loop over a dictionary goes through its keys
    . Use when look for the key or access the value with [key]
. Looping over values
    . Goes trough all the values only
    . Use when the keys don't matter
. Looping over key-value pairs
    . Gives a pair each time: (key, value)
    . The two variables after for are unpacked from that pair
    . Use when need both the key and the value in the loop

Important Rules to Remember
. Dictionary Iteration Patterns
. Iterating over a dictionary by default loops over keys
. Iterating over keys is useful when labels matter or when values need to be accessed or updated
. Iterating over values is useful when only the data matters and labels are irrelevant
. Iterating over key–value pairs provides full context and is the most common real-world pattern

Safety Notes
. Accessing a missing key raises a KeyError
. Keys are more stable than indexes as data grows or changes
. Choose iteration style based on intent, not habit

Short Reflection
Today I learned how to iterate through dictionaries using keys, values, or key–value pairs. I understand how each pattern reflects a different perspective on the data and why iterating over both keys and values together is often the most informative and flexible approach.