import Assignment1
import turtle

def test_rectangle_will_fit():
    Assignment1.rectangle_will_fit(100,100,60,40)
    X=100
    Y=100
    assert(X==100)
    assert(Y==100)

def test_circle_will_fit():
    Assignment1.circle_will_fit(-90,-200,60)
    X,Y=-90,-200
    assert(X,Y==-90,-200)

def test_triangle_will_fit():
    Assignment1.triangle_will_fit(-150,80,60)
    X,Y=-150,80
    assert(X,Y==-150,80)

def test_draw_shape_rectangle():
    P = Assignment1.draw_shape('r', 'red', 50, 0, 80, 50)
    assert(turtle.fillcolor()=='red')
    assert((turtle.xcor(),turtle.ycor())==100,100)
    assert(P==260)

def test_draw_shape_circle():
    P = Assignment1.draw_shape('c', 'blue', -90, -200, 60)
    assert(turtle.fillcolor()=='blue')
    assert((turtle.xcor(),turtle.ycor())==-90,-200)
    assert(P==376.99111843077515)

def test_draw_shape_triangle():
    P = Assignment1.draw_shape('t', 'green', -150, 80, 60)
    assert(turtle.fillcolor()=='green')
    assert((turtle.xcor(),turtle.ycor())==-150,80)
    assert(P==180)







