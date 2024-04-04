from turtle import *
tracer(0)
screensize(8000, 8000)
left(90)
m = 25

up()
for i in range(10):
    rt(120)
    fd(m*10)
down()
for i in range(7):
    fd(m*15)
    rt(90)
for i in range(5):
    rt(60)
    fd(m*20)
    rt(30)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(m * x, m * y)
        dot(5, 'red')
done()
