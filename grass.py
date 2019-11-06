from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\grass.png')
        self.x, self.y = 400, 30

    def update(self):
        pass


    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(800, 30)


    #def get_bb(self):
    #    return self.x - 400, self.y, self.x + 400, self.y