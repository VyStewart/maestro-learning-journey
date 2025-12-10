# ------------------------------
# Practice 1 — Function I (print inside)
# ------------------------------

def greet(name):
    print(f"Hello, {name}!")

# Test
greet("Vy")
greet("Soleil")


# ------------------------------
# Practice 2 — Function with internal logic (local variable)
# ------------------------------

def study_time(hours):
    label = "hour" if hours == 1 else "hours"
    print(f"I study {hours} {label} every day.")


# Test
study_time(1)
study_time(3)


# ------------------------------
# Practice 3 — Return a doubled number
# ------------------------------

def double_number(n):
    result = n * 2
    return result

# Test
value = double_number(5)
print(value)  # Expected: 10


# ------------------------------
# Practice 4 — Describe a book (print inside)
# ------------------------------

def describe_book(title, author):
    print(f"The book '{title}' is written by {author}.")

# Test
describe_book("Atomic Habits", "James Clear")


# ------------------------------
# Practice 5 — Total price calculator (return)
# ------------------------------

def total_price(price, quantity):
    result = price * quantity
    return result

# Test
total = total_price(4.50, 3)
print(f"Your total is ${total:.2f}")


# ------------------------------
# Practice 6 — Even or Odd (return)
# ------------------------------

def check_number(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


# Test
num = 7
result = check_number(num)
print(f"{num} is {result}")



# ------------------------------
# Practice 7 — Custom function (your choice)
# A function that returns a compliment message
# ------------------------------

def compliment(name):
    message = f"{name}, you are learning Python beautifully."
    return message


# Test
line = compliment("Vy")
print(line)

# Challenge 

# ------------------------------
# Practice 1 — Function I (print inside)
# ------------------------------

def greet(name):
    print(f"Hello, {name}!")


# Test
greet("Vy")
greet("Soleil")



# ------------------------------
# Practice 2 — Function with internal logic (local variable)
# ------------------------------

def study_time(hours):
    label = "hour" if hours == 1 else "hours"
    print(f"I study {hours} {label} every day.")


# Test
study_time(1)
study_time(3)



# ------------------------------
# Practice 3 — Return a doubled number
# ------------------------------

def double_number(n):
    result = n * 2
    return result


# Test
value = double_number(5)
print(value)  # Expected: 10



# ------------------------------
# Practice 4 — Describe a book (print inside)
# ------------------------------

def describe_book(title, author):
    print(f"The book '{title}' is written by {author}.")


# Test
describe_book("Atomic Habits", "James Clear")



# ------------------------------
# Practice 5 — Total price calculator (return)
# ------------------------------

def total_price(price, quantity):
    result = price * quantity
    return result


# Test
total = total_price(4.50, 3)
print(f"Your total is ${total:.2f}")



# ------------------------------
# Practice 6 — Even or Odd (return)
# ------------------------------

def check_number(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


# Test
num = 7
result = check_number(num)
print(f"{num} is {result}")



# ------------------------------
# Practice 7 — Custom function (your choice)
# A function that returns a compliment message
# ------------------------------

def compliment(name):
    message = f"{name}, you are learning Python beautifully."
    return message


# Test
line = compliment("Vy")
print(line)


### Challenge 

def format_price(item, price):
    #print(f"Inside: item = {item}, price = {price}")
    result = f"{item} costs ${price:.2f}"
    return result

line1 = format_price("Coffee", 4.5)
line2 = format_price("sandwich", 7.25)
print(line1)
print(line2)

### Practice Input outside Function

def study (hours, subject):
    time_label = "hour" if hours == 1 else "hours"
    message = (f"I spend {hours} {time_label} on learning {subject} every day.")
    return message
 
study_hours = int(input("How many hours do you spend on learning every day? "))
study_subject = input("What is your study's subject? ")

message = study (study_hours, study_subject)
print(message)