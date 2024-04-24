# начальные настройки
from turtle import *
tracer(0) # говорит программу не отслеживать путь черепашки
screensize(8000, 8000) # задаём размер окна, чтобы перемещаться по рисунку
left(90) # поворачиваемся на 90 градусов (по условию)
m = 25 # задаём масштаб
down() # опускаем хвост

# программа из условия ->
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

# строим сетку по которой будем считать клеточки ->
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(m * x, m * y)
        dot(5, 'red')
done() # или exitonclick()
