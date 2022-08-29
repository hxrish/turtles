import turtle 
wn = turtle.Screen()
a = turtle.Turtle()
a.shape('turtle')
a.color('blue')
for i in range(12):
    a.penup()
    a.forward(100)
    a.pendown()
    a.forward(20)
    a.penup()
    a.forward(20)
    a.stamp()
    a.forward(-140)
    a.pendown()
    a.left(30)

wn.exitonclick()