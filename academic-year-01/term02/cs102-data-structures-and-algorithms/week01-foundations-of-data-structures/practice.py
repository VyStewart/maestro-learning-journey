### CS102 - Data structures & algorithms 
### Week 01 - Foundations of data structures

# lesson 03: Index-based data structures
seats = ["Anna", "Ben", "Cara", "Diego", "Ella", "Farah"]

# Ask user for seat number:
seat_number = int(input("Enter seat number: "))

if 0 <= seat_number < len(seats):
    print("Seat", seat_number, "holds", seats[seat_number])
else:
    print("No one sits in that seat!")



