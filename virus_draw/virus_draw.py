import turtle
s=turtle.Turtle()
a=turtle.Screen()
a.bgcolor('black')
s.pencolor('red')
a=0
b=0
s.speed(0)
s.pu()
s.goto(0,200)
s.pd()
while True:
    s.fd(a)
    s.rt(b)
    a+=3
    b+=1
    if b==205:
        break
    s.hideturtle()

turtle.done()