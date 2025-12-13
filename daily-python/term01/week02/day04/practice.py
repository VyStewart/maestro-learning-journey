
# Practice 1: Login rule
password_entered = "abc123"
correct_password = "abc123"
is_banned = False

if not is_banned and password_entered == correct_password:
    print("Login successful")
else:
    print("Login failed")


# Practice 2: Game-style door rule
health = 10
have_key = False
master_pass = True

if (have_key or master_pass) and health > 0:
    print("Door opens")
else:
    print("Door stays closed")


# Boss Challenge: Final dungeon access
level = 12
is_cursed = False
has_sword = False
has_staff = True

if (level >= 10 and not is_cursed) and (has_sword or has_staff):
    print("You may enter the final dungeon.")
else:
    print("You are not ready yet.")

# exercise
score = 90 
passed = score >= 70

print(score)
print(passed)

other_passed = True
print(passed == other_passed)
print(passed is other_passed)

# Challenge
age = 21
min_age = 18

old_enough = age >= min_age

print(age)
print(min_age)
print(old_enough)

flag = True
print(old_enough == flag)
print(old_enough is flag)
