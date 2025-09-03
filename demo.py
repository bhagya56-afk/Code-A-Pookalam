import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# --- Helper: draw a filled circle ---
def FILLcircle(radius, color):
    t.color(color)
    t.penup()
    t.setheading(270)
    t.forward(radius)
    t.setheading(0)
    t.pendown()

    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
    t.penup()
    t.setheading(90) 
    t.forward(radius)
    t.setheading(0)
    t.pendown()

# --- Helper: draw Circle Set (CS) ---
def CS(a, b, c, d, fill_color):
    """
    a = radius of big imaginary circle
    b = number of small circles around
    c = radius of each small circle
    d = whether to fill (1 = yes)
    fill_color = color string
    """
    # Store turtle's original position and heading
    original_position = t.pos()
    original_heading = t.heading()

    t.color(fill_color)
    t.speed(0)
    angle= 360 / b

    for i in range(b):
        theta = math.radians(i * angle)
        center_x = a * math.cos(theta)
        center_y = a * math.sin(theta)

        t.penup()
        t.goto(center_x, center_y - c)  # adjust so circle is centered
        t.pendown()

        if d == 1:
            t.fillcolor(fill_color)
            t.begin_fill()
            
        t.circle(c)
        if d == 1:
            t.end_fill()

    # Return turtle to original state
    t.penup()
    t.goto(original_position)
    t.setheading(original_heading)
    t.pendown()

def petal(length=100,x1=250,x2=65,x3=64):
    t.color(x1,x2,x3)
    t.begin_fill()
    for i in range(9):
        t.forward(length)
        t.circle(length/4,208)
        t.forward(length)
        t.right(180)
        t.right(-17)
    t.end_fill()

t = turtle.Turtle()

    

# --- Demo Design ---
CS(280,24,40,1,"Orange")
FILLcircle(280, "green")
# --- Draw 24 small circles inside the large green circle ---
inner_radius = 220  # radius of imaginary circle inside green
num_circles = 24   # number of circles in the ring
circle_size = 40    # radius of each small circle

CS(inner_radius, num_circles, circle_size, 1, "yellow")  # fill color can match green
FILLcircle(200, "red")
 # --- Add small white circles inside red circle ---
CS(160, 12, 15, 1, "white")  # 12 small white circles, radius 15, filled

FILLcircle(150, "brown")

CS(100, 24, 30, 1, "orange")  # outer spaced layer



# --- Add Kathakali image in the center ---
turtle.register_shape("kathakali.gif")  # register the image as a shape
img_turtle = turtle.Turtle()
img_turtle.hideturtle()
img_turtle.penup()
img_turtle.goto(0, 0)  # center of the Pookalam
img_turtle.shape("kathakali.gif")
img_turtle.stamp()  # place the image once





turtle.done()
