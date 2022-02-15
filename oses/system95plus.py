import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

global pro95plus
pro95plus = 20
unlocklevel = 15
# required system for code
requiredsystem = "95"
# required system that shows on the boot menu
requiredstring = "PB95"

def launch95plus(systemlevel, systembadge, systempro):
    clear()
    print('P r o g r e s s b a r  9 5  p l u s')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    beginMenu("95plus", systemlevel, systempro)
