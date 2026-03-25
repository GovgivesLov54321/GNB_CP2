# GNB - 1st - Classes Project Option 2: Geometry Calculator
# GNB - Geometry Calculator (Fixed Version)

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def display(self):
        print(f"Circle (r = {self.radius})")
        print(f"Area: {round(self.area(), 2)}")
        print(f"Perimeter: {round(self.perimeter(), 2)}")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print(f"Rectangle (l = {self.length}, w = {self.width})")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4

    def display(self):
        print(f"Square (side = {self.side})")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

    def perimeter(self):
        return self.base * 3  # assuming equilateral

    def display(self):
        print(f"Triangle (base = {self.base}, height = {self.height})")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Enter a positive number.")
        except:
            print("Invalid input. Try again.")


def compare_shapes(shape1, shape2):
    print("\nComparing Shapes:")

    if shape1.area() > shape2.area():
        print("Shape 1 has larger area")
    else:
        print("Shape 2 has larger area")

    if shape1.perimeter() > shape2.perimeter():
        print("Shape 1 has larger perimeter")
    else:
        print("Shape 2 has larger perimeter")


def sort_shapes(shapes):
    choice = input("Sort by (area/perimeter): ").lower()

    if choice == "area":
        shapes.sort(key=lambda s: s.area())
    elif choice == "perimeter":
        shapes.sort(key=lambda s: s.perimeter())
    else:
        print("Invalid choice.")
        return

    print("\nSorted Shapes:")
    for s in shapes:
        s.display()
        print()

def show_formulas():
    print("\n--- FORMULA GUIDE ---")
    print("Circle -> Area = πr², Perimeter = 2πr")
    print("Rectangle -> Area = l*w, Perimeter = 2(l+w)")
    print("Square -> Area = s², Perimeter = 4s")
    print("Triangle -> Area = (b*h)/2, Perimeter = 3b")
