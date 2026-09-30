from pico2d import *

open_canvas()

ground = load_image('ground.png')
character = load_image('kirby.png')

frame = 0

for x in range(50, 750, 5):
    clear_canvas()

    ground.draw(400, 35, 800, 70)

    update_canvas()
