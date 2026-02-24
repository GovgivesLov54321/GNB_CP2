# GNB - 1st - Word Counter 1/3
# relative path to copy for it to make your life easier: individual_projects/word_counter/personal_journal.txt

from file_handling import (
    read_document,
    add_content_to_document,
    update_document_info
)


def display_menu():
    print("\n--- Personal Journal Word Count Updater ---")
    print("1. Update document info")
    print("2. View document")
    print("3. Add content to document")
    print("4. Exit")


def main():
    file_path = ""

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            file_path = input(
                "Enter the exact file path for your journal: "
            ).strip()
            word_count = update_document_info(file_path)
            if word_count is not None:
                print(f"Journal updated... Word count: {word_count}")

        elif choice == "2":
            if not file_path:
                file_path = input(
                    "Enter the exact file path for your journal: "
                ).strip()
            content = read_document(file_path)
            if content is not None:
                print("\nJournal content:\n")
                print(content)

        elif choice == "3":
            if not file_path:
                file_path = input(
                    "Enter the exact file path for your journal: "
                ).strip()
            add_content_to_document(file_path)

        elif choice == "4":
            print("Hasta la pronto. Thanks for using this for your personal journal.")
            break

        else:
            print("Please enter a valid option (1-4).")


if __name__ == "__main__":
    main()
