# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')


# 캐릭터를 지정한 위치에 그리는 함수 
def draw_character(x, y): 
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)   


# 원 모양으로 캐릭터 이동
def draw_circle():
    print("circle")

    center_x = 400
    center_y = 300
    radius = 200

    for deg in range(0, 360, 5): # 0~360도 5도씩 이동
        rad = math.radians(deg) # 각도를 라디안으로 변환

        # 원 위의 x,y 좌표 계산
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)

        draw_character(x, y)
    

# 사각형의 위쪽 방향 이동
def draw_top():
    print("top")

    stat_x = 50
    end_x = 750
    top_y = 550

    for x in range(stat_x, end_x, 5):
        draw_character(x, top_y)


# 사각형의 오른쪽 방향 이동
def draw_right():
    right_x = 750
    stat_y = 550
    end_y = 50

    for y in range(stat_y, end_y, -5):
        draw_character(right_x, y)


# 사각형의 아래쪽 방향 이동
def draw_bottom():
    stat_x = 750
    end_x = 50
    bottom_y = 50

    for x in range(stat_x, end_x, -5):
        draw_character(x, bottom_y)


# 사각형의 왼쪽 방향 이동
def draw_left():
    left_x = 50
    stat_y = 50
    end_y = 550

    for y in range(stat_y, end_y, 5):
        draw_character(left_x, y)


# 사각형 모양으로 캐릭터 이동 ( 위 - 오 - 아 - 왼 )
def draw_rectangle():
    print("rectangle")
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()


# 두 점 사이를 직선으로 이동
def draw_line(x0, y0, x1, y1):
    steps = 100 

    for step in range(steps + 1):
        t = step / steps 
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t

        draw_character(x, y)


# 삼각형 아래쪽 A -> B 이동    
def draw_triangle_bottom():
    print("triangle - bottom (A -> B)")

    start_x = 100
    start_y = 100
    end_x = 700
    end_y = 100

    draw_line(start_x, start_y, end_x, end_y)


# 삼각형 오른쪽 대각선 B -> C 이동
def draw_triangle_right_up():
    print("triangle - right up (B -> C)")

    start_x = 700
    start_y = 100
    end_x = 400
    end_y = 500

    draw_line(start_x, start_y, end_x, end_y)


# 삼각형 왼쪽 대각선 C -> A 이동
def draw_triangle_left_down():
    print("triangle - left down (C -> A)")

    start_x = 400
    start_y = 500
    end_x = 100
    end_y = 100

    draw_line(start_x, start_y, end_x, end_y)


# 삼각형 모양으로 캐릭터 이동 ( A - B - C - A )
def draw_triangle():
    print("triangle")
    draw_triangle_bottom()
    draw_triangle_right_up()
    draw_triangle_left_down()


# 원 -> 사각형 -> 삼각형 무한 루프
while True :
    draw_circle()
    draw_rectangle()
    draw_triangle()


close_canvas()