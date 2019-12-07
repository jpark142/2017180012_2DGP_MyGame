import game_framework
from pico2d import *
import title_state

name = "BlueWinState"
image = None

bgm_blue_win = None


def enter():
    global image, bgm_blue_win
    image = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\ending_blue_win.png')
    bgm_blue_win = load_music('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\sound\\happy_winner.wav')
    bgm_blue_win.set_volume(64)
    bgm_blue_win.repeat_play()


def exit():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)


def draw():
    # clear_canvas()
    image.draw(500, 300)
    update_canvas()
    pass


def update():
    pass

