import game_framework
from pico2d import *
import main

name = "TitleState"
image = None


def enter():
    global image
    image = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\title.png')


def exit():
    global image
    del(image)



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main)


def draw():
    clear_canvas()
    image.draw(500, 300, 1000, 600)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass





