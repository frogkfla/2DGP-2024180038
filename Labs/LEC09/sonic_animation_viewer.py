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

# 두 번째 애니메이션
frames2 = [
    (8,   409, 25, 36),
    (37,  409, 25, 36),
    (65,  407, 31, 38),
    (97,  409, 37, 36),
    (136, 411, 31, 34),
    (170, 409, 32, 37),
    (206, 409, 25, 37),
    (238, 408, 24, 37),
    (263, 408, 30, 37),
    (295, 409, 35, 36),
    (334, 410, 32, 35),
    (370, 408, 29, 38)
]

# 세 번째 애니메이션
frames3 = [
    (2,   362, 32, 39),
    (40,  363, 33, 38),
    (90,  363, 33, 37),
    (130, 363, 34, 41),
    (181, 362, 34, 41),
    (228, 364, 32, 39)
]

# 네 번째 애니메이션
frames4 = [
    (1,   326, 29, 39),
    (35,  327, 29, 38),
    (67,  327, 30, 29),
    (99,  327, 30, 38),
    (131, 327, 29, 38),
    (162, 326, 29, 39),
    (193, 326, 30, 39),
    (230, 326, 31, 39),
    (268, 325, 30, 30)
]

# 다섯 번째 애니메이션
frames5 = [
    (1,   292, 30, 27),
    (36,  292, 29, 27),
    (70,  292, 29, 27),
    (105, 292, 29, 27),
    (139, 292, 29, 27),
    (174, 292, 29, 27)
]

# 여섯 번째 애니메이션
frames6 = [
    (1,   252, 29, 35),
    (36,  252, 30, 34),
    (75,  251, 30, 35),
    (111, 252, 31, 35),
    (152, 251, 27, 35),
    (186, 252, 31, 35)
]

# 일곱 번째 애니메이션
frames7 = [
    (0,   208, 30, 34),
    (36,  208, 30, 34),
    (72,  208, 39, 31),
    (123, 208, 39, 32),
    (172, 208, 39, 31),
    (218, 208, 38, 32)
]

# 여덟 번째 애니메이션
frames8 = [
    (0,   164, 30, 38),
    (35,  164, 31, 38),
    (72,  164, 30, 38),
    (108, 164, 31, 38),
    (145, 164, 30, 38),
    (181, 164, 31, 38),
    (218, 164, 30, 38),
    (254, 164, 31, 38)
]

# 아홉 번째 애니메이션
frames9 = [
    (1,   109, 27, 37),
    (31,  111, 31, 35),
    (64,  111, 31, 35),
    (99,  111, 32, 37),
    (136, 111, 32, 35),
    (176, 111, 33, 35),
    (217, 111, 33, 35),
    (254, 112, 33, 35)
]

# 열 번째 애니메이션
frames10 = [
    (6,   57, 34, 39),
    (49,  57, 34, 42),
    (96,  60, 23, 38),
    (125, 60, 23, 38)
]


# 전체 애니메이션
animations = [
    frames1,
    frames2,
    frames3,
    frames4,
    frames5,
    frames6,
    frames7,
    frames8,
    frames9,
    frames10
]

# 각 애니메이션의 이동 여부
moving_animations = [
    True,   # 1번
    True,   # 2번
    True,   # 3번
    True,   # 4번
    True,   # 5번
    True,   # 6번
    True,   # 7번
    True,   # 8번
    False,  # 9번
    False   # 10번
]

# 전체 프레임 수 확인
total_frames = sum(len(animation) for animation in animations)
print("전체 애니메이션 개수:", len(animations))
print("전체 프레임 개수:", total_frames)


animation = 0
frame = 0
repeat_count = 0

last_frame_time = get_time()
frame_interval = 0.1

is_paused = False
pause_start_time = 0.0

character_x = 100
character_y = 300

move_speed = 200
move_direction = 1

jump_start_y = 300
jump_height = 180
jump_start_y = 300
jump_height = 180
jump_time = 0.0

last_move_time = get_time()

def move_character(character_x, move_direction, deltaTime):
    character_x += move_speed * move_direction * deltaTime

    if character_x >= 1100:
        character_x = 1100
        move_direction = -1

    elif character_x <= 100:
        character_x = 100
        move_direction = 1

    return character_x, move_direction

def jump_character(character_y, jump_time, deltaTime):
    jump_time += deltaTime

    character_y = jump_start_y + jump_height * 4 * jump_time * (1.0 - jump_time)

    if jump_time >= 1.0:
        jump_time = 0.0
        character_y = jump_start_y

    return character_y, jump_time


while True:
    clear_canvas()

    # 현재 동작의 프레임 목록
    current_frames = animations[animation]

    # 현재 프레임
    x, y, width, height = current_frames[frame]

    sonic.clip_draw(
        x, y,
        width, height,
        character_x, character_y,
        width * 4, height * 4
    )

    update_canvas()

    current_time = get_time()

    # 이전 화면으로부터 얼마나 시간이 지났는지 계산
    deltaTime = current_time - last_move_time
    last_move_time = current_time

    # 이동 애니메이션 처리
    if moving_animations[animation] and not is_paused:
        character_x, move_direction = move_character(character_x, move_direction, deltaTime)

    if animation == 2 and not is_paused:
        character_y, jump_time = jump_character(character_y, jump_time, deltaTime)

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

            character_y = jump_start_y
            jump_time = 0.0

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()