import turtle as t
t.title('yin and yang')
raj=t.Turtle()
raj.shape('turtle')
raj.penup()
raj.goto(0,250)
raj.pendown()
raj.begin_fill()
raj.circle(-250,180)
raj.end_fill()
raj.circle(-250,180)
raj.begin_fill()
raj.right(180)
raj.circle(125,180)
raj.end_fill()
raj.color('black','white')
raj.begin_fill()
raj.right(180)
raj.circle(125,-180)
raj.end_fill()
raj.penup()
raj.left(90)
raj.forward(125)
raj.forward(30)
raj.pendown()
raj.color('black','black')
raj.begin_fill()
raj.left(90)
raj.circle(30)
raj.end_fill()
raj.penup()
raj.right(90)
raj.forward(250)
raj.pendown()
raj.color('black','white')
raj.begin_fill()
raj.left(90)
raj.circle(30,-360)
raj.end_fill()
raj.hideturtle()
t.done()
