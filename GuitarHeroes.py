import pygame
import sys
import time
import random
import pyautogui

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
RESOLUTION = (WINDOW_WIDTH,WINDOW_HEIGHT)

GAME_SPEED = 60
CLOCK = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(RESOLUTION)

monospace = pygame.font.SysFont('monospace',18)

last = pygame.time.get_ticks()
SPAWN_EVERY = 320/2

LINE_POS = []
LINE_POINT = [0,500]
LINE_RED_Y = [500 for i in range(10)]

KEYS = [pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_f,pygame.K_g,pygame.K_h\
    ,pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_SPACE]
BUTTONS = ['a','s','d','f','g','h','j','k','l','space']

FPS = 0
cSec = 0
cFrame = 0

SCORE = 0

def Define_Line_POS():
    a = 0
    for i in range(10):
        LINE_POS.append(a)
        a += 50
Define_Line_POS()

class NOTES:
    NOTES_A = []
    NOTES_S = []
    NOTES_D = []
    NOTES_F = []
    NOTES_G = []
    NOTES_H = []
    NOTES_J = []
    NOTES_K = []
    NOTES_L = []
    NOTES_SPACE = []
class NOTE_COLLIDED:
    NOTE_COLLIDED_A = []
    NOTE_COLLIDED_S = []
    NOTE_COLLIDED_D = []
    NOTE_COLLIDED_F = []
    NOTE_COLLIDED_G = []
    NOTE_COLLIDED_H = []
    NOTE_COLLIDED_J = []
    NOTE_COLLIDED_K = []
    NOTE_COLLIDED_L = []
    NOTE_COLLIDED_SPACE = []

class Color:
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    DARK_GREY = (15,15,15)

def createRandomColor():
    r = random.randint(100,255)
    g = random.randint(100,255)
    b = random.randint(100,255)
    Col = (r,g,b)
    return Col
def Draw_Line():
    SELING = True
    for line in LINE_POS:
        if SELING == True:
            pygame.draw.rect(screen,Color.BLACK,(line,0,50,WINDOW_HEIGHT-100))
            SELING = False
        else:
            pygame.draw.rect(screen,Color.DARK_GREY,(line,0,50,WINDOW_HEIGHT-100))
            SELING = True
    pygame.draw.rect(screen,Color.BLACK,(LINE_POINT[0],LINE_POINT[1],WINDOW_WIDTH,WINDOW_HEIGHT-500))
    pygame.draw.rect(screen,Color.BLACK,(500,0,WINDOW_WIDTH-500,WINDOW_HEIGHT))
def Create_Notes(NOTES_DEFINER,LINE_POS_INDEX):
    NOTES_DEFINER.append([LINE_POS[LINE_POS_INDEX],0,createRandomColor()])
def Create_All_Notes():
    global last
    now = pygame.time.get_ticks()
    if now - last >= SPAWN_EVERY:
        last = now
        Notes_value = random.randint(0,9)
        if Notes_value == 0:
            Create_Notes(NOTES.NOTES_A,0)
        elif Notes_value == 1:
            Create_Notes(NOTES.NOTES_S,1)
        elif Notes_value == 2:
            Create_Notes(NOTES.NOTES_D,2)
        elif Notes_value == 3:
            Create_Notes(NOTES.NOTES_F,3)
        elif Notes_value == 4:
            Create_Notes(NOTES.NOTES_G,4)
        elif Notes_value == 5:
            Create_Notes(NOTES.NOTES_H,5)
        elif Notes_value == 6:
            Create_Notes(NOTES.NOTES_J,6)
        elif Notes_value == 7:
            Create_Notes(NOTES.NOTES_K,7)
        elif Notes_value == 8:
            Create_Notes(NOTES.NOTES_L,8)
        elif Notes_value == 9:
            Create_Notes(NOTES.NOTES_SPACE,9)
def Draw_Notes(NOTES_DEFINER):
    for note in NOTES_DEFINER:
        pygame.draw.rect(screen,note[2],(note[0],note[1],50,50))
def Draw_All_Notes():
    Draw_Notes(NOTES.NOTES_A)
    Draw_Notes(NOTES.NOTES_S)
    Draw_Notes(NOTES.NOTES_D)
    Draw_Notes(NOTES.NOTES_F)
    Draw_Notes(NOTES.NOTES_G)
    Draw_Notes(NOTES.NOTES_H)
    Draw_Notes(NOTES.NOTES_J)
    Draw_Notes(NOTES.NOTES_K)
    Draw_Notes(NOTES.NOTES_L)
    Draw_Notes(NOTES.NOTES_SPACE)
def Moving_Notes(NOTES_DEFINER):
    for note in NOTES_DEFINER:
        note[1] += 10
def Moving_All_Notes():
    Moving_Notes(NOTES.NOTES_A)
    Moving_Notes(NOTES.NOTES_S)
    Moving_Notes(NOTES.NOTES_D)
    Moving_Notes(NOTES.NOTES_F)
    Moving_Notes(NOTES.NOTES_G)
    Moving_Notes(NOTES.NOTES_H)
    Moving_Notes(NOTES.NOTES_J)
    Moving_Notes(NOTES.NOTES_K)
    Moving_Notes(NOTES.NOTES_L)
    Moving_Notes(NOTES.NOTES_SPACE)
def count_fps():
    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
    return FPS
def Draw_Note_Helper():
    text = [['A',20],['S',70],['D',120],['F',170],['G',220],['H',270],['J',320],['K',370],['L',420],['SPACE',450]]
    for word in text:
        screen.blit(monospace.render(word[0],True,(255,255,255)),(word[1],510))
def Draw_Label():
    text = 'Score : ' + str(SCORE)
    fps_text = 'FPS : ' + str(count_fps())
    label = monospace.render(text,True,(255,255,255))
    fps_label = monospace.render(fps_text,True,(255,255,255))
    screen.blit(label,(20,20))
    screen.blit(fps_label,(700,20))
    Draw_Note_Helper()
def collison(object_1,object_2):
	p_x = object_1[0]
	p_y = object_1[1]
	e_x = object_2[0]
	e_y = object_2[1]
	
	if (e_y >= p_y and e_y < (p_y + 20)) or (p_y >= e_y and p_y < (e_y + 20)):
		return True
	else:
		return False
def detectCollison(line,NOTES):
    global NOTE_COLLIDED
    for NOTE in NOTES:
        if collison(line,NOTE):
            NOTE_COLLIDED = NOTE
            return True
# def playerControl(NOTES,KEYS):
#     global SCORE
#     keystate = pygame.key.get_pressed()
#     if keystate[KEYS[0]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_A):
#             p = NOTES.NOTES_A.index(NOTE_COLLIDED)
#             NOTES.NOTES_A.pop(p)
#             SCORE += 10
#     if keystate[KEYS[1]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_S):
#             p = NOTES.NOTES_S.index(NOTE_COLLIDED)
#             NOTES.NOTES_S.pop(p)
#             SCORE += 10
#     if keystate[KEYS[2]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_D):
#             p = NOTES.NOTES_D.index(NOTE_COLLIDED)
#             NOTES.NOTES_D.pop(p)
#             SCORE += 10
#     if keystate[KEYS[3]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_F):
#             p = NOTES.NOTES_F.index(NOTE_COLLIDED)
#             NOTES.NOTES_F.pop(p)
#             SCORE += 10
#     if keystate[KEYS[4]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_G):
#             p = NOTES.NOTES_G.index(NOTE_COLLIDED)
#             NOTES.NOTES_G.pop(p)
#             SCORE += 10
#     if keystate[KEYS[5]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_H):
#             p = NOTES.NOTES_H.index(NOTE_COLLIDED)
#             NOTES.NOTES_H.pop(p)
#             SCORE += 10
#     if keystate[KEYS[6]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_J):
#             p = NOTES.NOTES_J.index(NOTE_COLLIDED)
#             NOTES.NOTES_J.pop(p)
#             SCORE += 10
#     if keystate[KEYS[7]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_K):
#             p = NOTES.NOTES_K.index(NOTE_COLLIDED)
#             NOTES.NOTES_K.pop(p)
#             SCORE += 10
#     if keystate[KEYS[8]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_L):
#             p = NOTES.NOTES_L.index(NOTE_COLLIDED)
#             NOTES.NOTES_L.pop(p)
#             SCORE += 10
#     if keystate[KEYS[9]]:
#         if detectCollison(LINE_POINT,NOTES.NOTES_SPACE):
#             p = NOTES.NOTES_SPACE.index(NOTE_COLLIDED)
#             NOTES.NOTES_SPACE.pop(p)
#             SCORE += 10
def playerControl(NOTES,KEYS):
    global SCORE
    keystate = pygame.key.get_pressed()
    if detectCollison(LINE_POINT,NOTES.NOTES_A):
        # Bot(BUTTONS[0])
        p = NOTES.NOTES_A.index(NOTE_COLLIDED)
        NOTES.NOTES_A.pop(p)
        SCORE += 10
        # if keystate[KEYS[0]]:
        #     p = NOTES.NOTES_A.index(NOTE_COLLIDED)
        #     NOTES.NOTES_A.pop(p)
        #     SCORE += 10
    if detectCollison(LINE_POINT,NOTES.NOTES_S):
        # Bot(BUTTONS[1])
        p = NOTES.NOTES_S.index(NOTE_COLLIDED)
        NOTES.NOTES_S.pop(p)
        SCORE += 10
        # if keystate[KEYS[1]]:
        #     p = NOTES.NOTES_S.index(NOTE_COLLIDED)
        #     NOTES.NOTES_S.pop(p)
        #     SCORE += 10
    if detectCollison(LINE_POINT,NOTES.NOTES_D):
        # Bot(BUTTONS[2])
        p = NOTES.NOTES_D.index(NOTE_COLLIDED)
        NOTES.NOTES_D.pop(p)
        SCORE += 10
        # if keystate[KEYS[2]]:
        #     p = NOTES.NOTES_D.index(NOTE_COLLIDED)
        #     NOTES.NOTES_D.pop(p)
        #     SCORE += 10
    if detectCollison(LINE_POINT,NOTES.NOTES_F):
        # Bot(BUTTONS[3])
        p = NOTES.NOTES_F.index(NOTE_COLLIDED)
        NOTES.NOTES_F.pop(p)
        SCORE += 10
        # if keystate[KEYS[3]]:
        #     p = NOTES.NOTES_F.index(NOTE_COLLIDED)
        #     NOTES.NOTES_F.pop(p)
        #     SCORE += 10
    if detectCollison(LINE_POINT,NOTES.NOTES_G):
        # Bot(BUTTONS[4])
        p = NOTES.NOTES_G.index(NOTE_COLLIDED)
        NOTES.NOTES_G.pop(p)
        SCORE += 10
        # if keystate[KEYS[4]]:
        #     p = NOTES.NOTES_G.index(NOTE_COLLIDED)
        #     NOTES.NOTES_G.pop(p)
        #     SCORE += 10
    if detectCollison(LINE_POINT,NOTES.NOTES_H):
        # Bot(BUTTONS[5])
        p = NOTES.NOTES_H.index(NOTE_COLLIDED)
        NOTES.NOTES_H.pop(p)
        SCORE += 10
        # if keystate[KEYS[5]]:
        #     p = NOTES.NOTES_H.index(NOTE_COLLIDED)
        #     NOTES.NOTES_H.pop(p)
        #     SCORE += 10
    if detectCollison(LINE_POINT,NOTES.NOTES_J):
        # Bot(BUTTONS[6])
        p = NOTES.NOTES_J.index(NOTE_COLLIDED)
        NOTES.NOTES_J.pop(p)
        SCORE += 10
        # if keystate[KEYS[6]]:
        #     p = NOTES.NOTES_J.index(NOTE_COLLIDED)
        #     NOTES.NOTES_J.pop(p)
        #     SCORE += 10
    if detectCollison(LINE_POINT,NOTES.NOTES_K):
        # Bot(BUTTONS[7])
        p = NOTES.NOTES_K.index(NOTE_COLLIDED)
        NOTES.NOTES_K.pop(p)
        SCORE += 10
        # if keystate[KEYS[7]]:
        #     p = NOTES.NOTES_K.index(NOTE_COLLIDED)
        #     NOTES.NOTES_K.pop(p)
        #     SCORE += 10
    if detectCollison(LINE_POINT,NOTES.NOTES_L):
        # Bot(BUTTONS[8])
        p = NOTES.NOTES_L.index(NOTE_COLLIDED)
        NOTES.NOTES_L.pop(p)
        SCORE += 10
        # if keystate[KEYS[8]]:
        #     p = NOTES.NOTES_L.index(NOTE_COLLIDED)
        #     NOTES.NOTES_L.pop(p)
        #     SCORE += 10
    if detectCollison(LINE_POINT,NOTES.NOTES_SPACE):
        # Bot(BUTTONS[9])
        p = NOTES.NOTES_SPACE.index(NOTE_COLLIDED)
        NOTES.NOTES_SPACE.pop(p)
        SCORE += 10
        # if keystate[KEYS[9]]:
        #     p = NOTES.NOTES_SPACE.index(NOTE_COLLIDED)
        #     NOTES.NOTES_SPACE.pop(p)
        #     SCORE += 10
def DRAW_LINE_POINT():
    pygame.draw.rect(screen,Color.WHITE,(LINE_POINT[0],LINE_POINT[1],500,3))

last2 = pygame.time.get_ticks()
def main():
    while True:
        CLOCK.tick(GAME_SPEED)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        Draw_Line()
        Create_All_Notes()
        Draw_All_Notes()
        DRAW_LINE_POINT()
        Draw_Label()
        playerControl(NOTES,KEYS)
        Moving_All_Notes()

        pygame.display.update()
if __name__ == "__main__":
    main()