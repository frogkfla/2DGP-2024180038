from pico2d import *

open_canvas()

ground = load_image('ground.png')
character = load_image('kirby.png')

def draw_frame(frame_data):
    clear_canvas()

    ground.draw(400, 45, 800, 90)

    left, bottom, width, height = frame_data

    character.clip_draw(
        left, bottom,
        width, height,
        400, 120,
        width * 2.5, height * 2.5
    )
    
    update_canvas()