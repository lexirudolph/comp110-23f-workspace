"""Turtle Project: Happy Halloween!"""

__author__ = "730416818"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene: Drawing a spooky haunted house!"""
    jack: Turtle = Turtle()
    draw_canvas(jack, -500.0, -500.0)
    draw_ground(jack, -500.0, -500.0)
    draw_house(jack, -250.0, -250.0)
    draw_roof(jack, -250.0, 250.0)
    draw_windows(jack, -200.0, 50.0)
    draw_windows(jack, 75.0, 50.0)
    draw_door(jack, -75.0, -250.0)  
    draw_jacks(jack, -170.0, -200.0)
    draw_jacks(jack, 150.0, -200.0)
    done()


def draw_canvas(c_turtle: Turtle, x: float, y: float) -> None:
    """Draw the canvas (background) of the scene."""
    c_turtle.color(0, 0, 0)
    c_turtle.begin_fill()
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.setheading(0.0)
    c_turtle.pendown()
    i: int = 0
    while (i < 4):
        c_turtle.forward(1000)
        c_turtle.left(90)
        i += 1
    c_turtle.end_fill()


def draw_ground(g_turtle: Turtle, x: float, y: float) -> None:
    """Draw the ground of the scene beginning at x, y coordinates."""
    g_turtle.color(122, 116, 93)
    g_turtle.begin_fill()
    g_turtle.penup()
    g_turtle.goto(x, y)
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


def draw_house(h_turtle: Turtle, x: float, y: float) -> None:
    """Draw a spooky house beginning at x, y coordinates."""
    h_turtle.color(96, 34, 160)
    h_turtle.begin_fill()
    h_turtle.penup()
    h_turtle.goto(x, y)
    h_turtle.setheading(0.0)
    h_turtle.pendown()
    i: int = 0
    while (i < 4):
        h_turtle.forward(500)
        h_turtle.left(90)
        i += 1
    h_turtle.end_fill()
    

def draw_roof(r_turtle: Turtle, x: float, y: float) -> None:
    """Draw the roof of the spooky house beginning at x, y coordinates."""
    r_turtle.color(137, 145, 119)
    r_turtle.begin_fill()
    r_turtle.penup()
    r_turtle.goto(x, y)
    r_turtle.setheading(0.0)
    r_turtle.pendown()
    r_turtle.forward(500)
    r_turtle.left(140)
    r_turtle.forward(326.352)
    r_turtle.left(80)
    r_turtle.forward(326.352)
    r_turtle.end_fill()


def draw_windows(w_turtle: Turtle, x: float, y: float) -> None:
    """Draw two spooky windows on the house beginning at x, y coordinates."""
    w_turtle.color(255, 243, 0)
    w_turtle.penup()
    w_turtle.goto(x, y)
    w_turtle.setheading(0.0)
    w_turtle.pendown()
    w_turtle.begin_fill()
    w: int = 0
    while (w < 4):
        w_turtle.forward(120)
        w_turtle.left(90)
        w += 1
    w_turtle.end_fill()
    w_turtle.color(0, 0, 0)
    w_turtle.penup()
    w_turtle.goto(x, y)
    w_turtle.setheading(0.0)
    w_turtle.pendown()
    wi: int = 0
    while (wi < 4):
        w_turtle.forward(120)
        w_turtle.left(90)
        wi += 1
    w_turtle.penup()
    w_turtle.goto(x + 60, y)
    w_turtle.setheading(0.0)
    w_turtle.pendown()
    w_turtle.left(90)
    w_turtle.forward(120)
    w_turtle.penup()
    w_turtle.goto(x, y + 60)
    w_turtle.setheading(0.0)
    w_turtle.pendown()
    w_turtle.forward(120)


def draw_door(d_turtle: Turtle, x: float, y: float) -> None:
    """Draw a spooky door on house beginning at x, y coordinates."""
    d_turtle.color(47, 41, 63)
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.setheading(0.0)
    d_turtle.pendown()
    d_turtle.begin_fill()
    d_turtle.forward(150)
    d_turtle.left(90)
    d_turtle.forward(250)
    d_turtle.left(90)
    d_turtle.forward(150)
    d_turtle.left(90)
    d_turtle.forward(250)
    d_turtle.end_fill()


def draw_jacks(j_turtle: Turtle, x: float, y: float) -> None:
    """Draw spooky jack-o-lanterns in front of the house beginning at x, y coordinates with varying widths."""
    j_turtle.color(242, 167, 0)
    j_turtle.speed(100)
    j_turtle.penup()
    j_turtle.goto(x, y)
    j_turtle.setheading(0.0)
    j_turtle.pendown()
    j_turtle.width(100)
    side_length: float = 30
    i: int = 0
    while (i < 50):
        j_turtle.forward(side_length)
        j_turtle.left(130)
        i = i + 1
        side_length = side_length * 0.97
    j_turtle.color(35, 130, 26)
    j_turtle.penup()
    j_turtle.goto(x + 10, y + 70)
    j_turtle.setheading(0.0)
    j_turtle.pendown()
    j_turtle.width(20)
    j_turtle.left(90)
    j_turtle.forward(10)
    j_turtle.color(0, 0, 0)
    j_turtle.penup()
    j_turtle.goto(x - 25, y + 20)
    j_turtle.setheading(0.0)
    j_turtle.pendown()
    j_turtle.width(1)
    j_turtle.begin_fill()
    e: int = 0
    while (e < 3):
        j_turtle.forward(20)
        j_turtle.left(120)
        e += 1
    j_turtle.end_fill()
    j_turtle.penup()
    j_turtle.goto(x + 25, y + 20)
    j_turtle.setheading(0.0)
    j_turtle.pendown()
    j_turtle.width(1)
    j_turtle.begin_fill()
    ei: int = 0
    while (ei < 3):
        j_turtle.forward(20)
        j_turtle.left(120)
        ei += 1
    j_turtle.end_fill()
    j_turtle.penup()
    j_turtle.goto(x - 10, y - 10)
    j_turtle.setheading(0.0)
    j_turtle.pendown()
    j_turtle.width(20)
    j_turtle.left(45)
    m: int = 0
    while (m < 3):
        j_turtle.forward(10)
        j_turtle.right(90)
        j_turtle.forward(10)
        j_turtle.left(90)
        m += 1