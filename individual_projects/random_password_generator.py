# GNB - 1st - Random Password Generator
import random


# Function returns a list of lowercase letters
def get_lowercase_letters():
    return list("abcdefghijklmnopqrstuvwxyz")


# Function returns a list of uppercase letters
def get_uppercase_letters():
    return list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


# Function returns a list of digits
def get_numbers():
    return list("0123456789")


# Function returns a list of special characters
def get_special_characters():
    return list("!@#$%^&*()-_=+[]{}|;:',.<>?/")


# Function builds a list of allowed characters based on user choices
def build_character_pool(include_lower, include_upper, include_numbers, include_special):
    character_pool = []

    if include_lower:
        character_pool.extend(get_lowercase_letters())

    if include_upper:
        character_pool.extend(get_uppercase_letters())

    if include_numbers:
        character_pool.extend(get_numbers())

    if include_special:
        character_pool.extend(get_special_characters())

    return character_pool


# Function creates a password of the desired length from the character pool
def generate_password(length, character_pool):
    password = ""

    for _ in range(length):
        password += random.choice(character_pool)

    return password


# Function generates and displays 4 passwords
def generate_passwords():
    length = int(input("How long does the password need to be: "))

    include_lower = input("Does the password need lowercase letters (Y/N): ").strip().lower() == "y"
    include_upper = input("Does the password need uppercase letters (Y/N): ").strip().lower() == "y"
    include_numbers = input("Does the password need numbers (Y/N): ").strip().lower() == "y"
    include_special = input("Does the password need special characters (Y/N): ").strip().lower() == "y"

    character_pool = build_character_pool(
        include_lower,
        include_upper,
        include_numbers,
        include_special
    )

    if len(character_pool) == 0:
        print("You must select at least one character type.")
        return

    print("\nPossible Passwords:\n")

    for _ in range(4):
        print(generate_password(length, character_pool))


# Function displays menu and controls program flow
def main():
    print("Welcome to the Password Generator!")
    print("You can customize your password requirements.\n")

    while True:
        print("\nMAIN MENU")
        print("1. Generate Passwords")
        print("2. Exit")

        choice = input("Choice: ")

        if choice == "1":
            generate_passwords()
        elif choice == "2":
            print("Goodbye! Stay secure 😎")
            break
        else:
            print("Please enter a valid option (1 or 2).")


main()
