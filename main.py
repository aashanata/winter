import turtle

screen=turtle.Screen()

screen.screensize(500.500)
screen.bgcolor('blue')
t_ground=turtle.Turtle()
t_ground.speed(0)
t_ground.pencolor("brown4")
t_ground.fillcolor("white")

t_ground.penup()
t_ground.goto(-1000,-100)

t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

#tree

t_ground.speed(0)

t_ground.pencolor('lightgreen')

t_ground.penup()

t_ground.goto(-50,100)

t_ground.pendown()

t_ground.fillcolor('lightgreen')

t_ground.begin_fill()

t_ground.goto(50,100)

t_ground.goto(0,180)

t_ground.goto(-50,100)

t_ground.penup()

t_ground.goto(-60,60)

t_ground.pendown()

t_ground.goto(60,60)

t_ground.goto(0,140)

t_ground.goto(-60,60)

t_ground.penup()

t_ground.goto(-70,20)

t_ground.pendown()

t_ground.goto(70,20)

t_ground.goto(0,100)

t_ground.goto(-70,20)

t_ground.penup()

t_ground.goto(-80,-20)

t_ground.pendown()

t_ground.goto(80,-20)

t_ground.goto(0,60)

t_ground.goto(-80,-20)

t_ground.penup()

t_ground.goto(-90,-60)

t_ground.pendown()

t_ground.goto(90,-60)

t_ground.goto(0,20)

t_ground.goto(-90,-60)

t_ground.end_fill()

t_ground.speed(0)

t_ground.pencolor('brown')

t_ground.fillcolor('brown')

t_ground.begin_fill()

t_ground.penup()

t_ground.goto(-10,-110)

t_ground.pendown()

t_ground.forward(25)

t_ground.left(90)

t_ground.forward(50)

t_ground.left(90)

t_ground.forward(25)

t_ground.left(90)

t_ground.forward(50)

t_ground.end_fill()


import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Create a turtle named "snowman"
snowman = turtle.Turtle()
snowman.speed(2)

# Function to draw a circle
def draw_circle(t, radius, color):
    t.penup()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.pendown()

# Move the snowman to the right by adjusting the x-coordinate
x_offset = 100

# Draw the bottom circle (body)
snowman.penup()
snowman.goto(x_offset, -150)
snowman.pendown()
draw_circle(snowman, 60, "white")

# Draw the middle circle (body)
snowman.penup()
snowman.goto(x_offset, -50)
snowman.pendown()
draw_circle(snowman, 45, "white")

# Draw the top circle (head)
snowman.penup()
snowman.goto(x_offset, 50)
snowman.pendown()
draw_circle(snowman, 30, "white")

# Draw eyes
snowman.penup()


turtle.done()