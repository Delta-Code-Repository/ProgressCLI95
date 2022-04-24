from saveloader import detectSave, loadSystemSave
from rich import print as rprint
from clear import clear
from checkbadge import calculateBadge
from player import startup
import sys
import os
import random

# no touchy!!!
version = "0.2.2b-dev1"
compileDate = "04-24-2022"

# find systems and generate list
pathToOses = './oses/'
sys.path.insert(0, pathToOses)
osesDir = os.listdir(pathToOses)

# sanitize list
osArrayUnsorted = []
for x in osesDir:
    if x == "__pycache__":
        continue
    else:
        x = x.replace('.py', '')
        osArrayUnsorted.append(x)

# import systems
for x in osArrayUnsorted:
    globals()[x] = __import__(x)

# sort array into new array (this is probably inefficient but whatever)
finished = False
arrayCounter = 0
osArray = []
while finished == False:
    arraySelect = random.randrange(0, len(osArrayUnsorted))
    xobj = eval(osArrayUnsorted[arraySelect]).system()
    if xobj.listinbootmenu == arrayCounter:
        osArray.append(osArrayUnsorted[arraySelect])
        osArrayUnsorted.pop(arraySelect)
        arrayCounter +=1
    else:
        continue

    if len(osArrayUnsorted) == 0:
        finished = True

def loadSettings(system):
    xsys = osArray[system]
    xobj = eval(xsys).system()
    x = loadSystemSave(xobj.shortname)
    if x == False:
        print()
    else:
        xlevel = x
        xbadge = calculateBadge(xlevel, xobj.prolevel)
        startup(xobj.shortname, xlevel, xobj.prolevel, xbadge, xobj.startupstring)

def boot():

    detectSave()

    while True:
        clear()

        rprint('[white]Sparrow Assistant Enhanced Text BIOS.[not bold]80.1[/not bold][/white] - [bright_yellow]Energy Star (un)Powered[/bright_yellow]')
        rprint('[white]CLI ver. [bold]{0}[/bold] - compiled {1}[/white]\n\n'.format(version, compileDate))

        bmc = 1 # boot menu counter
        for x in osArray:
            xobj = eval(x).system()
            systemexists = loadSystemSave(xobj.shortname)
            if systemexists == False:
                rprint('[red][not bold]{0}[/not bold]. [not bold]{1}[/not bold] - Get to level {2} in {3} to unlock this![/red]'.format(bmc, xobj.name, xobj.unlocklevel, xobj.requiredstring))
                bmc += 1
            else:
                systembadge = calculateBadge(systemexists, xobj.prolevel)
                print(str(bmc) + '. ' + xobj.name + systembadge)
                bmc += 1

        choice = input()
        if choice == "":
            print()
        else:
            choice = int(choice) - 1
            loadSettings(choice)

boot()
