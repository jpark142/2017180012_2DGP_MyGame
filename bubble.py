from pico2d import *
import game_world
from platforms import Platforms


class Bubble:
    #image = None

    def __init__(self, x = 500, y = 300, velocity = 1):

        self.image = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\bubble_p1.png')

        self.x, self.y, self.velocity = x, y, velocity
        self.updated_x = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        self.updated_x = self.x

       # pt = Platforms() # 객체 불러오기

        if self.x < 25 or self.x > 1000 - 25:
            game_world.remove_object(self)
            print("Bubble Removed")
      #  elif self.x == pt.px1 -25 and self.y == pt.py1:
      #      game_world.remove_object(self)
       #    print("Bubble Removed")

    # 물방울 바운딩 박스
    def get_bb_b1(self):
        return self.updated_x - 20, self.y - 20, self.updated_x + 20, self.y + 20


class Bubble2:
    #image2 = None

    def __init__(self, x=500, y=300, velocity=1):
        #if self.image2 == None:
        self.image2 = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\bubble_p2.png')

        self.x, self.y, self.velocity = x, y, velocity
        self.updated_x = 0
        self.updated_y = 0

        self.left_b2 = 0
        self.bottom_b2 = 0
        self.right_b2 = 0
        self.top_b2 = 0

    def draw(self):
        self.image2.draw(self.x, self.y)

    def update(self,player1):
        self.x += self.velocity
        self.updated_x = self.x
        self.updated_y = self.y

        if self.x < 25 or self.x > 1000 - 25:
            game_world.remove_object(self)
            #print("Bubble2 Removed")

        if is_bubble_hit(player1, self):
            player1.isHit = True


    def get_bb_b2(self):
        return self.updated_x - 20, self.updated_y - 20, self.updated_x + 20, self.updated_y + 20



 # 물방울과 플레이어 충돌
    # 만약에 is_bubble_hit == True 이면 idle->in_bubble, run->in_bubble
def is_bubble_hit(player1, bubble2):
        # if 맞았으면 return True 안맞았으면 return False
    left_p1, bottom_p1, right_p1, top_p1 = player1.get_bb()  # player1의 바운딩박스
    left_b2, bottom_b2, right_b2, top_b2 = bubble2.get_bb_b2()  # player2의 물방울 바운딩박스

    if left_p1 > right_b2:
        return False
    if right_p1 < left_b2:
        return False
    if top_p1 < bottom_b2:
        return False
    if bottom_p1 > top_b2:
        return False
    return True





