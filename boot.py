from lang import langload
from saveloader import detectSave, detectSettings, loadSystemSave, loadSettingsSave
from rich import print as rprint
from clear import clear
from checkbadge import calculateBadge
from player import startup
from lang import langset
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

        xu = "system" + xobj.systemunlock
        xun = osArray.index(xu)
        xunlo = eval(osArray[xun]).system()
        xunlock = xunlo.unlocklevel

        startup(xobj.shortname, xlevel, xobj.prolevel, xbadge, xobj.startupstring, xobj.systemunlock, xunlock, settingsdict)

def boot():

    detectSave()
    detectSettings()

    langset()

    global settingsdict
    global lang
    settingsdict = loadSettingsSave()


    while True:
        clear()

        rprint(lang["Sparrow"])
        rprint(lang["Version"].format(version, compileDate))
        rprint(lang["DEV"])

        bmc = 1 # boot menu counter
        for x in osArray:
            xobj = eval(x).system()
            systemexists = loadSystemSave(xobj.shortname)
            if systemexists == False:
                rprint(lang["NotUnlock"].format(bmc, xobj.name, xobj.unlocklevel, xobj.requiredstring))
                bmc += 1
            else:
                systembadge = calculateBadge(systemexists, xobj.prolevel)
                print(str(bmc) + '. ' + xobj.name, systembadge)
                bmc += 1

        choice = input()
        if choice == "":
            print()
        elif choice == "credits":
            clear()
            rprint(lang["Credits"])
            print()
            rprint("[#ff0000]BurningInfern0[/#ff0000]")
            rprint("[#f5a623]gamingwithpivin[/#f5a623]")
            rprint("[#f8e71c]setapdede[/#f8e71c]")
            rprint("[#37d67a]5jiji[/#37d67a]")
            rprint("[#4a90e2]Dieguito0512[/#4a90e2]")
            rprint("[#50e3c2]SevenSixteen[/#50e3c2]")
            input()
        else:
            choice = int(choice) - 1
            loadSettings(choice)

boot()
