# GNB - 1st - Fractal Pattern Generator (what're we doing with these assignments LaRose? 💔)

# import turtle cause it'll prob help
import turtle


# define function draw_triangle(t, size)
def draw_triangle(t, size):
    # this draws ONE normal triangle
    for _ in range(3):
        t.forward(size)
        t.left(120)


# define recursive function sierpinski(t, depth, size)
def sierpinski(t, depth, size):

    # BASE CASE:
    # if depth == 0
    if depth == 0:
        # draw_triangle(t, size)
        draw_triangle(t, size)
        # stop recursion
        return

    # RECURSIVE CASE:
    # otherwise break triangle into 3 smaller ones
    sierpinski(t, depth - 1, size / 2)

    t.forward(size / 2)
    sierpinski(t, depth - 1, size / 2)
    t.backward(size / 2)

    t.left(60)
    t.forward(size / 2)
    t.right(60)

    sierpinski(t, depth - 1, size / 2)

    t.left(60)
    t.backward(size / 2)
    t.right(60)


# define function triangle_turtle(color, depth)
def triangle_turtle(color, depth):

    # create turtle screen
    screen = turtle.Screen()
    screen.title("Sierpinski Triangle Generator")

    # create turtle object
    t = turtle.Turtle()

    # set turtle speed to fastest
    t.speed(0)

    # hide turtle so it looks clean
    t.hideturtle()

    # set turtle color to color parameter
    t.color(color)

    # lift pen and move turtle to better starting position
    t.penup()
    t.goto(-200, -150)
    t.pendown()

    # call sierpinski(turtle, depth, starting_size)
    starting_size = 400
    sierpinski(t, depth, starting_size)

    # update screen
    screen.update()

    return screen


# define main function or wtv...
def main():

    # print welcome message
    print("Welcome to the Sierpinski Triangle Generator!")
    print("This program creates a Sierpinski Triangle fractal using recursion.")

    # loop so user can draw again if they want
    while True:

        # Have user choose recursion depth (1-5)
        try:
            depth = int(input("\nEnter recursion depth (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # validate depth
        if depth < 1 or depth > 5:
            print("Depth must be between 1 and 5.")
            continue

        # Have user choose color
        color = input("Enter triangle color (red, green, blue, yellow, orange, purple, cyan, magenta, black, white): ").lower()

        allowed_colors = [
            "red", "green", "blue", "yellow",
            "orange", "purple", "cyan",
            "magenta", "black", "white"
        ]

        # validate color
        if color not in allowed_colors:
            print("Invalid color choice.")
            continue

        print("\nGenerating Sierpinski Triangle...")

        # call triangle_turtle(color, depth)
        screen = triangle_turtle(color, depth)

        print("Fractal generated successfully!")

        # ask user what to do next
        choice = input("\nPress Enter to exit or type 'again' to draw another triangle: ").lower()

        if choice != "again":
            break

        # clear turtle screen before next run
        turtle.clearscreen()

    print("Goodbye!")


# call main()
if __name__ == "__main__":
    main()
