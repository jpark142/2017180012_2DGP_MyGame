from pico2d import *
from bubble import Bubble, Bubble2
from grass import Grass

import game_world


PLAYER_GRAVITY = -0.01

RIGHT_DOWN_p1, LEFT_DOWN_p1, RIGHT_UP_p1, LEFT_UP_p1, UP_UP_p1, UP_DOWN_p1, BUBBLE_SHOT_p1,\
    RIGHT_DOWN_p2, LEFT_DOWN_p2, RIGHT_UP_p2, LEFT_UP_p2, UP_UP_p2, UP_DOWN_p2, BUBBLE_SHOT_p2 = range(14)

key_event_table = {
    # 플레이어1 키 입력
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN_p1,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN_p1,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP_p1,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP_p1,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN_p1,
    (SDL_KEYUP, SDLK_UP): UP_UP_p1,
    (SDL_KEYDOWN, SDLK_RSHIFT): BUBBLE_SHOT_p1,
}
key_event_table2 = {
    # 플레이어2 키 입력
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN_p2,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN_p2,
    (SDL_KEYUP, SDLK_d): RIGHT_UP_p2,
    (SDL_KEYUP, SDLK_a): LEFT_UP_p2,
    (SDL_KEYDOWN, SDLK_w): UP_DOWN_p2,
    (SDL_KEYUP, SDLK_w): UP_UP_p2,
    (SDL_KEYDOWN, SDLK_LSHIFT): BUBBLE_SHOT_p2
}


class IdleState:
    @staticmethod
    def enter_p1(player1, event):
        # 플레이어1
        if event == RIGHT_DOWN_p1:
            player1.vel_x += 0.5
        elif event == LEFT_DOWN_p1:
            player1.vel_x -= 0.5
        elif event == RIGHT_UP_p1:
            player1.vel_x -= 0.5
        elif event == LEFT_UP_p1:
            player1.vel_x += 0.5
        elif event == UP_DOWN_p1 and player1.jumping == False:
            player1.vel_y = 2
            player1.jumping = True

        elif event == UP_UP_p1:
            player1.jumping = True

       # player1.timer = 1000
    @staticmethod
    def enter_p2(player2, event2):
        # 플레이어2
        if event2 == RIGHT_DOWN_p2:
            player2.vel_x += 0.5
        elif event2 == LEFT_DOWN_p2:
            player2.vel_x -= 0.5
        elif event2 == RIGHT_UP_p2:
            player2.vel_x -= 0.5
        elif event2 == LEFT_UP_p2:
            player2.vel_x += 0.5
        elif event2 == UP_DOWN_p2 and player2.jumping == False:
            player2.vel_y = 2
            player2.jumping = True

        elif event2 == UP_UP_p2:
            player2.jumping = True

       # player2.timer = 1000


    @staticmethod
    def exit_p1(player1, event):
        if event == BUBBLE_SHOT_p1:
            player1.bubble_shot()
    @staticmethod
    def exit_p2(player2, event2):
        if event2 == BUBBLE_SHOT_p2:
            player2.bubble_shot()

    @staticmethod
    def do_p1(player1):
        # 플레이어1
        player1.frame1 = (player1.frame1+1) % 16
       # player1.timer -= 1
        player1.x += player1.vel_x
        player1.y += player1.vel_y
        player1.vel_y += player1.acc_y
        # player1.x = clamp(25, player1.x, 1000 - 25)

    @staticmethod
    def do_p2(player2):
        # 플레이어2
        player2.frame2 = (player2.frame2+1) % 8
       # player2.timer -= 1
        player2.x += player2.vel_x
        player2.y += player2.vel_y
        player2.vel_y += player2.acc_y
       # player2.x = clamp(25, player2.x, 1000 - 25)

    @staticmethod
    def draw_p1(player1):
        # 플레이어1
        if player1.vel_x == 0 and player1.dir == -1:  # 왼쪽보고 가만히 있기
            #.image.clip_draw(player1.frame1*60, sheet_line, 60, 60, player1.x, player1.y)
            player1.sheet_line = 180
        elif player1.vel_x == 0 and player1.dir == 1: # 오른쪽보고 가만히 있기
            #player1.image.clip_draw(player1.frame1*60, sheet_line, 60, 60, player1.x, player1.y)
            player1.sheet_line = 120


        #elif player1.vel_x == 1 and player1.dir == 1:
        #    player1.image.clip_draw(player1.frame*60, 0, 60, 60, player1.x, player1.y)
        #elif player1.vel_x == 1 and player1.dir == -1:
        #    player1.image.clip_draw(player1.frame*60, 60, 60, 60, player1.x, player1.y)
    @staticmethod
    def draw_p2(player2):
        # 플레이어2
        if player2.dir == 1: # 오른쪽보고 가만히 있기
            player2.image.clip_draw(player2.frame2*60, 120, 60, 60, player2.x, player2.y)
        elif player2.dir == -1:  # 왼쪽보고 가만히 있기
            player2.image.clip_draw(player2.frame2*60, 180, 60, 60, player2.x, player2.y)

class RunState:

    @staticmethod
    def enter_p1(player1, event):
        # 플레이어1
        if event == RIGHT_DOWN_p1:
            player1.vel_x += 0.5
            player1.dir = 1
        elif event == LEFT_DOWN_p1:
            player1.vel_x -= 0.5
            player1.dir = -1
        elif event == RIGHT_UP_p1:
            player1.vel_x -= 0.5
            player1.dir = -1
        elif event == LEFT_UP_p1:
            player1.vel_x += 0.5
            player1.dir = 1

        elif event == UP_DOWN_p1 and player1.jumping == False:
            player1.vel_y = 2
            player1.jumping = True

        elif event == UP_UP_p1:
            player1.jumping = True

    @staticmethod
    def enter_p2(player2, event2):
        # 플레이어2
        if event2 == RIGHT_DOWN_p2:
            player2.vel_x += 0.5
            player2.dir = 1
        elif event2 == LEFT_DOWN_p2:
            player2.vel_x -= 0.5
            player2.dir = -1
        elif event2 == RIGHT_UP_p2:
            player2.vel_x -= 0.5
            player2.dir = -1
        elif event2 == LEFT_UP_p2:
            player2.vel_x += 0.5
            player2.dir = 1
        elif event2 == UP_DOWN_p2 and player2.jumping == False:
            player2.vel_y = 2
            player2.jumping = True

        elif event2 == UP_UP_p2:
            player2.jumping = True

       # player1.dir = player1.vel_x

    @staticmethod
    def exit_p1(player1, event):
        if event == BUBBLE_SHOT_p1:
            player1.bubble_shot()


    @staticmethod
    def exit_p2(player2, event2):
        if event2 == BUBBLE_SHOT_p2:
            player2.bubble_shot()

    @staticmethod
    def do_p1(player1):
        # 플레이어1
        player1.frame1 = (player1.frame1 + 1) % 16
        # boy.timer -= 1
        player1.x += player1.vel_x
        player1.y += player1.vel_y
        player1.vel_y += player1.acc_y
       # player1.x = clamp(25, player1.x, 1000 - 25)

    @staticmethod
    def do_p2(player2):
        # 플레이어2
        player2.frame2 = (player2.frame2 + 1) % 8
        # player2.timer -= 1
        player2.x += player2.vel_x
        player2.y += player2.vel_y
        player2.vel_y += player2.acc_y
       # player2.x = clamp(25, player2.x, 1000 - 25)

    @staticmethod
    def draw_p1(player1):
        # 플레이어1
        if player1.vel_x == 0 and player1.dir == -1:  # 왼쪽보고 가만히 있기
           # player1.image.clip_draw(player1.frame1 * 60, sheet_line, 60, 60, player1.x, player1.y)
            player1.sheet_line = 180
        elif player1.vel_x == 0 and player1.dir == 1:  # 오른쪽보고 가만히 있기
            player1.sheet_line = 120
            #player1.image.clip_draw(player1.frame1 * 60, sheet_line, 60, 60, player1.x, player1.y)
        if player1.vel_x > 0:
            #player1.image.clip_draw(player1.frame1 * 60, 0, 60, 60, player1.x, player1.y)
            player1.sheet_line = 0
        elif player1.vel_x < 0:
            #player1.image.clip_draw(player1.frame1 * 60, 60, 60, 60, player1.x, player1.y)
            player1.sheet_line = 60


    @staticmethod
    def draw_p2(player2):
        # 플레이어2
        if player2.vel_x > 0:
            player2.image.clip_draw(player2.frame2 * 60, 0, 60, 60, player2.x, player2.y)
        elif player2.vel_x < 0:
            player2.image.clip_draw(player2.frame2 * 60, 60, 60, 60, player2.x, player2.y)
        if player2.vel_x == 0 and player2.dir == 1:  # 오른쪽보고 가만히 있기
            player2.image.clip_draw(player2.frame2 * 60, 120, 60, 60, player2.x, player2.y)
        elif player2.vel_x == 0 and player2.dir == -1:  # 왼쪽보고 가만히 있기
            player2.image.clip_draw(player2.frame2 * 60, 180, 60, 60, player2.x, player2.y)


next_state_table = {
    IdleState: {RIGHT_UP_p1: RunState, LEFT_UP_p1: RunState,
                RIGHT_DOWN_p1: RunState, LEFT_DOWN_p1: RunState,
                UP_UP_p1: RunState, UP_DOWN_p1: RunState,
                BUBBLE_SHOT_p1: IdleState},
    RunState: {RIGHT_UP_p1: IdleState, LEFT_UP_p1: IdleState,
               LEFT_DOWN_p1: IdleState, RIGHT_DOWN_p1: IdleState,
               UP_UP_p1: IdleState, UP_DOWN_p1: IdleState,
               BUBBLE_SHOT_p1: RunState}
}
next_state_table2 = {
    IdleState: {
        RIGHT_UP_p2: RunState, LEFT_UP_p2: RunState,
        RIGHT_DOWN_p2: RunState, LEFT_DOWN_p2: RunState,
        UP_UP_p2: RunState, UP_DOWN_p2: RunState,
        BUBBLE_SHOT_p2: IdleState},
    RunState: {
        RIGHT_UP_p2: IdleState, LEFT_UP_p2: IdleState,
        LEFT_DOWN_p2: IdleState, RIGHT_DOWN_p2: IdleState,
        UP_UP_p2: IdleState, UP_DOWN_p2: IdleState,
        BUBBLE_SHOT_p2: RunState}

}

class Player1:
    def __init__(self):
        self.x, self.y = (1000 - 50, 600 / 2)
        self.vel_x, self.vel_y = 0, 0
        self.acc_x, self.acc_y = 0, PLAYER_GRAVITY
        self.frame1 = 0
        self.image = load_image('green.png')
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter_p1(self, None)
        self.dir = 1
        self.jumping = False
        self.sheet_line = 180

    def bubble_shot(self):
        print("Bubble shot")
        bubble = Bubble(self.x, self.y, self.dir*3)
        grass = Grass()
        game_world.add_object(bubble, 2)
        if bubble.y <= grass.y + 40:  # 물방울이 중력때문에 화면 밖으로 내려가지 않게 함
            bubble.y = grass.y + 40

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do_p1(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit_p1(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter_p1(self, event)

    def draw(self):
       # self.image.clip_composite_draw(self.frame1 * 60, self.sheet_line, 60, 60, 0,'v', self.x, self.y)
       self.image.clip_draw(self.frame1 * 60, self.sheet_line, 60, 60, self.x, self.y)

       self.cur_state.draw_p1(self)


    def handle_event(self, event):

        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)



        #delay(0.03)

    # collide box
    #def get_bb(self):
    #    return self.x - 30, self.y - 30, self.x + 30, self.y - 30


class Player2:
    def __init__(self):
        self.x, self.y = (50, 600 / 2)
        self.vel_x, self.vel_y = 0, 0
        self.acc_x, self.acc_y = 0, PLAYER_GRAVITY
        self.frame2 = 0
        self.image = load_image('character2.png')
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter_p2(self, None)
        self.dir = 1
        self.jumping = False

    def bubble_shot(self):
        print("Bubble2 shot")
        bubble2 = Bubble2(self.x, self.y, self.dir*3)
        grass = Grass()  # grass 객체를 가져옴
        game_world.add_object(bubble2, 2)
        if bubble2.y <= grass.y + 40:  # 물방울이 중력때문에 화면 밖으로 내려가지 않게 함
            bubble2.y = grass.y + 40

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do_p2(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit_p2(self, event)
            self.cur_state = next_state_table2[self.cur_state][event]
            self.cur_state.enter_p2(self, event)

    def draw(self):
        self.cur_state.draw_p2(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table2:
            key_event2 = key_event_table2[(event.type, event.key)]
            self.add_event(key_event2)




