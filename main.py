
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10 * i, 0) for i in range(5, 0, -1)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction unless it's the opposite direction."
    if (x, y) != (-aim.x, -aim.y):  # Prevent moving backward
        aim.x = x
        aim.y = y

def inside(head):
    "Make the snake wrap around edges."
    if head.x > 190:
        head.x = -200
    elif head.x < -200:
        head.x = 190
    if head.y > 190:
        head.y = -200
    elif head.y < -200:
        head.y = 190
    return True

    # "Return True if head inside boundaries."
    # return -200 < head.x < 190 and -200 < head.y < 190

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
        print('Snake:', len(snake)-5)
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'blue')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 200)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()   