import sys
sys.path.insert(0, '../')
from clear import clear
from rich import print as rprint
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu

def launch95(systemlevel, systembadge, systempro, settingsdict):
    clear()
    rprint("\n    [on bright_red] [/]   [on bright_yellow] [/]\n  [on bright_cyan] [/]   [on blue] [/]\n    [on bright_yellow] [/]   [on bright_red] [/]\n  [on blue] [/]   [on bright_cyan] [/]\n\n[on bright_black]           [/]\n[on bright_black] [/][on blue] [/][on bright_yellow] [/][on blue] [/][on bright_yellow] [/]     [bold bright_green on bright_black] [/]\n[on bright_black]           [/]")
    rprint('[bold]Progressbar[/]  95')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    beginMenu("95", systemlevel, systempro, settingsdict)
