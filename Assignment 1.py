import pixart
import turtle

def test_init():
    pixart.innit()
    s=turtle.speed()
    assert(s==0)

    x=turtle.xcor();
    assert(x==-200)
    