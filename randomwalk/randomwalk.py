import turtle
import random

wn = turtle.Screen()

turtle1 = turtle.Turtle()

turtle1.color("blue")

turtle1.pencolor("blue")


while True:

	turtle1.setheading(random.randint(0,360))

	turtle1.forward(random.randint(-10,10))

wn.mainloop()

