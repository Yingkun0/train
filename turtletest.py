# -*- coding: cp936 -*-

'''
(1)�˶�����:
forward(degree)#��ǰ�ƶ�����degree�������
backward(degree)#����ƶ�����degree�������
right(degree)#�����ƶ����ٶ�
left(degree)#�����ƶ����ٶ�
goto(x,y)#�������ƶ�������Ϊx,y��λ��
stamp()#���Ƶ�ǰͼ��
speed(speed)#���ʻ��Ƶ��ٶȷ�Χ[0,10]���� 

(2)���ʿ�������:

down() #�ƶ�ʱ����ͼ��,ȱʡʱҲΪ����
up() #�ƶ�ʱ������ͼ��
pensize(width) #����ͼ��ʱ�Ŀ��
color(colorstring) #����ͼ��ʱ����ɫ
fillcolor(colorstring) #����ͼ�ε������ɫ fill(Ture) fill(false)
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
