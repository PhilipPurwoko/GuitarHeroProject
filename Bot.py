import pyautogui
import time
from GuitarHeroes import NOTES

class Delayer:
	def __init__(self,second):
		self.second = second
	def start(self):
		lister = [i for i in range(self.second)]
		lister.sort(reverse=True)
		for i in lister:
			print('Locking mouse position in {}'.format(i+1))
			time.sleep(1)
		print('Position Locked. Dont move')
def DefineColor():
    global LINES,COLORS
    mouse = pyautogui.position()
    for INDEX in range(10):
        LINES[INDEX] = [int(mouse[0]) + (50*INDEX),mouse[1]]
        COLORS[INDEX] = pyautogui.pixel(LINES[INDEX][0],mouse[1])
    print(COLORS)
    
Delay = Delayer(3)
Delay.start()

LINES = [i for i in range(10)]
COLORS = [i for i in range(10)]
COLORS_NOW = [i for i in range(10)]
BUTTONS = ['a','s','d','f','g','h','j','k','l','space']

DefineColor()

# while 1:
#     for INDEX in range(10):
#         COLORS_NOW[INDEX] = pyautogui.pixel(LINES[INDEX][0],LINES[INDEX][1])
#         if COLORS_NOW[INDEX] != COLORS[INDEX]:
#             # print('COLOR INDEX {} CHANGE'.format(INDEX))
#             pyautogui.keyDown(BUTTONS[INDEX])
#             pyautogui.keyUp(BUTTONS[INDEX])
#     print(COLORS_NOW)
print(NOTES)