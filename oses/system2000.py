import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

def launch2000(systemlevel, systembadge, systempro, settingsdict):
    clear()
    print('P r o g r e s s b a r  2 0 0 0')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(5)
    beginMenu("2000", systemlevel, systempro, settingsdict)
