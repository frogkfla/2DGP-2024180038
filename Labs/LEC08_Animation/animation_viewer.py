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

row2 = [
(5,   362, 41, 39),
(67,  362, 40, 39),
(130, 362, 36, 39),
(188, 362, 39, 39),
(247, 362, 42, 39),
(308, 362, 44, 39),
(367, 362, 43, 39),
(431, 362, 37, 39),
(485, 362, 33, 39),
(535, 362, 36, 39)
]
