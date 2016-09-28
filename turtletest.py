# -*- coding: cp936 -*-

'''
(1)运动命令:
forward(degree)#向前移动距离degree代表距离
backward(degree)#向后移动距离degree代表距离
right(degree)#向右移动多少度
left(degree)#向左移动多少度
goto(x,y)#将画笔移动到坐标为x,y的位置
stamp()#复制当前图形
speed(speed)#画笔绘制的速度范围[0,10]整数 

(2)画笔控制命令:

down() #移动时绘制图形,缺省时也为绘制
up() #移动时不绘制图形
pensize(width) #绘制图形时的宽度
color(colorstring) #绘制图形时的颜色
fillcolor(colorstring) #绘制图形的填充颜色 fill(Ture) fill(false)
'''
import turtle
import time
turtle.color('purple')
turtle.pensize(5)
turtle.speed(1)
turtle.goto(0,0)
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

for i in range(6):
    turtle.forward(100)
    turtle.right(144)


turtle.forward(100)
turtle.goto(-150,-120)
turtle.color('black')
turtle.write('Done')
time.sleep(3)
