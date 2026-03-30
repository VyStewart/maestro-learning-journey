### CS102 - Data structures & algorithms 
### Week 04 - Searching and sorting
### Date: March 29 - 2026

# Using Python's built-in sorting tools
"""
Python provides powerful built-in sorting functions that are optimized and easy to use.
The sorted() function returns a new sorted list from the items in an iterable, while the list.sort() method sorts the list in place.
Both functions accept a key parameter that allows you to specify a function to be called on each list element prior to making comparisons, and a reverse parameter that allows you to sort in descending order.
"""

# Example usage of sorted() and sort() with a list of tuples representing players and their scores

players = [
    ("Alice", 1200),
    ("Bob", 450),
    ("Cara", 750),
    ("Dan", 300)
]

players_by_score_desc = sorted(players, key=lambda p: p[1], reverse=True)
players.sort(key=lambda p: p[1])

print(players_by_score_desc)
print(players)

