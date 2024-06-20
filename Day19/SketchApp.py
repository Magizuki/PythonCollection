import turtle as turtle_module

tim = turtle_module.Turtle()
tim.pendown()
screen = turtle_module.Screen()

def forward():
    tim.forward(50)

def backward():
    tim.backward(50)

angle = 0
def clockwise():
    global angle 
    angle -= 10
    if angle < 0:
        angle = 360
    tim.setheading(angle)

def counter_clockwise():
    global angle 
    angle += 10
    if angle > 360:
        angle = 0
    tim.setheading(angle)

def clear_drawing():
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()


