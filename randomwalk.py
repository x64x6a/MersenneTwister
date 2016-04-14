from os import urandom
import random
import turtle
import middlesquare


def repos(tmnt, widths, heights):
    w,h = tmnt.pos()
    neww,newh = w,h

    if w < widths[0]:
        neww = widths[1] - (widths[0] - w)
    elif w > widths[1]:
        neww = widths[0] + (w - widths[1])

    if h < heights[0]:
        newh = heights[1] - (heights[0] - h)
    elif h > heights[1]:
        newh = heights[0] + (h - heights[1])

    if neww != w or newh != h:
        tmnt.penup()
        tmnt.goto(neww,newh)
        tmnt.pendown()

if __name__ == '__main__':
    SPEED = 0
    DIST = 8
    BGCOLOR = "black"

    screen = turtle.Screen()
    screen.title("Random Walk with Mersenne Twister (Red), Middle Square (White) and uRandom (Blue)")

    turtle1 = turtle.Turtle()
    turtle1.getscreen().bgcolor(BGCOLOR)
    turtle2 = turtle.Turtle()
    turtle3 = turtle.Turtle()

    turtle1.speed(SPEED)
    turtle2.speed(SPEED)
    turtle3.speed(SPEED)

    turtle1.color("blue", "#B5BAFF")
    turtle2.color("red", "#FFB5B5")
    turtle3.color("white", "#3B3B3B")

    width,height = turtle1.window_width(), turtle1.window_height()
    widths = -(width/2),(width/2)
    heights = -(height/2),(height/2)

    # set random numbers
    seed = 31337
    rand = random.Random(seed)
    msq = middlesquare.random(seed)

    while True:
        a = rand.getrandbits(32)
        b = int(urandom(4).encode('hex'), 16)
        c = msq.next()

        turtle1.setheading(a)
        turtle1.forward(DIST)

        turtle2.setheading(b)
        turtle2.forward(DIST)

        turtle3.setheading(c)
        turtle3.forward(DIST)

        repos(turtle1, widths, heights)
        repos(turtle2, widths, heights)
        repos(turtle3, widths, heights)

        width,height = turtle1.window_width(), turtle1.window_height()
        widths = -(width/2),(width/2)
        heights = -(height/2),(height/2)




