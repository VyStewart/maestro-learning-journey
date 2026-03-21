### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures
### Date: March 21 - 2026
### lesson 12: Implementing high dimenension arrays


# Example 1: 

cube = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]
cube[0][1][1] = 0
print(cube)                 # [[[1, 2], [3, 0]], [[5, 6], [7, 8]]]

# Example 2: "painting" a 3D array
cube = [
    [  # layer 0
        [0, 0, 0],  # row 0
        [0, 0, 0],  # row 1  ← we’ll paint this row
        [0, 0, 0]   # row 2
    ],
    [  # layer 1
        [0, 0, 0],
        [0, 0, 0],  # row 1  ← and this one too
        [0, 0, 0]
    ],
    [  # layer 2
        [0, 0, 0],
        [0, 0, 0],  # row 1  ← and this
        [0, 0, 0]
    ]
]
cube[0][1] = [1, 1, 1]
cube[1][1] = [1, 1, 1]
cube[2][1] = [1, 1, 1]
print(cube)

# Example 3: creating a 3D array with list comprehensions
cube = [
    [  # layer 0
        [0, 0, 0],  # row 0
        [0, 0, 0],  # row 1
        [0, 0, 0]   # row 2
    ],
    [  # layer 1
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [  # layer 2
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
]
cube[1] = [
    [9, 9, 9],
    [9, 9, 9],
    [9, 9, 9]
]

cube[1] = [
    [5, 0, 5],
    [0, 0, 0],
    [5, 0, 5]
]

print(cube)
