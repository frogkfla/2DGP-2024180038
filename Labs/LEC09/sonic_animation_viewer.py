from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')

while True:
    clear_canvas()

    # 첫 번째 Sonic 프레임을 4배 크기로 출력
    sonic.clip_draw(
        1, 448,
        29, 38,
        600, 300,
        29 * 4, 38 * 4
    )

    update_canvas()

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()