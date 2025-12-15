### Lesson: String membership with in/ not in to condiction
## Date: 12-13-2025

# Using bool to make decision based on wether a word appears inside a larger string.
subject = "Weekend SALE now!"
if "SALE" in subject:
    print("Promo email detected")
else:
    print("Regular email")

# Not in does the opposite. True when the substring is missing
# Example 1:
log = "System update complete"

if "ERROR" not in log:
    print("All good, no error found")
else:
    print("warning: errors present")
    
 # Example 2:   
if "URGENT" in subject:
   print("there is a sale this weekend")
elif "SALE" in subject:
  print("Sale is here.")
else:
  print("There is nothing goimg on.")
  
# Challenge: find and fix the bug
message = "ERROR: disk almost full"

if "ERROR" in message:
    print("ERROR found")
#else "ERROR" in message:  error      
elif "ERROR" not in message:   
    print("No error")

# Mini task to log in
subject = "Your package has shipped"

if "URGENT" in subject:
    print("High priority")
elif "shipped" in subject:
    print("Shipping update")
else:
    print("Other email")
    
# Boss-level Challenge:
# Email Filter

message = "hi, I need help with the spam email!"

if "help" in message:
    print("Flagged: support")
elif "spam" in message:
    print("Flagged: spam")
elif "hi" in message:
    print("Flagged: greeting")
else:
    print("Uncategorized")
    
# Ultra short challenge:
## Classify a system status message

message = "System WARNING: low memory"

if "ERROR" in message:
    print("Status: error")
elif "WARNING" in message:
    print("Status: warning")
elif "OK" not in message:
    print("Status: unknown")
else:
    print("Status: ok")
