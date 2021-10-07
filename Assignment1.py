import math
import turtle

turtle.speed(8)
X_MAX=200
Y_MAX=200
def rectangle_will_fit(x,y,length,height):

    if (y+height) <Y_MAX:
        return True
    if (x+length)>X_MAX:
        return True
    else:
        return False

def circle_will_fit(x,y,length):
    if x+length>X_MAX:             #Function to check if circle fits in border
        return True
    else:
        return False

def triangle_will_fit(x,y,length):
    if x+length>X_MAX:             #Function to check if triangle fits in border
        return True
    else:
        return False
def grid():
    turtle.penup()
    turtle.goto(-200,200)          #Function to draw a grid/border
    turtle.pendown()
    for i in range(4):
        turtle.forward(450)
        turtle.right(90)

def rectangle(length,height):
    for i in range(2):
        turtle.forward(length)        #Function for drawing a rectangle
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
def triangle(length):
    for i in range(2):
        turtle.forward(length)        #Function for drawing a triangle
        turtle.left(120)


def draw_shape(shape,color_code='red',x=0,y=0,length=100,height=0): #Main draw shape function
    global x1,y1,c1
    x1,y1,c1=x,y,color_code
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color_code)
    if shape=='r':
        rectangle(length,height)
        turtle.end_fill()
        P = 2 * (length + height)
        print("The Perimeter of rectangle:",P)
        return P
    elif shape=='c':
        turtle.circle(length)
        turtle.end_fill()
        P = math.pi * length * 2
        print("The Perimeter of circle:",P)
        return P
    elif shape=='t':
        triangle(length)
        turtle.end_fill()
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




def main(): #Main Function that can be called to draw all shapes as specified in Q6
    turtle.speed(5)
    grid()
    draw_shape('all','red',50,0,80,50)
    turtle.done()







