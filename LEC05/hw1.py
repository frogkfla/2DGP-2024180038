# 실습과제1
from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')

x=400
y=300

while True:
    while x < 600:
        clear_canvas()
        character.draw(x,y)
        update_canvas()
        x += 2
        delay(0.01)

    while y < 500:
        clear_canvas()
        character.draw(x,y)
        update_canvas()
        delay(0.01)
        y += 2

    while x > 400 :
        clear_canvas()
        character.draw(x,y)
        update_canvas()
        x -= 2
        delay(0.01)

    while y > 300:
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        y -= 2
        delay(0.01)


close_canvas()