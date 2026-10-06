from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')

# 첫 번째 동작에 사용할 프레임 데이터
# (x, y, width, height)
frames = [
    (1, 448, 29, 38)
]

while True:
    clear_canvas()

    # 현재 프레임 데이터 가져오기
    x, y, width, height = frames[0]

    # 원본 크기의 4배로 출력
    sonic.clip_draw(
        x, y,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()