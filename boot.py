from saveloader import detectSave, loadSystemSave
from rich import print as rprint
from clear import clear
from checkbadge import calculateBadge
from time import sleep
import sys
from mod import systemList, proList
from player import startGame, beginMenu, pauseBeginMenu

# compressed code helps make game much more expandable/moddable

# systems
sys.path.insert(0, './oses/')

def launch(systemOS, systemlevel, systembadge, systempro):
    clear()
    print(" ".join(systemOS))
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    repi = systemOS.replace("Progressbar ", "")
    beginMenu(repi, systemlevel, systempro)

def startup(system):
    # string from mod.py
    stri = systemList[int(system) - 1]
    # for saving
    repi = stri.replace("Progressbar", "")
    # originally "level95", "check95plus", etc
    level = loadSystemSave(repi)
    # removes "necessity" for each os to have a separate pro variable, mod.py
    pro = proList[int(system) - 1]
    # originally "badge95", etc
    badge = calculateBadge(level, pro)
    if level == False and int(system) > 1:
        boot()
    launch(stri, level, badge, pro)
def boot():

    detectSave()

    global currentSystem

    clear()
    rprint('Sparrow Assistant Enhanced Text BIOS.80.1 - [bright_yellow]Energy Star Powered[/bright_yellow]')
    print('Ver. 12-30-2021\n\n')
    for i in range(len(systemList)):
        stri = systemList[i]
        stri1 = systemList[i - 1]
        repi = stri.replace("Progressbar", "")
        save = loadSystemSave(repi)
        if save == False and i > 0:
            rprint(f'[red]{i}. {stri} - Get to level {proList[i - 1]} in {stri1} to unlock this![/red]')
        else:
            badge = calculateBadge(save, proList[i])
            print(f"{i + 1}. {stri}", badge)

    choice = input()
    startup(choice)

boot()
