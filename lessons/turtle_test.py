from turtle import Turtle, colormode, done
colormode(255)
g_turtle: Turtle = Turtle()
g_turtle.color(122, 116, 93)
g_turtle.begin_fill()
g_turtle.penup()
g_turtle.goto(-500, -500)
g_turtle.setheading(0.0)
g_turtle.pendown()
g_turtle.forward(1000)
g_turtle.left(90)
g_turtle.forward(250)
g_turtle.left(90)
g_turtle.forward(1000)
g_turtle.left(90)
g_turtle.forward(250)
g_turtle.left(90)
g_turtle.end_fill()