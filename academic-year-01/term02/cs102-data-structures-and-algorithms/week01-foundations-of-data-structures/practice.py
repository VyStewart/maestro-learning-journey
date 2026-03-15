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


# Acessing elements in an array
cities = ["Katy", "Houston", "Sugar Land", "Willowbrook"]

index = 3
new_city = "Tomball"

# Check if index is valid for INSERT (0 through len(cities))
if 0 <= index <= len(cities):
    cities.insert(index, new_city)
    print(f"Updated cities: {cities}")
    print(f"Valid indices for access are now 0 to {len(cities) - 1}")
else:
    print("Index out of range for insert")
    
# updating and replacing array values 
movies = ["M1", "M2", "M3", "M4", "M5", "M6", "M7"]

first_index = 0
mid_index = len(movies) // 2
last_index = len(movies) - 1

movies[first_index]= "First Fav"
movies[mid_index] = "Middle Fav"
movies[last_index] = "Last Fav"
movies[2] = "Custom 2"
movies[4] = "Custome 4"

print(movies)

