import turtle as t

t.shape("turtle")
t.pensize(10)

t.penup()
t.goto(-100,0)
t.pendown()
t.color("blue")
t.circle(50)

t.penup()
t.goto(0, 0)
t.pendown()
t.color("black")
t.circle(50)

t.penup()
t.goto(100, 0)
t.pendown()
t.color("red")
t.circle(50)

t.penup()
t.goto(-50, -50)
t.pendown()
t.color("yellow")
t.circle(50)

t.penup()
t.goto(50, -50)
t.pendown()
t.color("green")
t.circle(50)

t.color("black")
t.penup()
t.goto(0, 200)
t.write("오륜기", font=('Arial', 18, 'normal'))
