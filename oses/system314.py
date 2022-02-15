import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

global pro314
pro314 = 10
unlocklevel = "2p"
requiredsystem = ""
requiredstring = ""

def launch95(systemlevel, systembadge, systempro):
    clear()
    print('P r o g r e s s b a r  3 . 1 4')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    beginMenu("314", systemlevel, systempro)
