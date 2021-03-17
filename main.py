from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors=['black', 'blue', 'magenta', 'yellow', 'cyan']
color=random.choice(colors)
colors.remove(color)
color2=random.choice(colors)
    
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# La función se llama changeFood
# parametro de entrada: x (int), y (int)
# parametro de salida: N/A (no regresa valores)
# Descripcion: cambia la posición en x y y de "food"
def changeFood(x, y):
    food.x = x
    food.y = y

# La función se llama moveFood
# parametro de entrada: N/A (no hay parametros de entradas)
# parametro de salida: N/A (no regresa valores)
# Descripcion: calcula la nueva posición de "food" aleatoriamente y manda llamar la funcion de changeFood para actualizar la posición 
def moveFood():
    num = randrange(0,4)
    if num == 0:
        if inside(food):
            changeFood(food.x, food.y + 10)
    elif num == 1:
        if inside(food):
            changeFood(food.x + 10, food.y)
    elif num == 2:
        if inside(food):
            changeFood(food.x, food.y - 10)
    else:
        if inside(food):
            changeFood(food.x - 10, food.y)
    ontimer(moveFood, 1000)

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    
    for body in snake:
        square(body.x, body.y, 9, color)

    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
moveFood()
move()
done()