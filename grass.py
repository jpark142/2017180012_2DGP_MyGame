from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\grass.png')
        self.x, self.y = 400, 30
        self.bgm_main = load_music('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\sound\\happy2.mp3')
        self.bgm_main.set_volume(64)
        self.bgm_main.repeat_play()


    def update(self):
        pass


    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(800, 30)


    #def get_bb(self):
    #    return self.x - 400, self.y, self.x + 400, self.y