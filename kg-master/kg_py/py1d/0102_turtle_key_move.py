from turtle import * #터틀의 모든 것 import

screen = Screen()
t = Turtle()
i = 1

def forward_move():
    t.fd(10)

def backward_move():
    t.bk(10)

def left_move():
    t.left(10)

def right_move():
    t.right(10)

def s_clear():
    t.clear()

def c_goto():
    t.pu()
    t.home()
    t.pd()

def ft_up():
    global i
    i += 1
    t.pensize(i)


def ft_down():
    global i
    i -= 1
    t.pensize(i)


screen.title("my screen")
screen.listen()
screen.onkeypress(forward_move, 'w')
screen.onkeypress(backward_move, 's')
screen.onkeypress(left_move, 'a')
screen.onkeypress(right_move, 'd')
screen.onkeypress(s_clear, 'space')
screen.onkeypress(c_goto, 'c')
screen.onkeypress(t.undo, 'u')
screen.onkeypress(ft_up, '+')
screen.onkeypress(ft_down, '-')
