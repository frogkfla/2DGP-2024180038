from pico2d import *

open_canvas(1200, 600)

while True:
    clear_canvas()

    update_canvas()

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()