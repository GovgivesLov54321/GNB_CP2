# GNB - 1st - Simple Morse Code Translator


english = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
morse_code = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")

def english_to_morse(message):
       # Convert message to lowercase
    message = message.lower()
    translated = ""

    # Loop through each character in the message
    for char in message:
        # Check if character exists in English tuple
        if char in english:
            index = english.index(char)
            translated += morse_code[index] + " "
        else:
            # Handle characters not in Morse Code
            translated += "? "

    return translated.strip()

def morse_to_english(message):
    translated = ""
    morse = message.split()

    # Loop through each Morse symbol
    for symbol in morse:
        # Check if symbol exists in Morse tuple
        if symbol in morse:
            index = morse.index(symbol)
            translated += english[index]
        else:
            # Handle invalid Morse symbols
            translated += "?" # Wasn't sure how to make it just say, "Not Morse Code" or something like that...

    return translated
def main():
    # Introduction for the user
    print("Welcome to the Morse Code Translator!")
    print("You can translate English to Morse Code or Morse Code to English.")
    print()

    while True:
        # Display main menu
        print("MAIN MENU:")
        print("1. Translate from Morse Code to English")
        print("2. Translate from English to Morse Code")
        print("3. Exit")
        print()

        choice = input("Please select an option (1-3): ")
        print()

        # Option 1: Morse to English
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

        # Option 3: Exit program
        elif choice == "3":
            print("Ciao! Thanks for using the best morse code translator.")
            break

        # Handle invalid menu input
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            print()


main()