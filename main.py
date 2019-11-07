from pico2d import *
from player import *
from grass import *
from background import *

from platforms import *
import game_framework


name = "MainState"


def collide_check():
    global player1, grass, platforms
    if player1.y <= grass.y + 40:
        player1.y = grass.y + 40
        if player1.vel_y < 0:
            player1.vel_y = 0
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

    #if player1.y <= platforms.py1 + 40:
    #    player1.y = platforms.py1 + 40

    # check if player hits a platform - only if falling
    if player1.vel_y < 0:
        if collide_p1_pf1(player1, platforms):
            player1.y = platforms.py1 + 45
            player1.vel_y = 0
            player1.jumping = False
            #print("충돌!")
        if collide_p1_pf2(player1, platforms):
            player1.y = platforms.py2 + 45
            player1.vel_y = 0
            player1.jumping = False
            #print("충돌2!")
        if collide_p1_pf3(player1, platforms):
            player1.y = platforms.py3 + 45
            player1.vel_y = 0
            player1.jumping = False
            #print("충돌3!")
        if collide_p1_pf4(player1, platforms):
            player1.y = platforms.py4 + 45
            player1.vel_y = 0
            player1.jumping = False
            #print("충돌4!")
        if collide_p1_pf5(player1, platforms):
            player1.y = platforms.py5 + 45
            player1.vel_y = 0
            player1.jumping = False
            #print("충돌5!")


def collide_p1_pf1(player1, platforms):
    left_p1, bottom_p1, right_p1, top_p1 = player1.get_bb()
    # 플랫폼1
    left_pf1, bottom_pf1, right_pf1, top_pf1 = platforms.get_bb()

    if left_p1 > right_pf1: return False
    if right_p1 < left_pf1: return False
    if top_p1 < bottom_pf1: return False
    if bottom_p1 > top_pf1: return False
    return True


def collide_p1_pf2(player1, platforms):
    left_p1, bottom_p1, right_p1, top_p1 = player1.get_bb()
    # 플랫폼2
    left_pf2, bottom_pf2, right_pf2, top_pf2 = platforms.get_bb2()

    if left_p1 > right_pf2: return False
    if right_p1 < left_pf2: return False
    if top_p1 < bottom_pf2: return False
    if bottom_p1 > top_pf2: return False
    return True

def collide_p1_pf3(player1, platforms):
    left_p1, bottom_p1, right_p1, top_p1 = player1.get_bb()
    # 플랫폼3
    left_pf3, bottom_pf3, right_pf3, top_pf3 = platforms.get_bb3()
    if left_p1 > right_pf3: return False
    if right_p1 < left_pf3: return False
    if top_p1 < bottom_pf3: return False
    if bottom_p1 > top_pf3: return False
    return True

def collide_p1_pf4(player1, platforms):
    left_p1, bottom_p1, right_p1, top_p1 = player1.get_bb()
    # 플랫폼4
    left_pf4, bottom_pf4, right_pf4, top_pf4 = platforms.get_bb4()
    if left_p1 > right_pf4: return False
    if right_p1 < left_pf4: return False
    if top_p1 < bottom_pf4: return False
    if bottom_p1 > top_pf4: return False
    return True

def collide_p1_pf5(player1, platforms):
    left_p1, bottom_p1, right_p1, top_p1 = player1.get_bb()
    # 플랫폼5
    left_pf5, bottom_pf5, right_pf5, top_pf5 = platforms.get_bb5()
    if left_p1 > right_pf5: return False
    if right_p1 < left_pf5: return False
    if top_p1 < bottom_pf5: return False
    if bottom_p1 > top_pf5: return False
    return True


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
bubble2 = None
platforms = None

running = True


def enter():
    global player1, player2, grass, background, bubble, bubble2, platforms
    player1 = Player1()
    player2 = Player2()
    grass = Grass()
    bubble = Bubble()
    bubble2 = Bubble2()
    background = Background()
    platforms = Platforms()

    game_world.add_object(background, 0)
    game_world.add_object(grass, 1)
    game_world.add_object(platforms, 2)
    game_world.add_object(player1, 3)
    game_world.add_object(player2, 4)



def exit():
    global player1, player2, grass, background, bubble, bubble2, platforms
    del player1
    del player2
    del grass
    del background
    del bubble
    del bubble2
    del platforms
    game_world.clear()


def update():
    global player1, bubble2
    player1.update()
    player2.update()
    for game_object in game_world.all_objects():
        game_object.update()
        collide_check()

    for b2 in game_world.bubble2_objects:  # 버블2를 가져온다
        b2.update(player1)





def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    for game_object in game_world.bubble2_objects:
        game_object.draw()

    update_canvas()



