from pico2d import *

open_canvas()

ground = load_image('ground.png')
character = load_image('kirby.png')


# 스프라이트 시트에서 한 프레임을 잘라서 출력하는 함수
def draw_frame(frame_data):
    clear_canvas()

    ground.draw(400, 45, 800, 90)

    # 현재 프레임의 위치와 크기
    left, bottom, width, height = frame_data

    # 캐릭터 크기를 키우고 원본 비율 유지
    draw_height = 300
    draw_width = width * (draw_height / height)

    # 스프라이트 시트에서 해당 프레임을 잘라 화면에 출력
    character.clip_draw(
        left, bottom,
        width, height,
        400, 185,
        draw_width, draw_height
    )

    update_canvas()


# ESC 키가 눌렸는지 확인
def check_quit():
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return True

    return False


# 하나의 애니메이션을 5번 반복
def play_animation(animation):
     
    for repeat in range(5):
         
        for frame in animation:

            if check_quit():
                return False

            draw_frame(frame)
            delay(0.07)

    # 애니메이션 5회 반복 후 1초 정지
    delay(1.0)

    return True


# (left, bottom, width, height)
# 스프라이트 시트 2번째 줄의 프레임 좌표
row2 = [
    (5,   362, 41, 39),
    (67,  362, 40, 39),
    (130, 362, 36, 39),
    (188, 362, 39, 39),
    (247, 362, 42, 39),
    (308, 362, 44, 39),
    (367, 362, 43, 39),
    (431, 362, 37, 39),
    (485, 362, 33, 39),
    (535, 362, 36, 39)
]

# 스프라이트 시트 3번째 줄의 프레임 좌표
row3 = [
    (7,   272, 43, 69),
    (69,  272, 40, 69),
    (143, 272, 40, 69),
    (227, 272, 66, 69),
    (321, 272, 66, 69),
    (419, 272, 62, 69),
    (499, 272, 62, 69)
]

# 스프라이트 시트 4번째 줄의 프레임 좌표
row4 = [
    (10,  177, 50, 52),
    (80,  177, 39, 52),
    (147, 177, 52, 52),
    (225, 177, 46, 52),
    (294, 177, 42, 52),
    (358, 177, 51, 52),
    (427, 177, 46, 52),
    (491, 177, 51, 52),
    (559, 177, 41, 52)
]

# 스프라이트 시트 6번째 줄의 프레임 좌표
row6 = [
    (10,  0, 43, 43),
    (74,  0, 46, 43),
    (141, 0, 43, 43),
    (205, 0, 36, 43),
    (269, 0, 43, 43),
    (336, 0, 46, 43),
    (407, 0, 43, 43),
    (477, 0, 36, 43)
]


# 프로그램 실행 여부
running = True


# 2 -> 3 -> 4 -> 6행의 애니메이션을 순서대로 무한 반복
while running:

    # 2행 애니메이션 
    if not play_animation(row2):
        running = False
        break

    # 3행 애니메이션
    if not play_animation(row3):
        running = False
        break

    # 4행 애니메이션
    if not play_animation(row4):
        running = False
        break

    # 6행 애니메이션
    if not play_animation(row6):
        running = False
        break

close_canvas()