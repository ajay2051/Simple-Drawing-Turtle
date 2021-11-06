import turtle

turtle.bgcolor('black')

turtle.pensize(3)

# turtle.color("white")
turtle.speed(0)

#Draw Square

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done() # Square stays on screen

# Draw nice little drawings.

for i in range(6):
    for colors in ['white', 'aqua', 'yellow', 'green', 'blue', 'pink']:
        turtle.color(colors)
        turtle.circle(150)
        turtle.left(10)
turtle.done()

