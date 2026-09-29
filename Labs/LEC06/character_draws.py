# 실습 과제 진행
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')

def draw_circle():
    print("circle")
    for deg in range(0, 360, 5):
        rad = math.radians(deg)
        x = 400 + 200 * math.cos(rad)
        y = 300 + 200 * math.sin(rad)

        clear_canvas()
        
        character.draw(x, y)
        update_canvas()
        delay(0.1)
    pass


def draw_rectangle():
    print("rectangle")
    pass

def draw_triangle():
    print("triangle")
    pass


while True :
    draw_circle()
    draw_rectangle()
    draw_triangle()
    pass


close_canvas()