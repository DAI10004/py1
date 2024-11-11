import turtle as t

# ----驱动数据
data = {
    'A': [(-500, -300)],
    'table': [(350, -300)],
    'rectangles': [
        (350, -350, 50, 800, 'red'),
        (350, 100, 50, 800, 'red'),
        (400, -300, 400, 50, 'red'),
        (-450, -300, 400, 50, 'red')
    ],
    'lines': [(-280, -300, 400), (-280, -40, 60)],
    'circles': [
        (-280, -50, 'green'),
        (-280, -170, 'yellow'),
        (-280, -110, 'orange'),
        (-340, -110, 'white'),
        (-50, -110, 'blue'),
        (100, -110, 'pink'),
        (280, -110, 'black'),
        (150, -110, 'red'),
        (195, -110, 'red'),
        (240, -110, 'red'),
        (170, -130, 'red'),
        (215, -130, 'red'),
        (195, -150, 'red'),
        (240, -150, 'red'),
        (215, -170, 'red'),
        (240, -190, 'red'),
        (170, -90, 'red'),
        (215, -90, 'red'),
        (195, -70, 'red'),
        (240, -70, 'red'),
        (215, -50, 'red'),
        (240, -30, 'red'),
        (-450, 90, 'gray'),
        (350, 90, 'gray'),
        (-455, -310, 'gray'),
        (350, -310, 'gray')
    ],
    'half_circles': [(-50, 97), (-50, -298)]
}

# 移动函数
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# 大底面，圆角
def A(x, y):
    t.speed(0)
    t.pensize(2)
    move(x, y)
    t.color("black", "dark gray")
    t.begin_fill()
    t.seth(90)
    t.forward(400)
    t.circle(-50, 90)
    t.forward(800)
    t.circle(-50, 90)
    t.forward(400)
    t.circle(-50, 90)
    t.forward(800)
    t.circle(-50, 90)
    t.end_fill()

# 球桌函数
def draw_table(x, y):
    t.speed(0)
    t.pensize(5)
    t.color("green", "dark green")
    move(x, y)
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.left(90)
        t.forward(800)
        t.left(90)
    t.end_fill()

# 画圆函数
def draw_circle(x, y, color):
    move(x, y)
    t.speed(0)
    t.color(color)
    t.begin_fill()
    t.fillcolor(color)
    t.circle(10)
    t.end_fill()

# 画矩形函数
def draw_rectangle(x, y, length, width, color):
    move(x, y)
    t.speed(0)
    t.color("red", color)
    t.begin_fill()
    for _ in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.end_fill()

# 画半圆函数
def draw_half_circle1(x, y):
    t.speed(0)
    move(x, y)
    t.seth(90)
    t.color("gray", 'dark gray')
    t.begin_fill()
    t.circle(11, 180)
    t.end_fill()

def draw_half_circle2(x, y):
    t.speed(0)
    move(x, y)
    t.seth(-90)
    t.color("gray", 'dark gray')
    t.begin_fill()
    t.circle(11, 180)
    t.end_fill()

# ----绘制函数
for x, y in data['A']:
    A(x, y)
for x, y in data['table']:
    draw_table(x, y)
for x, y, length, width, color in data['rectangles']:
    draw_rectangle(x, y, length, width, color)
for x, y, length in data['lines']:
    move(x, y)
    t.seth(90)
    t.color('black')
    t.fd(length)


for x, y, color in data['circles']:
    draw_circle(x, y, color)
for x, y in data['half_circles']:
    if y == 97:
        draw_half_circle1(x, y)
    else:
        draw_half_circle2(x, y)

t.hideturtle()
t.done()