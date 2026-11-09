from pico2d import *

import game_framework
import game_world
from ball import select_item


menu_image = None


def init():
    global menu_image
    menu_image = load_image('item_select.png')


def finish():
    global menu_image
    menu_image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                select_item(None)
                game_framework.pop_mode()
            elif event.key == SDLK_1:
                select_item(1)
                game_framework.pop_mode()
            elif event.key == SDLK_2:
                select_item(2)
                game_framework.pop_mode()
            elif event.key in (SDLK_f, SDLK_ESCAPE):
                game_framework.pop_mode()


def update():
    # 아이템 선택 중에는 플레이 모드의 게임 객체를 갱신하지 않는다.
    pass


def render():
    clear_canvas()
    game_world.render()
    menu_image.draw(400, 350)
    update_canvas()
