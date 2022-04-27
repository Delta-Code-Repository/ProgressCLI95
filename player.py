from clear import clear
from rich import print as rprint
from rich.table import Table
from time import sleep
import random
from saveloader import editSystemSave, editSettingsFile, addSystemSave, loadSettingsSave
from checkbadge import calculateBadge

def startup(system, systemlevel, systempro, systembadge, systemlogo, systemunlock, systemunlocklevel):
    langobj = loadSettingsSave("lang")
    globals()[langobj] = __import__(langobj)
    global lang
    lang = eval(langobj).language()

    global unlock
    global unlocklevel

    unlock = systemunlock
    unlocklevel = systemunlocklevel

    clear()
    print('P r o g r e s s b a r ', systemlogo)
    print(systembadge)
    print(lang.loading)
    sleep(5)

    generateTables()
    beginMenu(system, systemlevel, systempro)

def generateTables():
    global bm1table
    global bm2table
    global bm3table
    global aptable
    global sett

    # begin menu table with no load game
    bm1table = Table()
    bm1table.add_column(lang.bm1)
    bm1table.add_row("1."+lang.bm2)
    bm1table.add_row("2."+lang.bm6)
    bm1table.add_row("3."+lang.bm4)
    bm1table.add_row("4."+lang.bm5)

    # begin menu table with load game
    bm2table = Table()
    bm2table.add_column(lang.bm1)
    bm2table.add_row("1."+lang.bm3)
    bm2table.add_row("2."+lang.bm2)
    bm2table.add_row("3."+lang.bm6)
    bm2table.add_row("4."+lang.bm4)
    bm2table.add_row("5."+lang.bm5)

    # paused begin menu
    bm3table = Table()
    bm3table.add_column(lang.bm1)
    bm3table.add_row("1."+lang.bm7)
    bm3table.add_row("2."+lang.bm2)
    bm3table.add_row("3."+lang.bm4)
    bm3table.add_row("4."+lang.bm5)

    # annoying popup
    aptable = Table()
    aptable.show_header = False
    aptable.add_column("Annoying popup!")
    aptable.add_row(lang.annoyingPopup)
    aptable.add_row("       [OK]", style="bold bright_black")

    sett = Table()
    sett.add_column(lang.sett1)
    sett.add_row("1."+lang.sett2)
    sett.add_row("2."+lang.sett3)

def screenDownFun():
    # checks if you have orange segments in your bar
    if progressbar2 > 0:
        print(lang.bar, end='')
        for segment in bar2:
            if segment == "Blue":
                rprint("[blue][][/blue]", end='')
            elif segment == "Orange":
                rprint("[bright_yellow][][/bright_yellow]", end='')
        print(lang.barProgress1.format(progressbar, progressbar2))
    else:
        print(lang.bar, end='')
        for segment in bar2:
            if segment == "Blue":
                rprint("[blue][][/blue]", end='')
            elif segment == "Pink":
                rprint("[bright_magenta][][/bright_magenta]", end='')
        print(lang.barProgress2.format(progressbar))

def settings(systemname, systemlevel, systempro):
    clear()
    rprint(sett)
    choise = input("> ")
    if choise == "1":
        clear()
        print(lang.doYouWant)
        rprint(lang.bar, " [blue][][][][][][][][][][][][][][][][][][][][/blue]")
        print(lang.barProgressP1, " 95% ",lang.inYourBar)
        print(lang.popupSetting)
        choice = input("> ")
        if choice == "Y" or choice =="y":
            editSettingsFile("screenDown", "True")
            settings(systemname, systemlevel, systempro)
        elif choice == "N" or choice == "n":
            editSettingsFile("screenDown", "False")
            settings(systemname, systemlevel, systempro)
        else:
            settings(systemname, systemlevel, systempro)
    elif choise == "2":
        beginMenu(systemname, systemlevel, systempro)
    else:
        settings(systemname, systemlevel, systempro)

# shutdown woohoo
def shutdown():
    clear()
    print(lang.wait)
    sleep(3)
    rprint(lang.closeCMD)
    sleep(2)
    quit()

def restart():
    clear()
    print(lang.wait)
    sleep(3)
    from boot import boot
    boot()

# Begin menu normally
def beginMenu(systemname, systemlevel, systempro):
    clear()
    if systemlevel > 1:
        rprint(bm2table)
    else:
        rprint(bm1table)
    choice = input("> ")
    if choice == "1":
        if systemlevel > 1:
            startGame(systemname, systemlevel, systempro)
        else:
            editSystemSave(systemname, 1)
            startGame(systemname, 1, systempro)
    elif choice == "2":
        if systemlevel > 1:
            editSystemSave(systemname, 1)
            startGame(systemname, 1, systempro)
        else:
            settings(systemname, systemlevel, systempro)
    elif choice == "3":
        if systemlevel > 1:
            settings(systemname, systemlevel, systempro)
        else:
            restart()
    elif choice == "4":
        if systemlevel > 1:
            restart()
        else:
            shutdown()
    elif choice == "5":
        if systemlevel > 1:
            shutdown()
    else:
        beginMenu(systemname, systemlevel, systempro)


# Begin menu during gameplay
def pauseBeginMenu(systemName, systemPro):
    clear()
    rprint(bm3table)
    choice = input()
    if choice == "1":
        return
    elif choice == "2":
        editSystemSave(systemName, 1)
        startGame(systemName, 1, systemPro)
    elif choice == "3":
        restart()
    elif choice == "4":
        shutdown()
    else:
        pauseBeginMenu(systemName, systemPro)

# original code by Setapdede, but i refined it a bit.
def spawnPopup(startLevel, systemLabel):
    clear()
    print('Level', startLevel)
    if systemLevel > 0:
        print('<', systemLabel, '>')
    rprint(aptable)
    popupinput = input()
    if popupinput == "OK":
        clear()
    elif popupinput == "ok":
        clear()
    else:
        spawnPopup(startLevel, systemLabel)

def startGame(systemName, startLevel, proLevel):
    global progressbar # total progressbar progress
    global progressbar2 # total orange segments in progressbar
    global progressbar3 # total pink segments in progressbar
    global lives
    global score
    global bar # array that contains segments for the progressbar
    global bar2 # contents in bar that are used to calculate pink segments
    global bardisplay # bar[] contents are displayed on screen
    global segments # used in conjunction with bardisplay
    global systemLabel # current system label
    global systemLevel # current system level (used with systemLabel)

    # setting global variables
    progressbar = 0
    progressbar2 = 0
    progressbar3 = 0
    lives = 3
    score = 0
    bar = []
    bar2 = []
    bardisplay = ""
    segments = ""

    systemLabel = calculateBadge(startLevel, proLevel)

    if systemLabel == "What?":
        systemLevel = 6
    elif systemLabel == "Grand":
        systemLevel = 5
    elif systemLabel == "Adept":
        systemLevel = 4
    elif systemLabel == "Master":
        systemLevel = 3
    elif systemLabel == "Expert":
        systemLevel = 2
    elif systemLabel == "Pro":
        systemLevel = 1
    else:
        systemLevel = 0

    while True:
        # clears the screen for next segment
        clear()

        # checks if lives are 0, breaks if true
        if lives == 0:
            rprint(lang.outOfLives)
            if startLevel == 1:
                rprint(lang.noLevelTaken)
            else:
                startLevel -= 1
                rprint(lang.negateLevel)
                editSystemSave(systemName, startLevel)
            lives = 3
            sleep(3)
            clear()

        popupshow = random.randint(0, 6)
        if popupshow == 6:
            spawnPopup(startLevel, systemLabel)

        print(lang.level, startLevel)
        if systemLevel > 0:
            print('<', systemLabel, '>')

        # randomly chooses a segment and loads art
        seg = random.randint(0, 5)
        if seg == 0:
            rprint("[blue]╔══╗\n║  ║\n║  ║\n╚══╝[/blue]")
        elif seg == 1:
            rprint("[bright_red]╔══╗\n║!!║\n║!!║\n╚══╝[/bright_red]")
        elif seg == 2:
            rprint("[bright_magenta]╔══╗\n║--║\n║--║\n╚══╝[/bright_magenta]")
        elif seg == 3:
            rprint("[bright_yellow]╔══╗\n║~~║\n║~~║\n╚══╝[/bright_yellow]")
        elif seg == 4:
            rprint("[bright_black]╔══╗\n║..║\n║..║\n╚══╝[/bright_black]")
        elif seg == 5:
            rprint("[bright_cyan]╔══╗\n║**║\n║**║\n╚══╝[/bright_cyan]")

        # green segment check
        greenseg = random.randint(0, 250)
        if greenseg == 95:
            clear()
            print('Level', startLevel)
            if systemLevel > 0:
                print('<', systemLabel, '>')
            seg = 6
            rprint("[bright_green]╔══╗\n║$$║\n║$$║\n╚══╝[/bright_green]")

        # checks if you have 1 life left
        if lives == 1:
            rprint(lang.oneLifeLeft)
        else:
            print(lang.livesLeft.format(lives))

        screenDownFun()

        # catches the currently displayed segment
        catch = input(lang.pressInstructions)

        # calculates which segment you caught and does stuff
        if seg == 0 and catch == "c":
            progressbar = progressbar + 5
            bar2.append("Blue")
            score = score + 5
        elif seg == 1 and catch == "c":
            bar = []
            bar2 = []
            bardisplay = ""
            lives = lives - 1
            progressbar = 0
            progressbar2 = 0
            progressbar3 = 0
            score = score - 10
        elif seg == 2 and catch == "c":
            if progressbar == 0:
                progressbar3 += 5
                progressbar += 5
                bar2.append("Pink")
            elif bar2[-1] == "Pink":
                progressbar3 += 5
                progressbar += 5
                bar2.append("Pink")
            elif bar2[-1] == "Orange":
                progressbar2 = progressbar2 - 5
                progressbar = progressbar - 5
                bar2.pop(-1)
                score = score + 5
            else:
                progressbar = progressbar - 5
                bar2.pop(-1)
                score + score - 5
        elif seg == 3 and catch == "c":
            progressbar = progressbar + 5
            progressbar2 = progressbar2 + 5
            bar2.append("Orange")
        elif seg == 4 and catch == "c":
            continue
        elif seg == 5 and catch == "c":
            bonus = random.randint(0, 1)
            if bonus == 0:
                progressbar = progressbar + 10
                bar2.append("Blue")
                bar2.append("Blue")
                score = score + 10
            else:
                progressbar = progressbar + 15
                bar2.append("Blue")
                bar2.append("Blue")
                bar2.append("Blue")
                score = score + 15
        elif seg == 6 and catch == "c":
            progressbar = 100
            progressbar2 = 0
            score = score + 100
        if catch == "c" and progressbar3 > 0 and not seg == 2:
            bar = []
            bar2 = []
            progressbar = 0
            progressbar2 = 0
            progressbar3 = 0

        if catch == "q":
            print(lang.gameOver)
            sleep(3)
            beginMenu(systemName, startLevel, proLevel)

        if catch == "beginmenu":
            pauseBeginMenu(systemName, proLevel)

        # if you have 100% on your progressbar, the game will end.
        if progressbar >= 100:

            # bonuses
            if progressbar2 > 0:
                print(lang.gameBravo)
            elif progressbar == 100 and progressbar2 == 0 and progressbar3 == 0:
                print(lang.gamePerfect)
            elif progressbar > 100:
                print(lang.gameOuterSpace)
            elif progressbar3 == 100:
                print (lang.magicPink)
            if progressbar == 50 and progressbar2 == 50:
                print (lang.gameYinAndYang)

            if progressbar == 0 and progressbar2 == 100:
                print (lang.gameNonconformist)

            
            # increment level count
            startLevel += 1
            editSystemSave(systemName, startLevel)

            # system unlock check section
            if unlocklevel == False:
                print()
            elif startLevel == unlocklevel:
                rprint(lang.newSystem)
                addSystemSave(unlock)

            # check pro
            if startLevel == proLevel:
                print(lang.proCongrats)
                print(lang.proAcquired)
                systemLevel = 1
                systemLabel = "Pro"

            # label check section
            if startLevel == 100:
                print(lang.expertAcquired)
                systemLevel = 2
                systemLabel = "Expert"
            elif startLevel == 250:
                print(lang.masterAcquired)
                systemLevel = 3
                systemLabel = "Master"
            elif startLevel == 500:
                print(lang.adeptAcquired)
                systemLevel = 4
                systemLabel = "Adept"
            elif startLevel == 1000:
                print(lang.grandAcquired)
            elif startLevel == 2147483647:
                print(lang.whatAcquired)
                systemLevel = 5
                systemLabel = "Grand"

            # reset variables and await input
            bar2 = []
            bardisplay = ""
            segments = ""
            progressbar = 0
            progressbar2 = 0
            progressbar3 = 0
            print(lang.pressEnter)
            input()
        continue
