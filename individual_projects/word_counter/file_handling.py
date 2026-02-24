# GNB - 1st - Word Counter 2/3

from time_handling import get_current_timestamp


def read_document(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None


def clean_word_count(content):
    words = content.split()
    return len(words)


def add_content_to_document(file_path):
    print("Enter new content (press Enter twice to finish):")

    new_lines = []
    while True:
        line = input()
        if line == "":
            break
        new_lines.append(line)

    try:
        with open(file_path, "a", encoding="utf-8") as file:
            for line in new_lines:
                file.write(line + "\n")

        print("\nContent added successfully.")
    except FileNotFoundError:
        print("Error: File not found.")


def update_document_info(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        word_count = clean_word_count(content)
        timestamp = get_current_timestamp()

        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n")
            file.write(f"Word Count: {word_count}\n")
            file.write(f"Last Updated: {timestamp}\n")

        return word_count

    except FileNotFoundError:
        print("Error: File not found.")
        return None
