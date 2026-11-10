# 실습과제2

from pico2d import *
from math import sin, cos, pi

open_canvas(800, 600)

character = load_image('character.png')

angle = 0

while True:

    x = 400 + 150 * cos(angle)
    y = 300 + 150 * sin(angle)

    clear_canvas()
    character.draw(x, y)
    update_canvas()

    angle += 0.05

    if angle >= 2 * pi:
        angle = 0

    delay(0.01)

close_canvas()