from pico2d import *
import game_world

class Bubble:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bubble.image == None:
            Bubble.image = load_image('bubble_p1.png')

        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1000 - 25:
            game_world.remove_object(self)
            print("Bubble Removed")


class Bubble2:
    image2 = None

    def __init__(self, x=400, y=300, velocity=1):
        if Bubble2.image2 == None:
            Bubble2.image2 = load_image('bubble_p2.png')

        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image2.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1000 - 25:
            game_world.remove_object(self)
            print("Bubble2 Removed")

