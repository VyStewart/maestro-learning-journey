### Lesson: String skills upgrade ii: common methods
### Date : 12-16-2025

## Trimming whitespace with strip, lstrip, and rstrip
# Example
name_line = " Alice,BOB,,  Charlie "

left_clean = name_line.lstrip()
right_clean = name_line.rstrip()
both_clean = name_line.strip()

print(left_clean),
print(right_clean),
print(both_clean)

## Case normalisation with.lower()
#Example
raw_name = "Alice"

print(raw_name == "alice")              # False
print(raw_name.lower() == "alice")      # True

## Fix messy text with .reolace()
#Example
line = "Alice,BOB,, Charlie"
fixed = line.replace("BOB", "Bob")

print(line)
print(fixed)

## Using .find() to search safely inside a string
# Example
line = "Alice,BOB,, Charlie"
fixed = line.replace("BOB", "Bob")

print(line)
print(fixed)

pos_bob = line.find("BOB")
pos_dave = line.find("Dave")

print(pos_bob)          # 6
print(pos_dave)         # -1    when not found

## Spliting the string into pieces with .split()
#Example 1
line = "Alice, Bob, , Charlie"
pieces = line.split(",")

print(pieces)       #['Alice, 'Bob', ' ', 'Charlie']

#Example 2
line = "Alice, Bob, , Charlie"
pieces = line.split(",")

print(pieces)

clean_line = line.replace(", ,", ",UNKNOWN,")
print(clean_line)

clean_pieces = clean_line.split(",")
print(clean_pieces)

#Example 3
line = "Alice, Bob, , Charlie"
pieces = line.split(",")

print(pieces)

clean_line = line.replace(", ,", ",UNKNOWN,")
print(clean_line)

clean_pieces = clean_line.split(",")
print(clean_pieces)

clean_pieces = clean_line.split(",")

first = clean_pieces[0].strip()
second = clean_pieces[1].strip()
third = clean_pieces[2].strip()
fourth = clean_pieces[3].strip()

print(first)
print(second)
print(third)
print(fourth)