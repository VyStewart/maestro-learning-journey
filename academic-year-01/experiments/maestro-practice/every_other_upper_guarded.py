### Maestro Challenge
### Course: Python101
### Date: Feb 23 - 2026

'''
Task: Write a function called every_other_upper(text)
It should return the same string but with every second character made upper
'''

def every_other_upper(text):
    """
    Returns a new string with every second charater uppercased.
    
    Guard phase:
     - Raise ValueError if input is not a string.
     - Raise ValueError if the string contains any digits.

    Args:
        text (str): input string to process
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    if any(char.isdigit() for char in text):
        raise ValueError("Input can not contain any digits.")
    
    result = ""
    
    for i in range(len(text)):
        if i % 2 != 0:
            result += text[i].upper()
        else:
            result += text[i]
    return result 
            
result = every_other_upper(" I love learning Python")
print(result)

'''
    Practice Insight:
     - Used a loop with range (len(text)) to control upper case of every 2nd char.
     - If I only use slicing, I couldn't change individual items.
     - Indexing gives me full control.
'''