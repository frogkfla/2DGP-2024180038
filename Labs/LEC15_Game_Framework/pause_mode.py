from pico2d import *

import game_framework
import game_world


def init():
    pass


def finish():
    pass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()


def update():
    # 게임 월드를 갱신하지 않아 캐릭터와 공이 정지된 상태를 유지한다.
    pass


def render():
    clear_canvas()
    game_world.render()
    update_canvas()
