import sys
sys.path.insert(0, '../')
from clear import clear
from time import sleep
from player import startGame, beginMenu, pauseBeginMenu
from rich import print as rprint
def launch95plus(systemlevel, systembadge, systempro, settingsdict):
    clear()
    rprint("\n    [on bright_red] [/]   [on bright_yellow] [/]\n  [on bright_cyan] [/]   [on blue] [/]\n    [on bright_yellow] [/]   [on bright_red] [/]\n  [on blue] [/]   [on bright_cyan] [/]\n\n[on bright_black]           [/]\n[on bright_black] [/][on blue] [/][on bright_yellow] [/][on blue] [/][on bright_yellow] [/]     [bold bright_green on bright_black]+[/]\n[on bright_black]           [/]")
    rprint('[bold]Progressbar[/]  95 [bold][bright_black]+[/bright_black][bright_yellow]P[/bright_yellow][bright_red]L[/bright_red][bright_blue]U[/bright_blue][bright_green]S[/bright_green][/bold]')
    print(systembadge)
    print('\n\n\nNow Loading...')
    sleep(4)
    beginMenu("95plus", systemlevel, systempro, settingsdict)
