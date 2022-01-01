from saveloader import detectSave, loadSystemSave
from termcolor import colored
from clear import clear
from checkbadge import calculateBadge
import sys

# system pros
global pro95
global pro95plus

pro95 = 10
pro95plus = 20

# systems
sys.path.insert(0, './oses/')

def startup(system):
    from system95 import launch95
    from system95plus import launch95plus
    if system == "1":
        level95 = loadSystemSave("95")
        badge95 = calculateBadge(level95, pro95)
        launch95(level95, badge95, pro95)
    elif system == "2":
        plus95check = loadSystemSave("95plus")
        badge95plus = calculateBadge(plus95check, pro95plus)
        if plus95check == False:
            boot()
        else:
            launch95plus(plus95check, badge95plus, pro95plus)

def boot():

    detectSave()

    global currentSystem

    # fancy bios text
    energyStar = colored('Energy Star Powered', "yellow")

    clear()
    print('Sparrow Assistant Enhanced Text BIOS.80.1 -', energyStar)
    print('Ver. 12-30-2021\n\n')

    ninefive = loadSystemSave("95")
    ninefivebadge = calculateBadge(ninefive, pro95)
    print('1. Progressbar 95', ninefivebadge)

    ninefiveplus = loadSystemSave("95plus")
    if ninefiveplus == False:
        print(colored('2. Progressbar 95 Plus - Get to level 15 in PB95 to unlock this!', "red"))
    else:
        ninefiveplusbadge = calculateBadge(ninefiveplus, pro95plus)
        print('2. Progressbar 95 Plus', ninefiveplusbadge)

    choice = input()
    startup(choice)

boot()
