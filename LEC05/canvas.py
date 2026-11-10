## 여기를 채워주세요

from pico2d import *
open_canvas(800, 600)
update_canvas()
delay(5)
close_canvas()



from pico2d import *

open_canvas(800,600)

character = load_image('character.png')

for x in range(0, 9):
    for y in range(0, 7):
        character.draw(x * 100, y * 100)
        update_canvas()


delay(2)

close_canvas()