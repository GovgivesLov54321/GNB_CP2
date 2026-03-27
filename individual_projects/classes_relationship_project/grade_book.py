# GNB - 1st - Class Relationships Project Option 1: Simple Grade Book
#Lwk kinda understand what needs to be done
import math
import csv


class Student:
    def __init__(self, name, student_id, grade_list):
        self.name = name
        self.student_id = student_id
        self.grade_list = grade_list

    def add_student(student_name, student_id):
        student_name = input("What is the name of the student you'd like to add? (Format = First Middle initial Last): ").strip()
        student_id = int(input("What's their four-digit student ID?: "))
    
    def find_student():
        search_choice = input("Which would you like to search by (Enter a number):" \
        "1. Student Last Name" \
        "2. Student ID Number")
        if search_choice == 1:
            with open("individual_projects\classes_relationship_project\grade_list.csv", mode = "r+") as csv_file:



class GradeBook:
    def __init__(self):
        pass