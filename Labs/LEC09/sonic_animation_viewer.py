from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')

# 첫 번째 애니메이션
frames1 = [
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

# 전체 애니메이션
animations = [
    frames1
]

animation = 0
frame = 0
repeat_count = 0

last_frame_time = get_time()
frame_interval = 0.1

is_paused = False
pause_start_time = 0.0

while True:
    clear_canvas()

    # 현재 동작의 프레임 목록
    current_frames = animations[animation]

    # 현재 프레임
    x, y, width, height = current_frames[frame]

    sonic.clip_draw(
        x, y,
        width, height,
        600, 300,
        width * 4, height * 4
    )

    update_canvas()

    current_time = get_time()

    if not is_paused:
        if current_time - last_frame_time >= frame_interval:
            frame += 1

            if frame >= len(current_frames):
                repeat_count += 1

                if repeat_count >= 5:
                    frame = len(current_frames) - 1
                    is_paused = True
                    pause_start_time = current_time
                else:
                    frame = 0

            last_frame_time = current_time

    else:
        if current_time - pause_start_time >= 1.0:
            animation = (animation + 1) % len(animations)

            frame = 0
            repeat_count = 0
            is_paused = False
            last_frame_time = current_time

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()