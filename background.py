from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\giphy.gif')


    def update(self):
        pass

    def draw(self):
        self.image.draw(1000 / 2, 600 / 2)