# GNB - 1st - Classes Project Option 2: Geometry Calculator
import math
from main import menu


class Circle: #will be asking for radius -- radius give diameter (which is 2*r) -- circumference (which is 2*math.pi*r) -- area (which is math.pi*r**2)
    r = float(input("Enter a radius (positive number): "))
    def __init__(self, circle, radius, diameter, area, circumference):
        self.circle = circle
        self.radius = radius
        self.diameter = diameter
        self.area = area
        self.circumference = circumference
    
    def calculate_circle(radius):
        diameter = radius * 2
        circumference = 2*math.pi*radius
        area = math.pi*(radius**2)
    
    def __str__(self): #string
                    return f"""┌─────────────────────────────────────┐
        │ Shape: Circle #1                    │
        │ Radius: {circle.} units                  │
        │ Area: 95.03 units²                 │
        │ Perimeter: 34.56 units             │
        │ Diameter: 11.0 units               │
        └─────────────────────────────────────┘"""

circle = Circle("")
class Rectangle: #will be asking for height & base -- height & base give area (which is b*h) -- perimeter (which is 2*b + 2*h)
    h = float(input("Enter a height length (positive number): "))
    b = float(input("Enter a base length (positive number): "))
    def __init__(self, rectangle, area, perimeter, height, base):
        self.rectangle = rectangle
        self.area = area
        self.perimeter = perimeter
        self.height = height
        self.base = base
    
    def calculate_rectangle(height, base):
        area = height * base
        perimeter = (height * 2) + (base * 2)


class Square: #will be asking for height/base -- height/base give area (which is b*h) -- perimeter (which is b and/or height*4)
    h_and_or_b = float(input("Enter a side length (positive number):"))
    def __init__(self, square, area, perimeter, height_and_or_base):
        self.square = square
        self.area = area
        self.perimeter = perimeter
        self.height_and_or_base = height_and_or_base

    def calculate_square(height_and_or_base):
        area = height_and_or_base ** 2
        perimeter = height_and_or_base * 4



class Triangle: #will be asking for base & height -- base give area (which is b*h/2) -- perimeter (which is b*3)
    b = float(input("Enter a base length (positive number): "))
    h = float(input("Enter a height length (positive number): "))
    def __init__(self, equilateral_triangle, area, perimeter, height, base):
        self.equilateral_triangle = equilateral_triangle
        self.area = area
        self.perimeter = perimeter
        self.height = height
        self.base = base
    
    def calculate_triangle(height, base):
        area = (height * base) / 2
        perimeter = base * 3

# this prints out pi for python osns: print(math.pi)