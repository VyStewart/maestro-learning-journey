### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 03: Hierachy in Pseudocode
### Date: Jan - 14 - 2026

# Ask the user for a word
word = input("Enter a word: ").lower()

# Analyze the word
# 2.1 Count characters
char_count = len(word)

# 2.2 Count vowels
vowel_count = 0
for char in word:
    if char in ("aeiou"):
       vowel_count +=1
       
# Show both counts to the user
print("Number of character:", char_count)
print("Number of vowel:", vowel_count)