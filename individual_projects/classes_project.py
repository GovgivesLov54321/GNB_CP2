# GNB - 1st - Classes Project Option 2: Geometry Calculator
import math

class Circle: #will be asking for radius -- radius give diameter (which is 2*r) -- circumference (which is 2*math.pi*r) -- area (which is math.pi*r**2)
    def __init__(self, circle, radius, diameter, area, circumference):
        self.circle = circle
        self.radius = radius
        self.diameter = diameter
        self.area = area
        self.circumference = circumference


class Rectangle: #will be asking for height & base -- height & base give area (which is b*h) -- perimeter (which is 2*b + 2*h)
    def __init__(self, rectangle, area, perimeter, height, base):
        self.rectangle = rectangle
        self.area = area
        self.perimeter = perimeter
        self.height = height
        self.base = base
    class Square: #will be asking for height/base -- height & base give area (which is b*h) -- perimeter (which is b and/or height*4)
            def __init__(self, square, area, perimeter, height_and_or_base):
                self.square = square
                self.area = area
                self.perimeter = perimeter
                self.height_and_or_base = height_and_or_base
class Triangle: #will be asking for base & height
    def __init__(self, triangle, area, perimeter, height, base):
        self.triangle = triangle
        self.area = area
        self.perimeter = perimeter
        self.height = height
        self.base = base

# this prints out pi for python osns: print(math.pi)