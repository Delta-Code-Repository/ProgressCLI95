import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

global promeme
promeme = 30
unlocklevel = 30
# required system for code
requiredsystem = "98"
# required system that shows on the boot menu
requiredstring = "PB98"

def launchmeme(systemlevel, systembadge, systempro):
    clear()
    print('P r o g r e s s b a r  M e m e')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    beginMenu("Meme", systemlevel, systempro)
