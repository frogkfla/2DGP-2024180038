from pico2d import get_canvas_width, load_image

import game_world


selected_item = None


def select_item(item):
    """None, 1(작은 공), 2(큰 공) 중 발사할 아이템을 선택한다."""
    global selected_item
    selected_item = item


def get_selected_item():
    return selected_item


class Ball:
    images = {}

    def __init__(self, x, y, velocity, item):
        image_file = {1: 'ball21x21.png', 2: 'ball41x41.png'}[item]
        if item not in Ball.images:
            Ball.images[item] = load_image(image_file)

        self.x, self.y = x, y
        self.velocity = velocity
        self.image = Ball.images[item]

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
