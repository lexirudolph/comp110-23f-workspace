from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.color(255, 209, 0)
#EXERCISE 1: make a square
##def ex_01():
#    leo.forward(100)
 #   leo.right(90)
  #  leo.forward(100)
   # leo.right(90)
    #leo.forward(100)
    #leo.right(90)
    #leo.forward(100)
    #done()

#To simplify: Use a while loop like this:
i: int = 0
side_length: int = 200
while (i < 4):        
    leo.forward(300)        
    leo.left(90)        
    i = i + 1

leo.penup()
leo.goto(55, 55)
leo.pendown()
 
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

#EXERCISE 2: make a triangle with a while loop
#i: int = 0    
#while (i < 3):        
 #   leo.forward(300)        
  #  leo.left(120)        
   # i = i + 1

#To move the turtle to a new x, y position:
    #leo.goto(x, y)

#How to change color! (R, G, B)
leo.color(42, 130, 52)

#Any of these can be used to determine color:
#    leo.pencolor("pink")
 #   leo.fillcolor(32, 67, 93)
  #  leo.color("green", "yellow")


#EXERCISE 3:
leo.speed(50)
leo.hideturtle()


"""Mini Project!"""
bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.penup()
bob.goto(55, 55)
bob.pendown()
bob.speed(75)

i: int = 0
while (i < 30):
    bob.forward(side_length)
    bob.left(130)
    i = i + 1
    side_length = side_length * 0.97

done()