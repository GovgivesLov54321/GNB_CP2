# GNB - 1st - Movie Recommender
import csv
from menu import menu





with open("individual_projects/movie_recommender/movie_list.csv", "r") as csv_file:

#        content = csv.reader(csv_file)
 #       headers = next(content)
  #      rows = []
   #     for line in content:
           #print(f"{line[0]}: {line[1]}")
     #       rows.append({headers[0]: line[0], headers[1]: line[1]}) Kinda using this but change to e.g. header 4 (which would be fifth column in csv thing), and check by row for stuff that less than 70 minutes, then add those to a list that's for example named "acceptable_options" or sum, and then you print that entire row, making sure it looks pretty and allat

def main():
    # Introduction for the user
    print("Welcome to the Movie Recommender!")
    print("You can search for different types of movies based off different criteria.")
    print()

    while True:
        # Display main menu
        print("Choose how to search for a movie:")
        print("1. Movie Title")
        print("2. Director Name")
        print("3. Genre")
        print("4. Age Rating")
        print("5. Movie Length (in minutes)")
        print("6. Notable Actor(s) Name(s)")
        print("7. Exit")
        print()

        choice = input("Please select an option (1-7): ")
        print()

        # Option 1: Movie Title
        if choice == "1":
            print("MORSE CODE TO ENGLISH:")
            code = input("What is the code you need translated?\n")
            print()
            print("Your message says:")
            print(morse_to_english(code))
            print()

        # Option 2: English to Morse
        elif choice == "2":
            print("ENGLISH TO MORSE CODE:")
            ingles = input("What is the message you need translated?\n")
            print()
            print("Your message says:")
            print(english_to_morse(ingles))
            print()

        # Option 7: Exit program
        elif choice == "7":
            print("Aloha! Thanks for using the best movie recommender.")
            break

        # Handle invalid menu input
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            print()


main()