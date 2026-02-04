# GNB - 1st - Movie Recommender
import csv
from menu import menu

def main():
    print("What do you want to search for movies by?: ")
    options = ["Genre", "Director Name", "Notable Actor", "Movie Length", "Title", "Rating"]
    for option in options:
        print(option)
    while True:
        choice = menu(options)
        if == 0:
            genre()
        elif == 1:
            (characters, selected_character)
        elif choice.get('index') == 2:
            view_inventory(characters, selected_character)
        elif choice.get('index') == 3:
            return characters, selected_character
