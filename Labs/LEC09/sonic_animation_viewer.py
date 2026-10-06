from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')

while True:
    clear_canvas()

    # 첫 번째 Sonic 프레임
    sonic.clip_draw(
        1, 448,       # 이미지에서 프레임의 왼쪽 아래 좌표
        29, 38,       # 프레임의 가로, 세로 크기
        600, 300      # 화면에 출력할 위치
    )

    update_canvas()

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()