# GNB - 1st - Personal Library Program


# STORE ALL SONGS IN A LIST

song_library = [
    "Cactus by Kofi Stone",
    "After Hours by Kofi Stone",
    "Black Joy by Kofi Stone",
    "I Wish by Kofi Stone",
    "Woof Meow by Saiming",
    "Fee Fi Fo by Saiming",
    "Lungs by Saiming",
    "Nish by Namesbliss",
    "Let Me Play by Tame Dog"
]

# STORE SONGS IN A SET (PREVENT DUPLICATES)
song_set = set(song_library)


# FUNCTION: VIEW SONGS
# Displays all songs in the library

def view_songs():
    print("\n--- YOUR SONG LIBRARY ---")

    if len(song_library) == 0:
        print("Your library is empty.")
    else:
        for song in song_library:
            print(song)


# FUNCTION: ADD A SONG
# Prompts user for song title and artist
# Uses a set to prevent duplicate entries

def add_song():
    title = input("Song title: ").strip()
    artist = input("Artist name: ").strip()

    new_song = f"{title} by {artist}"

    if new_song in song_set:
        print("\nThat song is already in your library.")
    else:
        song_library.append(new_song)
        song_set.add(new_song)
        print(f"\nYou have added:\n{new_song}")


# FUNCTION: REMOVE A SONG
# Displays numbered list and removes selected song

def remove_song():
    if len(song_library) == 0:
        print("There are no songs to remove.")
        return

    print("\n--- SELECT A SONG TO REMOVE ---")
    for index, song in enumerate(song_library, start=1):
        print(f"{index}. {song}")

    choice = input("Enter the number of the song you want to remove: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(song_library):
            removed_song = song_library.pop(choice - 1)
            song_set.remove(removed_song)
            print(f"\nYou have removed:\n{removed_song}")
        else:
            print("Invalid number.")
    else:
        print("Please enter a valid number.")


# FUNCTION: SEARCH SONGS
# Allows search by title or artist

def search_songs():
    print("\nWhat would you like to search by?")
    print("1. Title")
    print("2. Artist")

    choice = input("Enter 1 or 2: ")

    print("\n--- SEARCH RESULTS ---")
    found = False

    if choice == "1":
        keyword = input("Enter song title keyword: ").lower()
        for song in song_library:
            if keyword in song.lower():
                print(song)
                found = True

    elif choice == "2":
        keyword = input("Enter artist name: ").lower()
        for song in song_library:
            if keyword in song.lower():
                print(song)
                found = True
    else:
        print("Invalid choice.")
        return

    if not found:
        print("No matching songs found.")


# FUNCTION: RUN PROGRAM
# Displays menu and controls program flow

def run_library():
    print("Welcome to Your Personal Song Library!")
    print("Manage songs by Kofi Stone, Saiming, and more.\n")

    while True:
        print("\nMAIN MENU")
        print("Type the number for the action you would like to perform")
        print("1. View Songs")
        print("2. Add Song")
        print("3. Remove Song")
        print("4. Search Songs")
        print("5. Exit")

        user_choice = input("Choice: ")

        if user_choice == "1":
            view_songs()
        elif user_choice == "2":
            add_song()
        elif user_choice == "3":
            remove_song()
        elif user_choice == "4":
            search_songs()
        elif user_choice == "5":
            print("¡Hasta la vista! Thanks for using the BEST Song Library.")
            break
        else:
            print("Please enter a valid option (1–5).")


# START THE PROGRAM

run_library()
