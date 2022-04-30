from tkinter import E
from clear import clear

def shell(type = None):
    wd = [] # working directory
    dirs = []
    if type == "dos" or type == None:
        clear()
        while(True):
            command = input(f"C:{chr(92).join(wd)}>").strip().split()
            if command == []: 
                continue
            elif command[0] == "dir":
                print("..")
                for dir in dirs:
                    print(dir.ljust(16) + "<DIR>")
            elif command[0] == "exit":
                return
            elif command[0] == "echo":
                print(" ".join(command[1:]))

            else: 
                print("Invalid command")
    elif type == "terminus":
        print("Terminus is not implemented yet. Sorry!")
    else:
        raise ValueError(f"Unknown shell type {type}")



shell()

