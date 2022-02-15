import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

global proxb
proxb = 40
unlocklevel = 40
# required system for code
requiredsystem = "2000"
# required system that shows on the boot menu
requiredstring = "PB2000"

def launchxb(systemlevel, systembadge, systempro):
    clear()
    print('P r o g r e s s b a r  X B')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(5)
    beginMenu("xb", systemlevel, systempro)
