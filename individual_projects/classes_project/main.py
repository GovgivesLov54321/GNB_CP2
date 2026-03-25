# GNB - 1st - Main thing for geometry calc 

from geometry_calc import *
def menu():
    shapes = []

    while True:
        print("\n=== GEOMETRY CALCULATOR ===")
        print("1. Create Shape")
        print("2. View Shapes")
        print("3. Compare Shapes")
        print("4. Sort Shapes")
        print("5. Formula Guide")
        print("6. Exit")

        choice = input("Choice: ")

        # CREATE SHAPE
        if choice == "1":
            print("\n1. Circle\n2. Rectangle\n3. Square\n4. Triangle")
            shape_choice = input("Select shape: ")

            if shape_choice == "1":
                r = get_positive_number("Enter radius length: ")
                shapes.append(Circle(r))

            elif shape_choice == "2":
                l = get_positive_number("Enter length: ")
                w = get_positive_number("Enter width: ")
                shapes.append(Rectangle(l, w))

            elif shape_choice == "3":
                s = get_positive_number("Enter side length: ")
                shapes.append(Square(s))

            elif shape_choice == "4":
                b = get_positive_number("Enter base length: ")
                h = get_positive_number("Enter height: ")
                shapes.append(Triangle(b, h))

        # VIEW
        elif choice == "2":
            for i, shape in enumerate(shapes):
                print(f"\nShape #{i+1}")
                shape.display()

        # COMPARE
        elif choice == "3":
            if len(shapes) < 2:
                print("Need at least 2 shapes.")
                continue

            i1 = int(input("First shape #: ")) - 1
            i2 = int(input("Second shape #: ")) - 1

            compare_shapes(shapes[i1], shapes[i2])

        # SORT
        elif choice == "4":
            sort_shapes(shapes)

        # FORMULAS
        elif choice == "5":
            show_formulas()
        # EXIT
        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


menu()
