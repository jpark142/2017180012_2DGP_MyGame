from pico2d import *

open_canvas()

grass= load_image('grass.png')
character = load_image('character.png')
character2 = load_image('character2.png')

x_p1 = 800 // 2
x_p2 = 750  # 시작 위치
frame = 0

dir_x_p1 = 0
dir_x_p2 = 0

sheet_line1 = 120
sheet_line2 = 180

running = True


def handle_events():
    global running, dir_x_p1, dir_x_p2, sheet_line1,sheet_line2, x_p1, x_p2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:  # 오른쪽이동 (플레이어1)
                dir_x_p1 += 10
                sheet_line1 = 0
            if event.key == SDLK_d:  # 오른쪽이동 (플레이어2)
                dir_x_p2 += 10
                sheet_line2 = 0

            elif event.key == SDLK_LEFT:  # 왼쪽이동 (플레이어1)
                dir_x_p1 -= 10
                sheet_line1 = 60
            elif event.key == SDLK_a:  # 왼쪽이동 (플레이어2)
                dir_x_p2 -= 10
                sheet_line2 = 60

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x_p1 -= 10
                sheet_line1 = 120
            if event.key == SDLK_d:
                dir_x_p2 -= 10
                sheet_line2 = 120

            elif event.key == SDLK_LEFT:
                dir_x_p1 += 10
                sheet_line1 = 180
            elif event.key == SDLK_a:
                dir_x_p2 += 10
                sheet_line2 = 180


def check_out_of_screen():
    global x_p1, x_p2
    if x_p1 <= 0:
        x_p1 = 0
    elif x_p2 <= 0:
        x_p2 = 0
    elif x_p1 >= 800:
        x_p1 = 800
    elif x_p2 >= 800:
        x_p2 = 800


while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 60, sheet_line1, 60, 60, x_p1, 70)
    character2.clip_draw(frame * 60, sheet_line2, 60, 60, x_p2, 70)
    handle_events()

    frame = (frame + 1) % 8


    update_canvas()

    x_p1 += dir_x_p1
    x_p2 += dir_x_p2


    check_out_of_screen()


    delay(0.07)

close_canvas()