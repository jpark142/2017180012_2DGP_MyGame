from pico2d import *
import game_world
from platforms import Platforms

class Bubble:
    #image = None

    def __init__(self, x = 400, y = 300, velocity = 1):

        self.image = load_image('bubble_p1.png')

        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
       # pt = Platforms() # 객체 불러오기

        if self.x < 25 or self.x > 1000 - 25:
            game_world.remove_object(self)
            print("Bubble Removed")
      #  elif self.x == pt.px1 -25 and self.y == pt.py1:
      #      game_world.remove_object(self)
       #    print("Bubble Removed")

    # 물방울 바운딩 박스
    def get_bb_b1(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20



class Bubble2:
    #image2 = None

    def __init__(self, x=400, y=300, velocity=1):
        #if self.image2 == None:
        self.image2 = load_image('bubble_p2.png')

        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image2.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1000 - 25:
            game_world.remove_object(self)
            print("Bubble2 Removed")

    def get_bb_b2(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

