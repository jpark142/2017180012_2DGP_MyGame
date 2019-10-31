from pico2d import *
from player import *
from grass import *
from background import *

import game_framework


name = "MainState"


def collide_check():
    global player1, grass, bubble
    if player1.y <= grass.y + 40:
        player1.y = grass.y + 40
        player1.jumping = False
    if player2.y <= grass.y + 40:
        player2.y = grass.y + 40
        player2.jumping = False

    if player1.x > 1000:
        player1.x = 0
    if player1. x < 0:
        player1.x = 1000
    if player2.x > 1000:
        player2.x = 0
    if player2. x < 0:
        player2.x = 1000


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player1.handle_event(event)
            player2.handle_event(event)


background = None
grass = None
player1 = None
player2 = None
bubble = None

running = True


def enter():
    global player1, player2, grass, background, bubble
    player1 = Player1()
    player2 = Player2()
    grass = Grass()
    bubble = Bubble()
    background = Background()

    game_world.add_object(background, 0)
    game_world.add_object(grass, 1)
    game_world.add_object(player1, 2)
    game_world.add_object(player2, 3)




def exit():
    global player1, player2, grass, background, bubble
    del player1
    del player2
    del grass
    del background
    del bubble
    game_world.clear()


def update():
    player1.update()
    player2.update()
    for game_object in game_world.all_objects():
        game_object.update()
        collide_check()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()



