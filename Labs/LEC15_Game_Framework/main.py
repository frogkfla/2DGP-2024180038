from pico2d import close_canvas, open_canvas

import game_framework
import logo_mode
import play_mode
import title_mode


open_canvas()
game_framework.run(logo_mode)
close_canvas()
