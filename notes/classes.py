# GNB - 1st - Classes Notes

class Animal: #name classes in PascalCase; every word in name is capitalized
    def __init__(self, name, species, age): #initialize
        self.name = name
        self.species = species
        self.age = age

    def __str__(self): #string
        return f"""Name = {elephant.name}
species = {elephant.species}
age = {elephant.age}"""
    
    def birthday(self):
        self.age += 1

elephant = Animal("LeBronita", "Loxodonta cyclotis", 25)
print(elephant)
elephant.birthday()
print(elephant)

class ClassPeriod:
    def __init__(self, subject, teacher, room = None):
        self.subject = subject.title()
        self.teacher = teacher
        self.room = room

    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}\n"

first = ClassPeriod("Computer Programming 2", "Ms LaRose", room = "200")
second = ClassPeriod("English 10 Honors", "Ms Jensen", room = "67")
print(first, second)

#Wassup twin