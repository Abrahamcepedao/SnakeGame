# Codigo de Juego de la Vibora
# Proposito: Continuar con una aplicación que implica una inteligencia muy sencilla
# conocida por la mayoría pero que requiere una actualización para manejar una funcionalidad adicional.
# se agregan las funcionalidades de: cambio de color de serpiente y comida; movimiento de la comida
# Autores: Monserrat Da Costa Gomez y Abraham Cepeda
from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# Este codigo agregado permite que se seleccione un color al azar de la siguiente lista para darle un color a la serpiente
# y elige al azar un color diferente para la comida
colors=['black', 'blue', 'magenta', 'yellow', 'cyan']
color=random.choice(colors)
colors.remove(color)
color2=random.choice(colors)

# La función se llama change
# parametro de entrada: x (int), y (int)
# parametro de salida: N/A (no regresa valores)
# Descripcion: cambia la posición en x y y de "snake"
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

# La función se llama inside
# parametro de entrada: head (la cabeza de la serpiente)
# parametro de salida: TRUE/FALSE
# Descripcion: revisa si la cabeza se encuentra dentro del juego
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

# La función se llama move
# parametro de entrada: el vector aim
# parametro de salida: si se sale del juego, cambia de color a rojo, o aumenta el tamaño de la serpiente si come
# Descripcion: cambia la posición en x y y de "food"
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
    
    # especificaciones del cuerpo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, color)

    # especificaciones de la comida
    square(food.x, food.y, 9, color2)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# la funcion 'onkey' tiene como parametros una funcion sin argumentos y una tecla, se mueve 19 pixeles segun las indicaciones
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
moveFood()
move()
done()