from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')

# 첫 번째 애니메이션의 프레임
# (x, y, width, height)
frames = [
    (0,   443, 30, 43),
    (30,  443, 28, 43),
    (58,  443, 30, 43),
    (88,  443, 30, 43),
    (118, 443, 30, 43),
    (148, 443, 32, 43),
    (180, 443, 30, 43),
    (210, 443, 30, 43),
    (240, 443, 30, 43),
    (270, 443, 30, 43),
    (300, 443, 32, 43)
]

frame = 0

# 프레임 변경에 사용할 시간
last_frame_time = get_time()
frame_interval = 0.1

while True:
    clear_canvas()

    # 현재 프레임 정보 가져오기
    x, y, width, height = frames[frame]

    # 현재 프레임을 원본의 4배 크기로 출력
    sonic.clip_draw(
        x, y,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()

    # 현재 시간 확인
    current_time = get_time()

    # 0.1초가 지났을 때만 다음 프레임으로 변경
    if current_time - last_frame_time >= frame_interval:
        frame = (frame + 1) % len(frames)
        last_frame_time = current_time

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()