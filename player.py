from clear import clear
from rich import print as rprint
from rich.table import Table
from time import sleep
import random
from saveloader import editSystemSave, editSettingsFile, addSystemSave, loadSettingsSave
from checkbadge import calculateBadge

# 0system, 1systemlevel, 2systempro, 3systembadge, 4systemlogo, 5systemunlock, 6systemunlocklevel

def startup(sa):
    langobj = loadSettingsSave("lang")
    globals()[langobj] = __import__(langobj)
    global lang
    lang = eval(langobj).language()

    global systemarray
    systemarray = sa

    clear()
    print('P r o g r e s s b a r ', systemarray[4])
    print(systemarray[3])
    print(lang.loading)
    sleep(5)

    generateTables()
    beginMenu()

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

def settings():
    clear()
    rprint(sett)
    choise = input("> ")
    if choise == "1":
        clear()
        print(lang.doYouWant)
        rprint(lang.bar, " [blue][][][][][][][][][][][][][][][][][][][][/blue]")
        print(lang.barProgress2.format("95"))
        print(lang.popupSetting)
        choice = input("> ")
        if choice == "Y" or choice =="y":
            editSettingsFile("screenDown", "True")
            settings()
        elif choice == "N" or choice == "n":
            editSettingsFile("screenDown", "False")
            settings()
        else:
            settings()
    elif choise == "2":
        beginMenu()
    else:
        settings()

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
def beginMenu():
    clear()
    if systemarray[1] > 1:
        rprint(bm2table)
    else:
        rprint(bm1table)
    choice = input("> ")
    if choice == "1":
        if systemarray[1] > 1:
            startGame()
        else:
            editSystemSave(systemarray[0], 1)
            systemarray[1] = 1
            onNewGame()
    elif choice == "2":
        if systemarray[1] > 1:
            editSystemSave(systemarray[0], 1)
            systemarray[1] = 1
            onNewGame()
        else:
            settings()
    elif choice == "3":
        if systemarray[1] > 1:
            settings()
        else:
            restart()
    elif choice == "4":
        if systemarray[1] > 1:
            restart()
        else:
            shutdown()
    elif choice == "5":
        if systemarray[1] > 1:
            shutdown()
    else:
        beginMenu()


# Begin menu during gameplay
def pauseBeginMenu():
    clear()
    rprint(bm3table)
    choice = input()
    if choice == "1":
        return
    elif choice == "2":
        editSystemSave(systemarray[0], 1)
        systemarray[1] = 1
        onNewGame()
    elif choice == "3":
        restart()
    elif choice == "4":
        shutdown()
    else:
        pauseBeginMenu()

# original code by Setapdede, but i refined it a bit.
def spawnPopup():
    clear()
    print('Level', systemarray[1])
    if not systemarray[3] == "":
        print('<', systemarray[3], '>')
    rprint(aptable)
    if (loadSettingsSave("screenDown")):
        screenDownFun()
    popupinput = input()
    popupinput = popupinput.lower()
    if popupinput == "ok":
        clear()
    else:
        spawnPopup()

def onNewGame():
    editSystemSave(systemarray[0], 1)
    systemarray[1] = 1
    systemarray[3] = ""
    loadGame()

def loadGame():
    global progressbar # total progressbar progress
    global progressbar2 # total orange segments in progressbar
    global progressbar3 # total pink segments in progressbar
    global lives
    global bar # array that contains segments for the progressbar
    global bar2 # contents in bar that are used to calculate pink segments
    global bardisplay # bar[] contents are displayed on screen
    global segments # used in conjunction with bardisplay

    # setting global variables
    progressbar = 0
    progressbar2 = 0
    progressbar3 = 0
    lives = 3
    bar = []
    bar2 = []
    bardisplay = ""
    segments = ""

    while True:
        # clears the screen for next segment
        clear()

        # checks if lives are 0, breaks if true
        if lives == 0:
            rprint(lang.outOfLives)
            if systemarray[1] == 1:
                rprint(lang.noLevelTaken)
            else:
                systemarray[1] -= 1
                rprint(lang.negateLevel)
                editSystemSave(systemarray[0], systemarray[1])
            lives = 3
            sleep(3)
            clear()

        popupshow = random.randint(0, 6)
        if popupshow == 6:
            spawnPopup()

        print(lang.level, systemarray[1])
        if not systemarray[3] == "":
            print('<', systemarray[3], '>')

        # randomly chooses a segment and loads art
        seg = random.randint(0, 7)
        if seg == 0:
            rprint("[blue]╔══╗\n║  ║\n║  ║\n╚══╝[/blue]")
        elif seg == 1:
            rprint("[red]╔══╗\n║!!║\n║!!║\n╚══╝[/red]")
        elif seg == 2:
            rprint("[bright_magenta]╔══╗\n║--║\n║--║\n╚══╝[/bright_magenta]")
        elif seg == 3:
            rprint("[yellow]╔══╗\n║~~║\n║~~║\n╚══╝[/yellow]")
        elif seg == 4:
            rprint("[bright_black]╔══╗\n║..║\n║..║\n╚══╝[/bright_black]")
        elif seg == 5:
            rprint("[cyan]╔══╗\n║**║\n║**║\n╚══╝[/cyan]")
        elif seg == 6:
            rprint("[blue]╔══╗[/blue]\n[cyan]║??║[/cyan]\n[yellow]║??║[/yellow]\n[red]╚══╝[/red]")
        elif seg == 7:
            greenseg = random.randint(0, 250)
            if greenseg == 95:
                rprint("[bright_green]╔══╗\n║$$║\n║$$║\n╚══╝[/bright_green]")
            else:
                seg = 4
                rprint("[bright_black]╔══╗\n║..║\n║..║\n╚══╝[/bright_black]")

        # checks if you have 1 life left
        if lives == 1:
            rprint(lang.oneLifeLeft)
        else:
            print(lang.livesLeft.format(lives))

        screenDownFun()

        # catches the currently displayed segment
        catch = input(lang.pressInstructions)

        #checks if you caught a non-pink segment in magic pink
        if catch == "c" and progressbar3 > 0 and not seg == 2:
            bar = []
            bar2 = []
            progressbar = 0
            progressbar2 = 0
            progressbar3 = 0

        # calculates which segment you caught and does stuff
        if seg == 0 and catch == "c":
            progressbar = progressbar + 5
            bar2.append("Blue")
        elif seg == 1 and catch == "c":
            bar = []
            bar2 = []
            bardisplay = ""
            lives = lives - 1
            progressbar = 0
            progressbar2 = 0
            progressbar3 = 0
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
            else:
                progressbar = progressbar - 5
                bar2.pop(-1)
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
            else:
                progressbar = progressbar + 15
                bar2.append("Blue")
                bar2.append("Blue")
                bar2.append("Blue")
        elif seg == 6 and catch == "c":
            randomseg = random.randint(0,4)
            if randomseg == 0:
                progressbar = progressbar + 5
                bar2.append("Blue")
            elif randomseg == 1:
                bar = []
                bar2 = []
                bardisplay = ""
                lives = lives - 1
                progressbar = 0
                progressbar2 = 0
            elif randomseg == 2:
                if progressbar == 0:
                    continue
                if bar2[-1] == "Orange":
                    progressbar2 = progressbar2 - 5
                    progressbar = progressbar - 5
                    bar2.pop(-1)
                else:
                    progressbar = progressbar - 5
                    bar2.pop(-1)
            elif randomseg == 3:
                progressbar = progressbar + 5
                progressbar2 = progressbar2 + 5
                bar2.append("Orange")
            elif randomseg == 4:
                bonus = random.randint(0, 1)
                if bonus == 0:
                    progressbar = progressbar + 10
                    bar2.append("Blue")
                    bar2.append("Blue")
                else:
                    progressbar = progressbar + 15
                    bar2.append("Blue")
                    bar2.append("Blue")
                    bar2.append("Blue")
        elif seg == 7 and catch == "c":
            progressbar = 100
            progressbar2 = 0

        if catch == "q":
            print(lang.gameOver)
            sleep(3)
            beginMenu()

        if catch == "beginmenu":
            pauseBeginMenu()

        # if you have 100% on your progressbar, the game will end.
        if progressbar >= 100:

            # bonuses
            if progressbar2 > 0:
                print(lang.gameBravo)
            elif progressbar == 100 and progressbar2 == 0 and progressbar3 == 0:
                print(lang.gamePerfect + "\n+1000" + lang.gamePoints)
            elif progressbar3 == 100:
                print (lang.magicPink + "\n+1000" + lang.gamePoints)
            if progressbar > 100:
                print(lang.gameOuterSpace + "\n+2000" + lang.gamePoints)
            if progressbar == 50 and progressbar2 == 50:
                print (lang.gameYinAndYang + "\n+1000" + lang.gamePoints)
            if progressbar == 0 and progressbar2 == 100:
                print (lang.gameNonconformist + "\n+4000" + lang.gamePoints)

            # increment level count
            systemarray[1] += 1
            editSystemSave(systemarray[0], systemarray[1])

            # system unlock check section
            if systemarray[6] == False:
                print()
            elif systemarray[1] == systemarray[6]:
                rprint(lang.newSystem)
                addSystemSave(systemarray[5])

            # check pro
            if systemarray[1] == systemarray[2]:
                print(lang.proCongrats)
                print(lang.proAcquired)
                systemarray[3] = "Pro"

            # label check section
            if systemarray[1] == 100:
                print(lang.expertAcquired)
                systemarray[3] = "Expert"
            elif systemarray[1] == 250:
                print(lang.masterAcquired)
                systemarray[3] = "Master"
            elif systemarray[1] == 500:
                print(lang.adeptAcquired)
                systemarray[3] = "Adept"
            elif systemarray[1] == 1000:
                print(lang.grandAcquired)
                systemarray[3] = "Grand"
            elif systemarray[1] == 2147483647:
                print(lang.whatAcquired)
                systemarray[3] = "What?"

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
