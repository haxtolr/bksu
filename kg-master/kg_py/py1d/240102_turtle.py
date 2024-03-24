import turtle as t
t.speed(0)
t.pensize(5)
t.color("red")
t.shape("turtle")

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

#위치 이동
t.goto(0,100)

#삼각형
t.color("blue")
t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.end_fill()


my_t = t.Turtle() #새로운 터틀 생성
my_t.penup()
my_t.goto(200, 0)

my_t.pendown()
my_t.forward(100)
my_t.left(90)
my_t.forward(100)
my_t.left(90)
my_t.forward(100)
my_t.left(90)
my_t.clear()
my_t.write("dkssud",font=('Arial', 18, 'normal'))
