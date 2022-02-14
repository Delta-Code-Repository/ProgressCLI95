from saveloader import detectSave, loadSystemSave
from termcolor import colored
from clear import clear
from checkbadge import calculateBadge
from time import sleep
import sys
from mod import systemList, proList
from player import startGame, beginMenu, pauseBeginMenu

# systems
sys.path.insert(0, './oses/')

def launch(systemOS, systemlevel, systembadge, systempro):
    clear()
    print(" ".join(systemOS))
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    repi = systemOS.replace("Progressbar", "")
    beginMenu(repi, systemlevel, systempro)

def startup(system):
    from system95 import launch95
    from system95plus import launch95plus
    from system98 import launch98
    from systemmeme import launchmeme
    from system2000 import launch2000
    stri = systemList[int(system) - 1]
    repi = stri.replace("Progressbar", "")
    level = loadSystemSave(repi)
    pro = proList[int(system) - 1]
    badge = calculateBadge(level, pro)
    if level == False and int(system) > 1:
        boot()
    launch(stri, level, badge, pro)
def boot():

    detectSave()

    global currentSystem

    # fancy bios text
    energyStar = colored('Energy Star Powered', "yellow")

    clear()
    print('Sparrow Assistant Enhanced Text BIOS.80.1 -', energyStar)
    print('Ver. 12-30-2021\n\n')
    for i in range(len(systemList)):
        stri = systemList[i]
        stri1 = systemList[i - 1]
        repi = stri.replace("Progressbar", "")
        save = loadSystemSave(repi)
        if save == False and i > 0:
            print(colored(f"{i + 1}. {stri} - Get to level {proList[i - 1]} in {stri1} to unlock this!", "red"))
        else:
            badge = calculateBadge(save, proList[i])
            print(f"{i + 1}. {stri}", badge)

    choice = input()
    startup(choice)

boot()
