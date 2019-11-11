from pico2d import *
from bubble import *
from grass import Grass

import game_world
import game_framework
import time

PLAYER_GRAVITY = -0.01


# Run Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30cm
RUN_SPEED_KMPH = 30.0  # km / hour
RUN_SPEED_MPM = 0
RUN_SPEED_MPS = 0
RUN_SPEED_PPS = 250.0

# Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
FRAMES_PER_ACTION = 32

STAND_FRAMES_PER_ACTION = 8
maintain = 2000


RIGHT_DOWN_p1, LEFT_DOWN_p1, RIGHT_UP_p1, LEFT_UP_p1, UP_UP_p1, UP_DOWN_p1, BUBBLE_SHOT_p1,\
    RIGHT_DOWN_p2, LEFT_DOWN_p2, RIGHT_UP_p2, LEFT_UP_p2, UP_UP_p2, UP_DOWN_p2, BUBBLE_SHOT_p2,\
    DOWN_DOWN_p1, DOWN_UP_p1, DOWN_DOWN_p2, DOWN_UP_p2, BUBBLE_HIT = range(19)

key_event_table = {
    # 플레이어1 키 입력
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN_p1,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN_p1,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP_p1,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP_p1,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN_p1,
    (SDL_KEYUP, SDLK_UP): UP_UP_p1,
    (SDL_KEYDOWN, SDLK_RSHIFT): BUBBLE_SHOT_p1,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN_p1,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP_p1
}
key_event_table2 = {
    # 플레이어2 키 입력
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN_p2,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN_p2,
    (SDL_KEYUP, SDLK_d): RIGHT_UP_p2,
    (SDL_KEYUP, SDLK_a): LEFT_UP_p2,
    (SDL_KEYDOWN, SDLK_w): UP_DOWN_p2,
    (SDL_KEYUP, SDLK_w): UP_UP_p2,
    (SDL_KEYDOWN, SDLK_LSHIFT): BUBBLE_SHOT_p2,
    (SDL_KEYDOWN, SDLK_s): DOWN_DOWN_p2,
    (SDL_KEYUP, SDLK_s): DOWN_UP_p2
}


class IdleState:
    @staticmethod
    def enter_p1(player1, event):
        # 플레이어1
        if event == RIGHT_DOWN_p1:
            player1.vel_x += RUN_SPEED_PPS
            player1.dir = 1
        elif event == LEFT_DOWN_p1:
            player1.vel_x -= RUN_SPEED_PPS
            player1.dir = -1

        elif event == RIGHT_UP_p1:
            player1.vel_x -= RUN_SPEED_PPS

        elif event == LEFT_UP_p1:
            player1.vel_x += RUN_SPEED_PPS

        elif event == UP_DOWN_p1 and player1.jumping is False:
            player1.vel_y = 2
            player1.jumping = True

        elif event == UP_UP_p1:
            player1.jumping = True

        elif event == DOWN_DOWN_p1:
            pass
        elif event == DOWN_UP_p1:
            pass


    @staticmethod
    def enter_p2(player2, event2):
        # 플레이어2
        if event2 == RIGHT_DOWN_p2:
            player2.vel_x += RUN_SPEED_PPS
        elif event2 == LEFT_DOWN_p2:
            player2.vel_x -= RUN_SPEED_PPS
        elif event2 == RIGHT_UP_p2:
            player2.vel_x -= RUN_SPEED_PPS
        elif event2 == LEFT_UP_p2:
            player2.vel_x += RUN_SPEED_PPS
        elif event2 == UP_DOWN_p2 and player2.jumping is False:
            player2.vel_y = 2
            player2.jumping = True

        elif event2 == UP_UP_p2:
            player2.jumping = True

        elif event2 == DOWN_DOWN_p2:
            pass
        elif event2 == DOWN_UP_p2:
            pass

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
        global maintain
        maintain = 2000

        # 플레이어1
        player1.frame1 = (player1.frame1 + STAND_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        player1.x += player1.vel_x * game_framework.frame_time
        player1.y += player1.vel_y
        player1.vel_y += player1.acc_y

        if player1.isHit is True:
            print("inBubbleState 상태로 바뀌었습니다.")
            player1.add_event(BUBBLE_HIT)
            player1.isHit = False

    @staticmethod
    def do_p2(player2):
        # 플레이어2
        player2.frame2 = (player2.frame2 + STAND_FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        player2.x += player2.vel_x * game_framework.frame_time
        player2.y += player2.vel_y
        player2.vel_y += player2.acc_y

    @staticmethod
    def draw_p1(player1):

        # 플레이어1
        if player1.vel_x == 0 and player1.dir == -1:  # 왼쪽보고 가만히 있기

            player1.sheet_line = 180
        elif player1.vel_x == 0 and player1.dir == 1:  # 오른쪽보고 가만히 있기

            player1.sheet_line = 120
        elif player1.vel_y >= 0 and player1.dir == 1:
            player1.sheet_line = 120
        elif player1.vel_y >= 0 and player1.dir == -1:
            player1.sheet_line = 180

        elif player1.isShot is True:
            player1.attack.clip_draw(0, 0, 60, 60, player1.x, player1.y)
            player1.isShot = False

    @staticmethod
    def draw_p2(player2):
        # 플레이어2
        if player2.dir == 1:  # 오른쪽보고 가만히 있기
            player2.sheet_line = 120

        elif player2.dir == -1:  # 왼쪽보고 가만히 있기
            player2.sheet_line = 180


class RunState:
    @staticmethod
    def enter_p1(player1, event):
        global maintain
        # 플레이어1
        if event == RIGHT_DOWN_p1:
            player1.vel_x += RUN_SPEED_PPS
            player1.dir = 1
        elif event == LEFT_DOWN_p1:
            player1.vel_x -= RUN_SPEED_PPS
            player1.dir = -1
        elif event == RIGHT_UP_p1:
            player1.vel_x -= RUN_SPEED_PPS
            player1.dir = -1
        elif event == LEFT_UP_p1:
            player1.vel_x += RUN_SPEED_PPS
            player1.dir = 1

        elif event == UP_DOWN_p1 and player1.jumping is False:
            player1.vel_y = 2
            player1.jumping = True

        elif event == UP_UP_p1:
            player1.jumping = True

        elif event == DOWN_DOWN_p1:
            pass
        elif event == DOWN_UP_p1:
            pass

        maintain = 2000

    @staticmethod
    def enter_p2(player2, event2):
        # 플레이어2
        if event2 == RIGHT_DOWN_p2:
            player2.vel_x += RUN_SPEED_PPS
            player2.dir = 1
        elif event2 == LEFT_DOWN_p2:
            player2.vel_x -= RUN_SPEED_PPS
            player2.dir = -1

        elif event2 == RIGHT_UP_p2:
            player2.vel_x -= RUN_SPEED_PPS
            player2.dir = -1
        elif event2 == LEFT_UP_p2:
            player2.vel_x += RUN_SPEED_PPS
            player2.dir = 1
        elif event2 == UP_DOWN_p2 and player2.jumping is False:
            player2.vel_y = 2
            player2.jumping = True

        elif event2 == UP_UP_p2:
            player2.jumping = True

        elif event2 == DOWN_DOWN_p2:
            pass
        elif event2 == DOWN_UP_p2:
            pass

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
        player1.frame1 = (player1.frame1 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        player1.x += player1.vel_x * game_framework.frame_time
        player1.y += player1.vel_y
        player1.vel_y += player1.acc_y
        if player1.isHit is True:
            print("inBubbleState 상태로 바뀌었습니다.")
            player1.add_event(BUBBLE_HIT)
            player1.isHit = False

    @staticmethod
    def do_p2(player2):
        # 플레이어2
        player2.frame2 = (player2.frame2 + + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        player2.x += player2.vel_x * game_framework.frame_time
        player2.y += player2.vel_y
        player2.vel_y += player2.acc_y

    @staticmethod
    def draw_p1(player1):
        # 플레이어1
        if player1.vel_x == 0 and player1.dir == -1:  # 왼쪽보고 가만히 있기

            player1.sheet_line = 180
        elif player1.vel_x == 0 and player1.dir == 1:  # 오른쪽보고 가만히 있기
            player1.sheet_line = 120

        if player1.vel_x > 0:

            player1.sheet_line = 0
        elif player1.vel_x < 0:

            player1.sheet_line = 60

        if player1.isShot is True:
            player1.attack.clip_draw(0, 0, 60, 60, player1.x, player1.y)
            player1.isShot = False

    @staticmethod
    def draw_p2(player2):
        # 플레이어2
        if player2.vel_x > 0:
            player2.sheet_line = 0

        elif player2.vel_x < 0:
            player2.sheet_line = 60

        if player2.vel_x == 0 and player2.dir == 1:  # 오른쪽보고 가만히 있기
            player2.sheet_line = 120

        elif player2.vel_x == 0 and player2.dir == -1:  # 왼쪽보고 가만히 있기
            player2.sheet_line = 180


class InBubbleState:
    @staticmethod
    def enter_p1(player1, event):
        # 플레이어1
        if event == RIGHT_DOWN_p1:
            player1.vel_x += RUN_SPEED_PPS

        elif event == LEFT_DOWN_p1:
            player1.vel_x -= RUN_SPEED_PPS

        elif event == RIGHT_UP_p1:
            player1.vel_x -= RUN_SPEED_PPS

        elif event == LEFT_UP_p1:
            player1.vel_x += RUN_SPEED_PPS

        player1.acc_y = 0  # 중력은 없애준다

        # 위아래
        if event == DOWN_DOWN_p1:
            player1.vel_y = PLAYER_GRAVITY
            player1.vel_y -= 0.5
        elif event == DOWN_UP_p1:
            player1.vel_y = PLAYER_GRAVITY
            #player1.vel_y += 0.5
        elif event == UP_DOWN_p1:
            player1.vel_y = PLAYER_GRAVITY

            player1.vel_y += 0.5

        elif event == UP_UP_p1:
            player1.vel_y = PLAYER_GRAVITY
            #player1.vel_y -= 0.5

       # player1.timer = 2000  # inBubbleState 지속시간
        player1.frame1 = 0

    @staticmethod
    def enter_p2(player2, event):
        # 플레이어2
        if event == RIGHT_DOWN_p2:
            player2.vel_x += RUN_SPEED_PPS

        elif event == LEFT_DOWN_p2:
            player2.vel_x -= RUN_SPEED_PPS

        elif event == RIGHT_UP_p2:
            player2.vel_x -= RUN_SPEED_PPS

        elif event == LEFT_UP_p2:
            player2.vel_x += RUN_SPEED_PPS

        player2.acc_y = 0  # 중력은 없애준다

        # 위아래
        if event == DOWN_DOWN_p2:
            player2.vel_y = PLAYER_GRAVITY
            player2.vel_y -= 0.5
        elif event == DOWN_UP_p2:
            player2.vel_y = PLAYER_GRAVITY
            # player1.vel_y += 0.5
        elif event == UP_DOWN_p2:
            player2.vel_y = PLAYER_GRAVITY

            player2.vel_y += 0.5

        elif event == UP_UP_p2:
            player2.vel_y = PLAYER_GRAVITY
            # player1.vel_y -= 0.5

        player2.timer = 3000  # inBubbleState 지속시간
        player2.frame2 = 0

    @staticmethod
    def exit_p1(player1, event):
        # player1.timer = 0
        pass

    @staticmethod
    def exit_p2(player2, event):
        player2.timer = 0
        pass

    @staticmethod
    def do_p1(player1):
        global maintain
        # 플레이어1
        player1.frame1 = (player1.frame1 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        maintain -= 1
        # print(player1.vel_x, ' ', player1.vel_y)
        print(maintain)

        if maintain == 0:  # 만약에 일정 시간이 다 되면
            player1.acc_y = PLAYER_GRAVITY
            print(player1.vel_x)
            if player1.vel_x != 0.0 or player1.vel_y != 0.0:
                player1.cur_state = RunState
                # print('Runstate!') # 물방울에서 빠져나온다. -> Runstate로
            if player1.vel_x == 0.0 and player1.vel_y == 0.0:
                player1.cur_state = IdleState  # 물방울에서 빠져나온다. -> Idlestate로
                # print('idlestate돌아왔습니다')
            elif player1.vel_x != 0.0 and player1.vel_y > 0.0:  # 어쩔 수가 없음(보류)
                player1.cur_state = IdleState
            elif player1.vel_x == 0.0 and player1.vel_y < 0.0:
                player1.cur_state = IdleState

        player1.x += player1.vel_x * game_framework.frame_time
        player1.y += player1.vel_y
        player1.vel_y += player1.acc_y

        if player1.y > 550:
            player1.y = 550

    @staticmethod
    def do_p2(player2):
        # 플레이어2
        player2.frame2 = (player2.frame2 + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        player2.timer -= 1

        print(player2.timer)

        if player2.timer == 0:  # 만약에 일정 시간이 다 되면
            player2.acc_y = PLAYER_GRAVITY
            print(player2.vel_x)
            if player2.vel_x != 0.0 or player2.vel_y != 0.0:
                player2.cur_state = RunState
                print('Runstate!')  # 물방울에서 빠져나온다. -> Runstate로
            if player2.vel_x == 0.0 and player2.vel_y == 0.0:
                player2.cur_state = IdleState  # 물방울에서 빠져나온다. -> Idlestate로
                print('idlestate돌아왔습니다')
            elif player2.vel_x != 0.0 and player2.vel_y > 0.0:
                player2.cur_state = IdleState
            elif player2.vel_x == 0.0 and player2.vel_y < 0.0:
                player2.cur_state = IdleState

        player2.x += player2.vel_x * game_framework.frame_time
        player2.y += player2.vel_y
        player2.vel_y += player2.acc_y

        if player2.y > 550:
            player2.y = 550

    @staticmethod
    def draw_p1(player1):
        player1.in_bubble.clip_draw(int(player1.frame1) * 80, 80, 80, 80, player1.x, player1.y)
        player1.font.draw(player1.x - 60, player1.y + 50, '(Time: %3.2f)' % maintain, (255, 0, 0))

    @staticmethod
    def draw_p2(player2):
        player2.in_bubble.clip_draw(int(player2.frame2) * 80, 80, 80, 80, player2.x, player2.y)
        player2.font.draw(player2.x - 60, player2.y + 50, '(Time: %s)' % player2.timer, (255, 0, 0))


next_state_table = {
    IdleState: {RIGHT_UP_p1: RunState, LEFT_UP_p1: RunState,
                RIGHT_DOWN_p1: RunState, LEFT_DOWN_p1: RunState,
                UP_UP_p1: RunState, UP_DOWN_p1: RunState,
                BUBBLE_SHOT_p1: IdleState,
                BUBBLE_HIT: InBubbleState,
                DOWN_UP_p1: IdleState, DOWN_DOWN_p1: IdleState},
    RunState: {RIGHT_UP_p1: IdleState, LEFT_UP_p1: IdleState,
               LEFT_DOWN_p1: IdleState, RIGHT_DOWN_p1: IdleState,
               UP_UP_p1: IdleState, UP_DOWN_p1: IdleState,
               BUBBLE_SHOT_p1: RunState,
               BUBBLE_HIT: InBubbleState,
               DOWN_UP_p1: RunState, DOWN_DOWN_p1: RunState},
    InBubbleState: {RIGHT_UP_p1: InBubbleState, LEFT_UP_p1: InBubbleState,
                    LEFT_DOWN_p1: InBubbleState, RIGHT_DOWN_p1: InBubbleState,
                    UP_UP_p1: InBubbleState, UP_DOWN_p1: InBubbleState,
                    DOWN_UP_p1: InBubbleState, DOWN_DOWN_p1: InBubbleState}
}
next_state_table2 = {
    IdleState: {
        RIGHT_UP_p2: RunState, LEFT_UP_p2: RunState,
        RIGHT_DOWN_p2: RunState, LEFT_DOWN_p2: RunState,
        UP_UP_p2: RunState, UP_DOWN_p2: RunState,
        BUBBLE_SHOT_p2: IdleState,
        BUBBLE_HIT: InBubbleState,
        DOWN_UP_p2: IdleState, DOWN_DOWN_p2: IdleState},
    RunState: {
        RIGHT_UP_p2: IdleState, LEFT_UP_p2: IdleState,
        LEFT_DOWN_p2: IdleState, RIGHT_DOWN_p2: IdleState,
        UP_UP_p2: IdleState, UP_DOWN_p2: IdleState,
        BUBBLE_SHOT_p2: RunState,
        BUBBLE_HIT: InBubbleState,
        DOWN_UP_p2: RunState, DOWN_DOWN_p2: RunState}
}


class Player1:
    def __init__(self):
        self.x, self.y = (850, 600 / 2)
        self.vel_x, self.vel_y = 0, 0
        self.acc_x, self.acc_y = 0, PLAYER_GRAVITY
        self.frame1 = 0
        self.image = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\character.png')
        self.attack = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\attack_p1.png')
        self.in_bubble = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\in_bubble.png')
        self.font = load_font('ENCR10B.TTF', 16)

        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter_p1(self, None)
        self.dir = 1
        self.jumping = False
        self.sheet_line = 180
        self.isShot = False  # 어떻게 쓸 수 있을까 고민
        self.isHit = False  # 물발울에 맞았냐

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
        self.image.clip_draw(int(self.frame1) * 60, self.sheet_line, 60, 60, self.x, self.y)
        self.cur_state.draw_p1(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    # collide box
    def get_bb_green(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30


class Player2:
    def __init__(self):
        self.x, self.y = (50, 600 / 2)
        self.vel_x, self.vel_y = 0, 0
        self.acc_x, self.acc_y = 0, PLAYER_GRAVITY
        self.frame2 = 0
        self.image = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\character2.png')
        self.in_bubble = load_image('C:\\2017180012 jpark\\2017180012_2DGP_MyGame\\res\\in_bubble.png')

        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter_p2(self, None)
        self.dir = 1
        self.jumping = False
        self.sheet_line = 120
        self.isHit = False

    def bubble_shot(self):
        bubble2 = Bubble2(self.x, self.y, self.dir*3)  # 발사 시작 위치
        grass = Grass()  # grass 객체를 가져옴

        game_world.bubble2_objects.append(bubble2)

        if bubble2.y <= grass.y + 40:  # 물방울이 중력때문에 화면 밖으로 내려가지 않게 함
            bubble2.y = grass.y + 40

    # collide box
    def get_bb_blue(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

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
        self.image.clip_draw(int(self.frame2) * 60, self.sheet_line, 60, 60, self.x, self.y)
        self.cur_state.draw_p2(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table2:
            key_event2 = key_event_table2[(event.type, event.key)]
            self.add_event(key_event2)





