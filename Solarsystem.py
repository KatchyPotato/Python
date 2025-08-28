import turtle
import random
turtle.getscreen()
turtle.shape("circle")
turtle.shapesize(0.3)
turtle.hideturtle()
turtle.bgcolor("navy")
turtle.title("Solar System")
turtle.penup()
turtle.left(180)
turtle.forward(150)
turtle.left(180)

turtle.showturtle()

turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.pendown()
turtle.circle(40)
turtle.end_fill()
turtle.penup()

turtle.forward(55)

turtle.pencolor("brown")
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.pendown()
turtle.circle(3)
turtle.end_fill()
turtle.penup()

turtle.forward(30)

turtle.pencolor("grey")
turtle.fillcolor("grey")
turtle.begin_fill()
turtle.pendown()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.forward(30)

turtle.pencolor("lime")
turtle.fillcolor("lime")
turtle.begin_fill()
turtle.pendown()
turtle.circle(8)
turtle.end_fill()
turtle.penup()

turtle.forward(30)

turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.pendown()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.forward(30)

turtle.pencolor("orange")
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.pendown()
turtle.circle(15)
turtle.end_fill()
turtle.penup()

turtle.forward(35)

turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.pendown()
turtle.circle(10)
turtle.end_fill()
turtle.penup()

turtle.forward(30)

turtle.pencolor("lightblue")
turtle.fillcolor("lightblue")
turtle.begin_fill()
turtle.pendown()
turtle.circle(8)
turtle.end_fill()
turtle.penup()

turtle.forward(30)

turtle.pencolor("purple")
turtle.fillcolor("purple")
turtle.begin_fill()
turtle.pendown()
turtle.circle(8)
turtle.end_fill()
turtle.penup()

turtle.pencolor("white")
turtle.fillcolor("white")
turtle.left(180)
turtle.forward(280)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.write("Sun")

turtle.right(90)
turtle.forward(115)
turtle.left(90)
turtle.forward(50)
turtle.write("Mercury")

turtle.left(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(30)
turtle.write("Venus")

turtle.right(90)
turtle.forward(45)
turtle.left(90)
turtle.forward(35)
turtle.write("Earth")

turtle.forward(30)
turtle.write("Mars")

turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(25)
turtle.write("Jupiter")

turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(40)
turtle.write("Saturn")

turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.write("Uranus")

turtle.left(90)
turtle.forward(45)
turtle.right(90)
turtle.forward(30)
turtle.write("Neptune")

#ChatGPT helped with code for random stars

stars = 500

screen = turtle.Screen()
width, height = screen.screensize()
turtle.speed(0)

while stars > 0:
    x = random.randint(-width, width)
    y = random.randint(-height, height)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(3)
    stars -= 1

turtle.hideturtle()
