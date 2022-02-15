from saveloader import detectSave, loadSystemSave
from rich import print as rprint
from clear import clear
from checkbadge import calculateBadge
import sys

# no touchy!!!
version = "0.2.2b-dev1"
compileDate = "02-15-2022"

# find systems
sys.path.insert(0, './oses/')

# import systems
import system95
import system95plus
import system98
import systemmeme
import system2000
import systemxb
import systemwista

def startup(system):
    if system == "1":
        level314 = loadSystemSave("314")
        badge314 = calculateBadge(level314, system314.pro314)
        system314.launch314(level314, badge314, system314.pro314)
    elif system == "2":
        level95 = loadSystemSave("95")
        badge95 = calculateBadge(level95, system95.pro95)
        system95.launch95(level95, badge95, system95.pro95)
    elif system == "3":
        plus95check = loadSystemSave("95plus")
        badge95plus = calculateBadge(plus95check, system95plus.pro95plus)
        if plus95check == False:
            boot()
        else:
            system95plus.launch95plus(plus95check, badge95plus, system95plus.pro95plus)
    elif system == "4":
        check98 = loadSystemSave("98")
        badge98 =  calculateBadge (check98, system98.pro98)
        if check98 == False:
            boot()
        else:
            system98.launch98(check98, badge98, system98.pro98)
    elif system == "5":
        checkmeme = loadSystemSave("Meme")
        badgememe =  calculateBadge (checkmeme, systemmeme.promeme)
        if checkmeme == False:
            boot()
        else:
            systemmeme.launchmeme(checkmeme, badgememe, systemmeme.promeme)
    elif system == "6":
        check2000 = loadSystemSave("2000")
        badge2000 =  calculateBadge (check2000, system2000.pro2000)
        if check2000 == False:
            boot()
        else:
            system2000.launch2000(check2000, badge2000, system2000.pro2000)
    elif system == "7":
        checkxb = loadSystemSave("xb")
        badgexb =  calculateBadge(checkxb, systemxb.proxb)
        if checkxb == False:
            boot()
        else:
            systemxb.launchxb(checkxb, badgexb, systemxb.proxb)
    elif system == "8":
       checkwista = loadSystemSave("wista")
       badgewista = calculateBadge(checkwista, systemwista.prowista)
       if checkwista == False:
          boot()
       else:
           systemwista.launchwista(checkwista, badgewista, systemwista.prowista)

def boot():

    detectSave()

    global currentSystem

    clear()
    # btw pivin fucking work on sparrow
    # it's just a decision tree, isn't too hard.
    # or at least sounds easy.
    rprint('[white]Sparrow Assistant Enhanced Text BIOS.[not bold]80.1[/not bold][/white] - [bright_yellow]Energy Star (un)Powered[/bright_yellow]')
    rprint('[white]CLI ver. [bold]{0}[/bold] - compiled {1}[/white]\n\n'.format(version, compileDate))

    # PROGRESSBAR 3.14
    threeonefour = loadSystemSave("314")
    if threeonefour == False:
        rprint('[red][not bold]1[/not bold]. Progressbar [not bold]3.14[/not bold] - Get two pro badges to unlock this![/red]')
    else:
        threeonefourbadge = calculateBadge(threeonefourplus, system314.pro314)
        print('2. Progressbar 3.14', threeonefourbadge)

    # PROGRESSBAR 95
    ninefive = loadSystemSave("95")
    ninefivebadge = calculateBadge(ninefive, system95.pro95)
    print('2. Progressbar 95', ninefivebadge)

    # PROGRESSBAR 95 PLUS
    ninefiveplus = loadSystemSave("95plus")
    if ninefiveplus == False:
        rprint('[red][not bold]3[/not bold]. Progressbar [not bold]95[/not bold] Plus - Get to level {0} in {1} to unlock this![/red]'.format(system95plus.unlocklevel, system95plus.requiredstring))
    else:
        ninefiveplusbadge = calculateBadge(ninefiveplus, system95plus.pro95plus)
        print('2. Progressbar 95 Plus', ninefiveplusbadge)

    # PROGRESSBAR 98
    nineeight = loadSystemSave("98")
    if nineeight == False:
        rprint('[red][not bold]4[/not bold]. Progressbar [not bold]98[/not bold] - Get to level {0} in {1} to unlock this![/red]'.format(system98.unlocklevel, system98.requiredstring))
    else:
        nineeightbadge = calculateBadge(nineeight, system98.pro98)
        print ('3. Progressbar 98', nineeightbadge)

    # PROGRESSBAR MEME
    meme = loadSystemSave("Meme")
    if meme == False:
        rprint('[red][not bold]5[/not bold]. Progressbar Meme - Get to level {0} in {1} to unlock this![/red]'.format(systemmeme.unlocklevel, systemmeme.requiredstring))
    else:
        memebadge = calculateBadge(meme, systemmeme.promeme)
        print ('4. Progressbar Meme', memebadge)

    # PROGRESSBAR 2000
    twok = loadSystemSave("2000")
    if twok == False:
        rprint('[red][not bold]6[/not bold]. Progressbar [not bold]2000[/not bold] - Get to level {0} in {1} to unlock this![/red]'.format(system2000.unlocklevel, system2000.requiredstring))
    else:
        twokbadge = calculateBadge(twok, system2000.pro2000)
        print ('5. Progressbar 2000', twokbadge)

    # PROGRESSBAR XB
    xb = loadSystemSave("xb")
    if xb == False:
        rprint('[red][not bold]7[/not bold]. Progressbar XB - Get to level {0} in {1} to unlock this![/red]'.format(systemxb.unlocklevel, systemxb.requiredstring))
    else:
        xbbadge = calculateBadge(xb, systemxb.proxb)
        print ('6. Progressbar XB', xbbadge)

    # PROGRESSBAR WISTA
    wista = loadSystemSave("Wista")
    if wista == False:
        rprint('[red][not bold]8[/not bold]. Progressbar Wista - Get to level {0} in {1} to unlock this![/red]'.format(systemwista.unlocklevel, systemwista.requiredstring))
    else:
         wistabadge = calculateBadge(wista, systemwista.prowista)
         print('7. Progressbar Wista (INCOMPLETE)', wistabadge)

    choice = input()
    startup(choice)

boot()
