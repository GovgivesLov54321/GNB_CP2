# GNB - 1st - main thing for grade book frfr
from grade_book import GradeBook

FILE_PATH = "individual_projects/classes_relationship_project/gradelist.csv"


def main():
    gb = GradeBook()
    gb.load_from_file(FILE_PATH)

    while True:
        print("\n📚 SIMPLE GRADE BOOK 📚")
        print("[1] Add New Student")
        print("[2] Add Grade to Student")
        print("[3] View Student Record")
        print("[4] View All Students")
        print("[5] Class Summary")
        print("[6] Exit")

        choice = input("Choice: ")

        # Add student osns
        if choice == "1":
            name = input("Enter name (First and Last only): ").strip()
            student_id = input("Enter ID (4-digits): ").strip()

            gb.add_student(name, student_id)
            print("Student added.")

        # Add grade ig
        elif choice == "2":
            student_id = input("Enter student ID (4-digits): ")
            student = gb.find_by_id(student_id)

            if student:
                try:
                    grade = float(input("Enter number grade (0-100): "))
                    if student.add_grade(grade):
                        print("Grade added.")
                    else:
                        print("Invalid grade.")
                except:
                    print("Invalid input.")
            else:
                print("Student not found.")

        # View one
        elif choice == "3":
            student_id = input("Enter student ID (4-digits): ")
            student = gb.find_by_id(student_id)

            if student:
                student.display()
            else:
                print("Student not found.")

        # View all
        elif choice == "4":
            gb.display_all()
        
        elif choice == "5":
            gb.class_summary()

        # Exit
        elif choice == "6":
            gb.save_to_file(FILE_PATH)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid option.")


main()
