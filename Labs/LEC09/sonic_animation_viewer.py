from pico2d import *

open_canvas(1200, 600)

sonic = load_image('sonic-sprite.png')

# 첫 번째 애니메이션
frames1 = [
    (1,   448, 29, 38),
    (31,  448, 26, 38),
    (58,  448, 29, 38),
    (88,  448, 29, 38),
    (118, 448, 29, 38),
    (148, 448, 30, 38),
    (180, 448, 29, 38),
    (210, 448, 29, 38),
    (240, 448, 29, 38),
    (270, 448, 24, 38),
    (302, 448, 29, 38)
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
    (1,   326, 29, 35),
    (35,  326, 30, 35),
    (67,  326, 30, 35),
    (98,  326, 31, 35),
    (131, 326, 29, 35),
    (162, 326, 30, 35),
    (193, 326, 30, 35),
    (230, 326, 31, 35),
    (268, 326, 30, 35)
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
    (1,   154, 24, 45),
    (31,  154, 29, 44),
    (65,  154, 20, 44),
    (90,  155, 25, 43),
    (119, 155, 25, 43),
    (149, 154, 20, 44),
    (184, 156, 40, 28),
    (232, 157, 39, 27)
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
    False,  # 1번
    True,   # 2번
    True,   # 3번
    False,  # 4번
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
print("이동 애니메이션 개수:", sum(moving_animations))
print("중앙 재생 애니메이션 개수:", len(moving_animations) - sum(moving_animations))

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

def check_frames():
    image_width = 399
    image_height = 525

    for animation_index, animation_frames in enumerate(animations):
        for frame_index, (x, y, width, height) in enumerate(animation_frames):
            if x < 0 or y < 0 or x + width > image_width or y + height > image_height:
                print("잘못된 프레임:", animation_index + 1, frame_index + 1)
                return

    print("모든 프레임 좌표 정상")

check_frames()


while True:
    clear_canvas()

    # 현재 동작의 프레임 목록
    current_frames = animations[animation]

    # 현재 프레임
    x, y, width, height = current_frames[frame]

    if move_direction == 1:
        sonic.clip_draw(
        x, y,
        width, height,
        character_x, character_y,
        width * 4, height * 4
    )
    else:
        sonic.clip_composite_draw(
        x, y,
        width, height,
        0,
        'h',
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

    if animation == 7 and not is_paused:
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

            if not moving_animations[animation]:
                character_x = 600
            else:
                character_x = 100
                move_direction = 1

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            close_canvas()
            exit()