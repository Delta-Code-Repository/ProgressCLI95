import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

global pro2000
pro2000 = 30
unlocklevel = 30
# required system for code
requiredsystem = "Meme"
# required system that shows on the boot menu
requiredstring = "PBMeme"

def launch2000(systemlevel, systembadge, systempro):
    clear()
    print('P r o g r e s s b a r  2 0 0 0')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(5)
    beginMenu("2000", systemlevel, systempro)
