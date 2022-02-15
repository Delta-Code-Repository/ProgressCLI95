import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

global pro95
pro95 = 10
unlocklevel = 0
requiredsystem = ""
requiredstring = ""

def launch95(systemlevel, systembadge, systempro):
    clear()
    print('P r o g r e s s b a r  9 5')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    beginMenu("95", systemlevel, systempro)
