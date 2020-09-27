import turtle
pen = turtle.Turtle()
wn = turtle.Screen() 
wn.bgcolor("blue")
pen.speed(10)

#STOMACH

pen.pensize(8)
pen.penup()
pen.setposition(0,-200)
pen.down()
pen.color("white")
pen.begin_fill()
pen.circle(80)
pen.end_fill()

#FACE

pen.pensize(8)
pen.penup()
pen.setposition(0,-50)
pen.pendown()
pen.begin_fill()
pen.circle(50)
pen.end_fill()

#LEFT EYE

pen.pensize(8)
pen.penup()
pen.setposition(-20,20)
pen.pendown()
pen.color("black")
pen.circle(5)
pen.end_fill()

#RIGHT EYE

pen.pensize(8)
pen.penup()
pen.setposition(20,20)
pen.pendown()
pen.color("black")
pen.circle(5)
pen.end_fill()

#NOSE

pen.pensize(5)
pen.penup()
pen.setposition(-2,0)
pen.pendown()
pen.begin_fill()
pen.fd(10)
pen.lt(135)
pen.fd(10)
pen.lt(100)
pen.fd(9)
pen.lt(125)
pen.end_fill()

#SMILE

pen.pensize(5)
pen.penup()
pen.goto(-18,-16)
pen.begin_fill()
pen.pendown()
pen.rt(90)
pen.circle(20, 180)
pen.left(90)
pen.forward(40)
pen.lt(180)
pen.end_fill()

#SCARF

pen.pensize(5)
pen.color("yellow")
pen.penup()
pen.goto(-35,-50)
pen.pendown()
pen.begin_fill()
pen.fd(70)
pen.lt(90)
pen.fd(5)
pen.lt(90)
pen.fd(70)
pen.lt(90)
pen.fd(20)
pen.lt(90)
pen.fd(5)
pen.lt(90)
pen.fd(15)
pen.end_fill()

#LEFT HAND

pen.pensize(5)
pen.penup()
pen.setposition(-78,-90)
pen.color("brown")
pen.pendown()
pen.begin_fill()
pen.lt(45)
pen.fd(75)
pen.lt(90)
pen.fd(5)
pen.lt(90)
pen.fd(75)
pen.lt(90)
pen.end_fill()
pen.fd(5)

#RIGHT HAND

pen.pensize(5)
pen.penup()
pen.setposition(78,-90)
pen.color("brown")
pen.pendown()
pen.begin_fill()
pen.fd(75)
pen.lt(90)
pen.fd(5)
pen.lt(90)
pen.fd(75)
pen.lt(90)
pen.end_fill()
pen.fd(5)

#HAT

pen.pensize(5)
pen.color("yellow")
pen.penup()
pen.goto(-35,50)
pen.pendown()
pen.begin_fill()
pen.lt(45)
pen.fd(70)
pen.lt(135)
pen.fd(60)
pen.lt(100)
pen.fd(51)
pen.end_fill()
pen.hideturtle()

wn.exitonclick()