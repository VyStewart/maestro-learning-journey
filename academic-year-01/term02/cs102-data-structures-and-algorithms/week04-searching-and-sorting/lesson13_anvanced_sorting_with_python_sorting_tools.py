### CS102 - Data structures & algorithms 
### Week 04 - Searching and sorting
### Date: March 29 - 2026

# Advanced sorting with Python's sorting tools
"""
Python's built-in sorting tools, such as sorted() and list.sort(), 
are highly optimized and can be used to sort complex data structures with ease.
The key parameter allows you to specify a function that extracts a comparison key 
from each list element, enabling you to sort by specific attributes or criteria.
The reverse parameter allows you to sort in descending order, which can be useful 
for sorting scores, dates, or any other data where you want the highest values first.
"""

# Example usage of sorted() and sort() with a list of dictionaries representing payers  and their scores

players = [
    {"name": "Alice", "score": 200},
    {"name": "Bob", "score": 150},
    {"name": "Cara", "score": 300},
    {"name": "Josh", "score": 600},
    {"name": "Marcus", "score": 450},
]
leaderboards = sorted(players, key=lambda p: (-p["score"], p["name"]))

print(leaderboards)

# Example usage of sorted() and sort() with a list of  products represented as dicts with rating and price

products = [
    {"name": "Laptop", "rating": 4.8, "price": 999.99},
    {"name": "Smartphone", "rating": 4.6, "price": 499.99},
    {"name": "Headphones", "rating": 4.5, "price": 199.99},
    {"name": "Smartwatch", "rating": 4.7, "price": 299.99},
    {"name": "Tablet", "rating": 4.3, "price": 399.99}
]
# Sort products by rating (highest first) and then by price (lowest first)
products_sorted = sorted(products, key=lambda p: (-p["rating"], p["price"]))
print(products_sorted)


