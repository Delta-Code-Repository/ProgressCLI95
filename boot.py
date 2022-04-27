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
version = "0.2.2b-dev2"
compileDate = "04-27-2022"

# find systems and generate list
pathToOses = './oses/'
sys.path.insert(0, pathToOses)
sys.path.insert(0, './lang/')
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

        if hasattr(xobj, "systemunlock"):
            xu = "system" + xobj.systemunlock
            xun = osArray.index(xu)
            xunlo = eval(osArray[xun]).system()
            xunlock = xunlo.unlocklevel
            xsystem = xobj.systemunlock
        else:
            xsystem = False
            xunlock = False

        startup(xobj.shortname, xlevel, xobj.prolevel, xbadge, xobj.startupstring, xsystem, xunlock)

def boot():

    langobj = loadSettingsSave("lang")
    if langobj == False:
        langobj = langset()
    try:
        globals()[langobj] = __import__(langobj)
    except:
        langobj = "en_US"
        globals()["en_US"] = __import__("en_US")

    detectSettings()
    detectSave()

    global lang
    lang = eval(langobj).language()

    while True:
        clear()

        rprint(lang.sparrow)
        rprint(lang.version.format(version, compileDate))
        rprint(lang.dev)

        bmc = 1 # boot menu counter
        for x in osArray:
            xobj = eval(x).system()
            systemexists = loadSystemSave(xobj.shortname)
            if systemexists == False:
                rprint(lang.notUnlocked.format(bmc, xobj.name, xobj.unlocklevel, xobj.requiredstring))
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
            rprint(lang.credits1)
            print()
            rprint("[#af005f]BurningInfern0[/#af005f]")
            rprint("[#fff400]gamingwithpivin[/#fff400]")
            rprint("[#6530ff]setapdede[/#6530ff]")
            rprint("[#2fda00]5jiji[/#2fda00]")
            rprint("[#edaf58]Dieguito0512[/#edaf58]")
            rprint("[#d5e7ae]SevenSixteen[/#d5e7ae]")
            print()
            rprint(lang.credits2)
            rprint("🇺🇸 American English (en_US) - [#af005f]BurningInfern0[/#af005f]")
            rprint("🇵🇱 Polish (pl_PL) - [#fff400]gamingwithpivin[/#fff400]")
            rprint("🇷🇴 Romanian (ro_RO) - [#6530ff]setapdede[/#6530ff], [#ff5045]AlexandruUnu[/#ff5045]")
            rprint("🇫🇷 French (fr_FR) - [#2fda00]5jiji[/#2fda00]")
            rprint("🇧🇷 Brazilian Portuguese (pt_BR) - [#1462d9]Luihum[/#1462d9]")
            rprint("🇮🇹 Italian (it_IT) - [#00459b]Christian230102[/#00459b]")
            rprint("🇧🇬 Bulgarian (bg_BG) - [#8a2be2]markverb1[/#8a2be2]")
            rprint("🇹🇷 Turkish (tr_TR) - [#8cc443]UstaYussuf[/#8cc443]")
            rprint("🇻🇪 Spanish (es_VE) - [#7289da]elThomas54[/#7289da]")
            print()
            input()
        elif choice == "chlang":
            langobj = langset()
            globals()[langobj] = __import__(langobj)
            lang = eval(langobj).language()
        else:
            choice = int(choice) - 1
            loadSettings(choice)

boot()
