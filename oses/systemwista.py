import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

global prowista
prowista = 40
unlocklevel = 50
# required system for code
requiredsystem = "XB"
# required system that shows on the boot menu
requiredstring = "PBXB"

# How about some uniqueness to these things? I can just do these by copypasting them.
# Just a suggestion.
def launchwista(systemlevel, systembadge, systempro):
    clear()
    print('P r o g r e s s b a r  W i s t a')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(6)
    beginMenu("wista", systemlevel, systempro)
