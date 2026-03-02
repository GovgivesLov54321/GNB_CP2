# GNB - 1st - Fractal Pattern Generator (what're we doing with these assignments LaRose? 💔)

# import turtle cause it'll prob help
# import turtle
# import random (maybe not needed but idk)

# Welcome user osns:
# "Welcome to the Sierpinski Triangle Generator!
#  This program creates a Sierpinski Triangle fractal using recursion."


# define function draw_triangle(t, size)
    # this draws ONE normal triangle
    # repeat 3 times
        # move turtle forward by size
        # turn left 120 degrees


# define recursive function sierpinski(t, depth, size)
    # BASE CASE:
    # if depth == 0
        # draw_triangle(t, size)
        # stop recursion (return)

    # RECURSIVE CASE:
    # otherwise:
        # call sierpinski(t, depth - 1, size / 2)
        # move turtle forward size / 2
        # call sierpinski(t, depth - 1, size / 2)
        # move turtle backward size / 2
        # turn left 60
        # move turtle forward size / 2
        # turn right 60
        # call sierpinski(t, depth - 1, size / 2)
        # turn left 60
        # move turtle backward size / 2
        # turn right 60


# define function triangle_turtle(color, depth)
    # create turtle screen
    # set background color (maybe white unless extra credit)
    # create turtle object
    # set turtle speed to fastest
    # hide turtle so it looks clean
    # set turtle color to color parameter

    # lift pen and move turtle to better starting position (so triangle is centered)
    # put pen down

    # call sierpinski(turtle, depth, starting_size)
        # starting_size could be like 400 or something

    # update screen


# define main function or wtv...
    # print welcome message

    # loop so user can draw again if they want
    # while True:

        # Have user choose recursion depth (1-5)
        # convert input to int
        # validate:
            # if depth < 1 or depth > 5
                # print "invalid depth"
                # continue loop

        # Have user choose color between:
        # red, green, blue, yellow, orange, purple, cyan, magenta, black, white

        # validate color
            # if color not in allowed list
                # print "invalid color"
                # continue loop

        # print "Generating Sierpinski Triangle..."

        # call triangle_turtle(color, depth)

        # print "Fractal generated successfully!"

        # ask user:
        # "Press Enter to exit or type 'again' to draw another triangle: "

        # if user just presses Enter
            # break loop
        # else if user types again
            # clear turtle screen
            # continue loop


# call main()
