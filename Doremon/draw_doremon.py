from turtle import *


def Position(x, y):

    penup()
    goto(x, y)
    pendown()


def eyes():

    fillcolor("#ffffff")
    begin_fill()

    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()


def mustaches():
    Position(-32, 135)
    seth(165)
    fd(60)

    Position(-32, 125)
    seth(180)
    fd(60)

    Position(-32, 115)
    seth(193)
    fd(60)

    Position(37, 135)
    seth(15)
    fd(60)

    Position(37, 125)
    seth(0)
    fd(60)

    Position(37, 115)
    seth(-13)
    fd(60)


def smile():
    Position(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)
    

def red_ribbon ():

    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


def nose():
    Position(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


def nose_shine():
    Position(9, 166)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(0.1)
    end_fill()


def black_eyes():
    seth(0)
    Position(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    Position(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    Position(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    Position(0, 0)


def face():
    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    # print(pos())
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    Position(63.56, 218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)


def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()


def left_arm():
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)
    fillcolor('#00a0de')
    begin_fill()


def left_body_curve():
    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)


def left_leg():
    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)


def right_leg():
    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)


def right_body_side__arm():
    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()


def right_feet():
    Position(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-18, 180)
    fd(90)
    circle(-18, 180)
    fd(10)
    end_fill()


def left_feet():
    Position(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(18, 180)
    fd(90)
    circle(18, 180)
    fd(10)
    end_fill()


def left_hand():
    Position(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()


def chest():
    Position(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill() 


def poket():
    Position(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)


def bell():
    Position(-103.42, 15.09)

    fd(90)
    seth(70)
    fillcolor('#ffd200')
    begin_fill()
    circle(-20)
    end_fill()
    
    seth(170)
    fillcolor('#ffd200')
    
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180 - 10)
    circle(100, 22)
    end_fill()

    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    Position(0, -150)

def Doraemon():
    head()
    red_ribbon ()
    face()
    nose()
    #nose_shine()
    smile()
    mustaches()
    black_eyes()
    Position(0, 0)
    left_arm()
    left_body_curve()
    left_leg()

    #bottom curve
    seth(100)
    circle(-1000, 9)

    right_leg()
    right_body_side__arm()
    right_feet()
    left_feet()
    left_hand()
    chest()
    poket()
    bell()


if __name__ == '__main__':
    screensize(500, 300, "#f0f0f0")
    pensize(3)
    speed(10)
    Doraemon()
    Position(100, -300)
    mainloop()