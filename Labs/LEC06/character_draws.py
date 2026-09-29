# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

def draw_circle():
    print("circle")

    center_x = 400
    center_y = 300
    radius = 200

    for deg in range(0, 360, 5):
        rad = math.radians(deg)
        
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)

        draw_character(x, y)
    pass


def draw_top():
    print("top")

    stat_x = 50
    end_x = 750
    top_y = 550

    for x in range(stat_x, end_x, 5):
        draw_character(x, top_y)


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)   


def draw_right():
    right_x = 750
    stat_y = 550
    end_y = 50

    for y in range(stat_y, end_y, -5):
        draw_character(right_x, y)
    pass


def draw_bottom():
    stat_x = 750
    end_x = 50
    bottom_y = 50

    for x in range(stat_x, end_x, -5):
        draw_character(x, bottom_y)
    pass


def draw_left():
    left_x = 50
    stat_y = 50
    end_y = 550

    for y in range(stat_y, end_y, 5):
        draw_character(left_x, y)
    pass


def draw_rectangle():
    print("rectangle")
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

def draw_line(x0, y0, x1, y1):
    n = 100
    for step in range(n + 1):
        t = step / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        draw_character(x, y)

    
def draw_triangle_bottom():
    print("triangle - bottom (A -> B)")

    start_x = 100
    start_y = 100
    end_x = 700
    end_y = 100

    draw_line(start_x, start_y, end_x, end_y)


def draw_triangle_right_up():
    print("triangle - right up (B -> C)")
    draw_line(700, 100, 400, 500)

def draw_triangle_left_down():
    print("triangle - left down (C -> A)")
    draw_line(400, 500, 100, 100)

def draw_triangle():
    print("triangle")
    draw_triangle_bottom()
    draw_triangle_right_up()
    draw_triangle_left_down()
    pass

while True :
    draw_circle()
    draw_rectangle()
    draw_triangle()

    pass

close_canvas()