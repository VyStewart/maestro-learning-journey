# ----------------------------------------
# Practice 1 — Convert hours to minutes (return)
# ----------------------------------------

def to_minutes(hours):
    result = hours * 60
    return result

study_time = to_minutes(3)
print("Total minutes:", study_time)



# ----------------------------------------
# Practice 2 — Maestro Early Return Demo
# ----------------------------------------

def describe_length(name):
    print("Starting description")
    length = len(name)
    if length == 0:
        return "Empty name"    # early exit
    print("Finish description")
    return f"Name has {length} characters"



# ----------------------------------------
# Practice 3 — Same function WITHOUT conditions
# (You are not allowed to use if yet, simply observe return behavior)
# ----------------------------------------

def describe_length(name):
    length = len(name)
    return f"Name has {length} characters"
    print("This will not run")   # unreachable code

message = describe_length("Vy")
print(message)



# ----------------------------------------
# Practice 4 — Early return stops execution
# ----------------------------------------

def double_and_log(x):
    print("Starting double")
    result = x * 2
    return result                 # function stops here
    print("Done")                 # unreachable code

number = double_and_log(15)
print("Number is:", number)



# ----------------------------------------
# Practice 5 — Challenge (Compute total with tax)
# ----------------------------------------

def compute_total(price, tax_rate):
    print("Starting total calculation")
    tax = price * tax_rate
    total = price + tax
    return total                  # early return
    print("This line will not run")

final_amount = compute_total(50, 0.08)
print(f"Final amount is: ${final_amount:.2f}")
