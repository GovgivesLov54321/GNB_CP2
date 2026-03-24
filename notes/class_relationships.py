# GNB - 1st - Class Relationships Notes

# Parent class
class Vehicle:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

# Child class

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car = Car("Ford", "Mustang")
boat = Boat("Ibiza", "Touring 20")
plane = Plane("Boeing", "747")

print(car.brand)
print(car.model)
car.move()


print(boat.brand)
print(boat.model)
boat.move()

print(plane.brand)
print(plane.model)
car.move()

# Aggregation "has a"
class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog

    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("Not in this library unc")
    def view_catalog(self):
        for book in self.catalog:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
lib = Library("Provo Library")

lib.add_book(Book("Black Brother, Black Brother", "Jewell Parker Rhodes"))

lib.view_catalog()