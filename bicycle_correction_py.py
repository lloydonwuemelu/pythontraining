import turtle
# turtle.delay(1000)

# Draw the inner circle on the right side
turtle.penup()
turtle.setposition(100,-20)
turtle.setheading(90)
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()

#Draw the inner circle on the left side
turtle.penup()
turtle.setposition(-70,-20)
turtle.setheading(90)
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.pendown()

#Draw the bigger  Right Circle
turtle.pensize(3)
turtle.penup()
turtle.setposition(135,-20)
turtle.pendown()
turtle.circle(50)

#Draw the bigger LEFT CIRCLE
turtle.pensize(3)
turtle.penup()
turtle.setposition(-35,-20)
turtle.pendown()
turtle.circle(50)

#Draw left triangle
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(80)
turtle.left(110)
turtle.forward(100)
turtle.left(130)
turtle.forward(100)
turtle.right(180)
turtle.forward(100)
turtle.right(60)

#Draw right triangle
turtle.forward(90)
turtle.right(120)
turtle.forward(110)
turtle.left(180)
turtle.forward(110)
turtle.right(130)
turtle.forward(90)

turtle.left(180)
turtle.forward(110)
turtle.right(110)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(30)
turtle.left(180)

turtle.penup()
turtle.forward(80)
turtle.pendown()

#Backseat
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(40)
turtle.left(180)
turtle.forward(20)
turtle.left(112)
turtle.forward(30)

turtle.penup()
turtle.circle(90)
turtle.pendown()


















