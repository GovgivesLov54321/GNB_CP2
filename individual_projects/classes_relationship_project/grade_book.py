# GNB - 1st - Class Relationships Project Option 1: Simple Grade Book
#Lwk kinda understand what needs to be done
import csv

class Student:
    def __init__(self, name, student_id, grade_list=None):
        self.name = name
        self.student_id = student_id
        self.grade_list = grade_list if grade_list else []

    # add a grade to student
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grade_list.append(grade)
            return True
        return False

    # calculate average
    def get_average(self):
        if len(self.grade_list) == 0:
            return 0
        return sum(self.grade_list) / len(self.grade_list)

    # convert to letter grade
    def get_letter_grade(self):
        avg = self.get_average()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    # display student info
    def display(self):
        if self.grade_list:
            print(f"Name: {self.name}")
            print(f"ID: {self.student_id}")
            print(f"Grade: {self.grade_list}%")
            print(f"Average: {round(self.get_average(), 2)}% ({self.get_letter_grade()})")
        else:
            print(f"Name: {self.name}")
            print(f"ID: {self.student_id}")
            print("Grades: None yet")


class GradeBook:
    def __init__(self):
        self.students = []

    # add student
    def add_student(self, name, student_id):
        self.students.append(Student(name, student_id))

    # find by ID
    def find_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    # find by name
    def find_by_name(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    # show all students
    def display_all(self):
        if not self.students:
            print("No students yet.")
            return

        for student in self.students:
            print("----------------------")
            student.display()

    # class summary
    def class_summary(self):
        if not self.students:
            print("No students to summarize.")
            return

        total = 0
        count = 0

        for student in self.students:
            total += student.get_average()
            count += 1

        print(f"Total Students: {count}")
        print(f"Class Average: {round(total / count, 2)}%")

    # Save to CSV
    def save_to_file(self, filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "student_id", "grades"])

            for student in self.students:
                grades_str = "|".join(map(str, student.grade_list))
                writer.writerow([student.name, student.student_id, grades_str])

    # load from CSV
    def load_from_file(self, filename):
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                self.students = []

                for row in reader:
                    grades = row["grades"].split("|") if row["grades"] else []
                    grades = [float(g) for g in grades if g]

                    student = Student(row["name"], row["student_id"], grades)
                    self.students.append(student)
        except FileNotFoundError:
            print("File not found. Starting new gradebook.")
