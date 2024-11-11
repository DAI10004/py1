import turtle
import random

# 设置画布
screen = turtle.Screen()
screen.bgcolor("white")

# 创建画笔
pen = turtle.Turtle()
pen.speed(0)  # 设置画笔速度最快


# 定义绘制分形树的函数
def tree(length, level):
    if level > 0:
        colors = ["green", "red", "yellow","blue"]
        pen.color(random.choice(colors))  # 随机选择一种颜色

        # 绘制当前分支
        pen.forward(length)
        pen.right(20)

        # 递归绘制右子树
        tree(length - 15, level - 1)

        pen.left(40)

        # 递归绘制左子树
        tree(length - 15, level - 1)

        pen.right(20)
        pen.backward(length)


# 设置初始位置
pen.penup()
pen.goto(0, -200)
pen.pendown()
pen.setheading(90)  # 朝上

# 开始绘制分形树
tree(100, 7)

# 结束绘图
pen.hideturtle()
turtle.done()