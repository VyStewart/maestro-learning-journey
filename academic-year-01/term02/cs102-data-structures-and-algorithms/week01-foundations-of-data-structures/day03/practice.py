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

# Removing elements from arrays
players = ["Ava", "Ben", "Josh", "Cara", "Marcus", "Dan", "Eli"]

last_out = players.pop()
first_out = players.pop(0)
middle_out = players.pop(len(players) // 2)

print(last_out)
print(first_out)
print(middle_out)
print(players)

# Combined array operations in sequence 
'''
Take a playlist, remove one song, and return
 
1.the removed song
2.the updated playlist
'''

def remove_first_song(songs):
    # work with song here
    removed = songs.pop(0)
    
    return removed, songs

playlist = ["Intro", "Skyline", "Midnight", "Outro"]
removed, final_playlist = remove_first_song(playlist)

print(removed)
print(final_playlist)

#  Access a song, update another, then remove one from the playlist.
def edit_playlist(songs, access_index, update_index, new_title, remove_index):
    """
    Access a song, update another, then remove one from the playlist.

    Steps:
    1. Read the song at access_index (do not change it).
    2. Change the title at update_index to new_title.
    3. Remove the song at remove_index using pop().
    4. Return the removed song and the final playlist.
    """
    # 1. access (just to show we can read it)
    looked_at = songs[access_index]
    print(f"Looked at: {looked_at}")

    # 2. update
    songs[update_index] = new_title

    # 3. remove
    removed_song = songs.pop(remove_index)

    # 4. return two values (as a tuple)
    return removed_song, songs


playlist = ["Intro", "Skyline", "Midnight", "Outro"]

removed, final_playlist = edit_playlist(
    playlist,
    access_index=1,            # look at "Skyline"
    update_index=2,            # change "Midnight" -> "Midnight Remix"
    new_title="Midnight Remix",
    remove_index=0             # remove "Intro"
)

print("Removed:", removed)
print("Final playlist:", final_playlist)

    