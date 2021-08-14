# Imports
import random
from os import system, name
from time import sleep
from termcolor import colored

# Clear screen function
def clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

# Resets variables for new game
def newGame():

    # Variables
    global progressbar
    global progressbar2
    global lives
    global score
    global level
    global bar
    global bar2
    global bardisplay
    global segments
    global proLevel
    global isPro

    # setting global variables
    progressbar = 0
    progressbar2 = 0
    lives = 3
    score = 0
    level = 1
    bar = []
    bar2 = []
    bardisplay = ""
    segments = ""
    proLevel = 10
    isPro = False

# shutdown woohoo
def shutdown():
    clear()
    print('P l e a s e  w a i t . . .\n\n\n')
    sleep(3)
    print(colored('It is now safe to close your Command Line Interface.', "yellow"))
    sleep(2)
    quit()

def startup():
    clear()
    print('P r o g r e s s b a r  9 5\n\n\nNow Loading...')
    sleep(4)
    beginMenu()

# Begin menu normally
def beginMenu():
    clear()
    print('╔════════════════════════╗\n║   B e g i n  M e n u   ║\n║    1 - New Game        ║\n║    2 - Shutdown        ║\n╚════════════════════════╝\n')
    choice = input()
    if choice == "1":
        newGame()
    elif choice == "2":
        shutdown()
    else:
        beginMenu()

# BIOS and system select when file starts up
def progressbar():
    # fancy bios text
    energyStar = colored('Energy Star Powered', "yellow")

    clear()
    print('Sparrow Assistant Enhanced Text BIOS.80.1 -', energyStar)
    print('Ver. 05-04-2021\n\n')
    print('1. Progressbar 95')
    choice = input()
    if choice == "1":
        startup()
    else:
        progressbar()

progressbar()

# Begin menu during gameplay
def pauseBeginMenu():
    clear()
    print('╔════════════════════════╗\n║   B e g i n  M e n u   ║\n║    1 - Resume          ║\n║    2 - New Game        ║\n║    3 - Shutdown        ║\n╚════════════════════════╝\n')
    choice = input()
    if choice == "1":
        return
    elif choice == "2":
        newGame()
    elif choice == "3":
        shutdown()
    else:
        pauseBeginMenu()

# Game loop
while True:
    # clears the screen for next segment
    clear()

    # checks if lives are 0, breaks if true
    if lives == 0:
        print("You are out of lives. Game over!")
        break

    # randomly chooses a segment and loads art
    seg = random.randint(0, 5)
    if seg == 0:
        seg_art = colored("╔══╗\n║  ║\n║  ║\n╚══╝", "blue")
    elif seg == 1:
        seg_art = colored("╔══╗\n║!!║\n║!!║\n╚══╝", "red")
    elif seg == 2:
        seg_art = colored("╔══╗\n║--║\n║--║\n╚══╝", "magenta")
    elif seg == 3:
        seg_art = colored("╔══╗\n║~~║\n║~~║\n╚══╝", "yellow")
    elif seg == 4:
        seg_art = colored("╔══╗\n║..║\n║..║\n╚══╝", "white")
    elif seg == 5:
        seg_art = colored("╔══╗\n║**║\n║**║\n╚══╝", "cyan")

    # green segment check
    greenseg = random.randint(0, 100)
    if greenseg == 95:
        seg = 6
        seg_art = colored("╔══╗\n║$$║\n║$$║\n╚══╝", "green")

    print('Level', level)
    if isPro == True:
        print('< Pro >')

    # print segment art
    print(seg_art)

    # checks if you have 1 life left
    if lives == 1:
        print("You have 1 life left. Be careful.")
    else:
        print("You have", lives, "lives left.")

    # checks if you have orange segments in your bar
    bardisplay = ""
    if progressbar2 > 0:
        for segments in bar:
            bardisplay = bardisplay + segments
        print("\nYour bar:", bardisplay, "\n")
        print("You have", progressbar, "% with", progressbar2, "% orange in your progressbar.")
    else:
        for segments in bar:
            bardisplay = bardisplay + segments
        print("\nYour bar:", bardisplay, "\n")
        print("You have", progressbar,"%", "in your progressbar.")

    # catches the currently displayed segment
    catch = input("Type 'C' to catch, any other key to move away, and 'Q' to quit.\n")

    # calculates which segment you caught and does stuff
    if seg == 0 and catch == "c":
        progressbar = progressbar + 5
        bar.append(colored("[]", "blue"))
        bar2.append("Blue")
        score = score + 5
    elif seg == 1 and catch == "c":
        bar = []
        bar2 = []
        bardisplay = ""
        lives = lives - 1
        progressbar = 0
        progressbar2 = 0
        score = score - 10
    elif seg == 2 and catch == "c":
        if progressbar == 0:
            continue
        if bar2[-1] == "Orange":
            progressbar2 = progressbar2 - 5
            progressbar = progressbar - 5
            bar.pop(-1)
            bar2.pop(-1)
            score = score + 5
        else:
            progressbar = progressbar - 5
            bar.pop(-1)
            bar2.pop(-1)
            score + score - 5
    elif seg == 3 and catch == "c":
        progressbar = progressbar + 5
        progressbar2 = progressbar2 + 5
        bar.append(colored("[]", "yellow"))
        bar2.append("Orange")
    elif seg == 4 and catch == "c":
        continue
    elif seg == 5 and catch == "c":
        bonus = random.randint(0, 1)
        if bonus == 0:
            progressbar = progressbar + 10
            bar.append(colored("[]", "blue"))
            bar.append(colored("[]", "blue"))
            bar2.append("Blue")
            bar2.append("Blue")
            score = score + 10
        else:
            progressbar = progressbar + 15
            bar.append(colored("[]", "blue"))
            bar.append(colored("[]", "blue"))
            bar.append(colored("[]", "blue"))
            bar2.append("Blue")
            bar2.append("Blue")
            bar2.append("Blue")
            score = score + 15
    elif seg == 6 and catch == "c":
        progressbar = 100
        progressbar2 = 0
        score = score + 100

    if catch == "q":
        print('Game Over! Thanks for playing!')
        sleep(3)
        beginMenu()

    if catch == "credits":
        clear()
        print('ProgressCLI95 0.2.1 Development Build 2')
        print('Original code (0.1) by Setapdede')
        print('Improved code (0.2+) by BurningInfern0')
        print('Made for use with Sparrow Assistant by pivinx1')
        print('\nPress ENTER to get back to the game.')
        input()

    if catch == "beginmenu":
        pauseBeginMenu()

    # if you have 100% on your progressbar, the game will end.
    if progressbar >= 100:
        if progressbar2 > 0:
            print('Bravo!')
        if progressbar >= 100 and progressbar2 == 0:
            print('Perfect!')
        if progressbar > 100:
            print('Outer space!')
        level = level + 1
        if level == 10:
            isPro = True
            print('\nCongratulations! You are the Professional!')
            print('Pro Label acquired!')
        bar = []
        bar2 = []
        bardisplay = ""
        segments = ""
        progressbar = 0
        progressbar2 = 0
        print('\nPress ENTER to play another level.')
        input()
    continue
