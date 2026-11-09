from pico2d import *
import game_framework
import game_world
from boy import Boy
from grass import Grass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode
            game_framework.push_mode(pause_mode)
        else:
            boy.handle_event(event)


def init():
    global boy

    grass = Grass()
    game_world.add_oject(grass, 0)
    boy = Boy()
    game_world.add_oject(boy, 1)


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


render = draw


def pause():
    boy.clear_movement_input()


def resume():
    pass


def finish():
    game_world.clear()
