# GNB - 1st - Simple Morse Code Translator

from menu import menu

english = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
morse_code = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")

def english_to_morse():
    help

def morse_to_english():
    help

def main():
    options = ["Translate Morse Code to English", "Translate English to Morse Code", "Exit"]
    while True:
        choice = menu(options)
        if choice == 0:
            morse_to_english()
        elif choice == 1:
            english_to_morse()
        elif choice == 2:
            print("Hope you had fun using the best morse code translator of all time. See ya :]")
            break