### CS101:  Software Engineering Principles
### Week07: From ideas to instruction
## Lesson 02: Breaking the problem
### Date: Jan - 14 - 2026

# Set the word count to 0
word_count = 0

# Collect the words longer then 4 letters to a list
words = []

#Ask the user for a sentence
while True:
    sentence = input("Enter a sentence (STOP to end): ").lower()

# Stop asking when the user enter STOP
    if sentence == "stop":
        break

#Count how many words in the sentence are longer than 4 letters
    for word in sentence.split():
        if len(word) > 4:
            word_count += 1
            words.append(word)
   
# Display the count
print("Words longer than 4 letters:", words)
print("Words longer than 4 letters:", word_count)