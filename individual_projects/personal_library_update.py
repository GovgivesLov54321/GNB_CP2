# GNB - Personal Library Program Update

import csv

DEFAULT_FILE = "library.csv"
FIELDS = ["title", "creator", "year", "genre"]


def load_library(file_path):
    library = []

    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    library.append({
                        "title": row["title"].strip(),
                        "creator": row["creator"].strip(),
                        "year": int(row["year"]),
                        "genre": row["genre"].strip()
                    })
                except:
                    print("Warning: Skipped a bad row.")
    except FileNotFoundError:
        # Create file if it doesn't exist
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

    return library


def save_library(file_path, library):
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(library)

    print("Library saved.")


def show_simple(library):
    if not library:
        print("Library is empty.")
        return

    for i, item in enumerate(library, start=1):
        print(f"{i}. {item['title']} by {item['creator']}")


def show_detailed(library):
    if not library:
        print("Library is empty.")
        return

    for i, item in enumerate(library, start=1):
        print(f"\nItem {i}")
        print(f"Title: {item['title']}")
        print(f"Creator: {item['creator']}")
        print(f"Year: {item['year']}")
        print(f"Genre: {item['genre']}")



def add_item(library):
    print("\nAdd New Item")

    title = input("Title: ").strip()
    creator = input("Creator: ").strip()

    while True:
        year_input = input("Year: ").strip()
        if year_input.isdigit():
            year = int(year_input)
            break
        print("Year must be a number.")

    genre = input("Genre: ").strip()

    library.append({
        "title": title,
        "creator": creator,
        "year": year,
        "genre": genre
    })

    print("Item added.")



def update_item(library):
    show_simple(library)
    if not library:
        return

    choice = input("Item number to update: ")

    if not choice.isdigit() or not (1 <= int(choice) <= len(library)):
        print("Invalid selection.")
        return

    item = library[int(choice) - 1]

    for key in item:
        new_value = input(f"{key.title()} ({item[key]}): ").strip()
        if new_value:
            if key == "year":
                if new_value.isdigit():
                    item[key] = int(new_value)
                else:
                    print("Invalid year. Kept original.")
            else:
                item[key] = new_value

    print("Item updated.")



def delete_item(library):
    show_simple(library)
    if not library:
        return

    choice = input("Item number to delete: ")

    if not choice.isdigit() or not (1 <= int(choice) <= len(library)):
        print("Invalid selection.")
        return

    removed = library.pop(int(choice) - 1)
    print(f"Deleted: {removed['title']}")


def run_program():
    file_path = input(f"Welcome to the Personal Library Program. \nWhat do you want to name your library? (Enter for {DEFAULT_FILE}): ").strip()
    if not file_path:
        file_path = DEFAULT_FILE

    library = load_library(file_path)
    unsaved = False

    while True:
        print("\nMAIN MENU")
        print("1. Show simple list")
        print("2. Show detailed list")
        print("3. Add item")
        print("4. Update item")
        print("5. Delete item")
        print("6. Save")
        print("7. Reload")
        print("8. Exit")

        choice = input("Choice: ").strip()

        if choice == "1":
            show_simple(library)
        elif choice == "2":
            show_detailed(library)
        elif choice == "3":
            add_item(library)
            unsaved = True
        elif choice == "4":
            update_item(library)
            unsaved = True
        elif choice == "5":
            delete_item(library)
            unsaved = True
        elif choice == "6":
            save_library(file_path, library)
            unsaved = False
        elif choice == "7":
            library = load_library(file_path)
            print("Library reloaded.")
        elif choice == "8":
            if unsaved:
                save_choice = input("Unsaved changes. Save before exit? (y/n): ").lower()
                if save_choice == "y":
                    save_library(file_path, library)
            print("Goodbye. Thanks for using the best Personal Song Library. :o")
            break
        else:
            print("Choose 1-8.")


run_program()
