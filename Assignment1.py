import math
import turtle

X_MAX=200
Y_MAX=200
def rectangle_will_fit(x,y,length,height): """Function to check if rectangle fits in border"""
    if y+height <Y_MAX:
        return True
    if x+length>X_MAX:
        return True
    else:
        return False

def circle_will_fit(x,y,length): """Function to check if circle fits in border"""

    if x+length>X_MAX:
        return True
    else:
        return False

def triangle_will_fit(x,y,length): """Function to check if triangle fits in border"""

    if x+length>X_MAX:
        return True
    else:
        return False
def grid(): """Function to draw a grid/border"""
    turtle.penup()
    turtle.goto(-200,200)
    turtle.pendown()
    for i in range(4):
        turtle.forward(450)
        turtle.right(90)

def rectangle(length,height): """Function for drawing a rectangle"""
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
def triangle(length):
    for i in range(2):
        turtle.forward(length)
        turtle.left(120) """Function for drawing a triangle"""


def draw_shape(shape,color_code='red',x=0,y=0,length=100,height=0): """Main draw shape function"""
    global x1,y1,c1
    x1,y1,c1=x,y,color_code
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color_code)
    if shape=='r':
        rectangle(length,height)
        P = 2 * (length + height)
        print("The Perimeter of rectangle:",P)
        return P
    elif shape=='c':
        turtle.circle(length)
        P = math.pi * length * 2
        print("The Perimeter of circle:",P)
        return P
    elif shape=='t':
        triangle(length)
        P= length+length+length
        print("The Perimeter is triangle:",P)
        return P
    elif shape=='all':
        draw_shape("r", color_code, x, y, length,height)
        draw_shape("c", "blue", -90, -200, length)
        draw_shape("t", "green", -150,80, length)

    else:
        print("Invalid Input")
        print("Perimeter is zero")
    turtle.end_fill()



def main(): """Main Function that can be called to draw all shapes as specified in Q6"""
    turtle.speed(5)
    grid()
    draw_shape('all','red',50,0,80,50)
    turtle.done()

turtle.speed(8)
grid()






