### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures
### Date: March 21 - 2026
### lesson 11: Introducing high dimension arrays


High-dimensional (multi-level) arrays – Key ideas
=================================================

1. 1-D array
------------
A simple list of items.

Example: a shopping list

items = ["eggs", "milk", "bread"]


2. 2-D array = “list of lists” (grid)
 
First index → row

 Second index → column (or position in that row)
 
Examples:

Theater seats → seats[row][seat]
Tic-tac-toe board → board[row][col]
School timetable → timetable[day][period]
Knitting pattern → pattern[row][stitch]

3. 3-D array = stacked grids (layers)
 
Think: multiple 2-D grids stacked on top of each other.
 
First index → layer
 Second index → row
 Third index → column

4. When to use a multi-level array?
 
Use a multi-level array when the SAME type of data is organized by 2 or more independent categories, like:
 
row & column
day & time slot
layer & row & column

- Summary 
High-dimensional array = an array whose elements are themselves arrays.
 
1-D → simple list
2-D → grid (list of lists)
3-D → stacked grids (list of list of lists)

