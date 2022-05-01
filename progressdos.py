from clear import clear
from rich import print as rprint

global directory, cwd

def shell(type = None):
    # File types:
    # @ Directory
    # $ Executable
    # ! System directory
    # & Encrypted directory
    # % Hidden directory

    cwd = [""] # current working directory
    directory = {"": ["!PROGRESSBAR", "FILE"]}
    if type == "dos" or type == None:
        clear()
        while(True):
            command = input(f"C:{chr(92).join(cwd)}>").lower().strip().split()
            try:
                match command[0]:
                    case "": continue
                    case "exit": return
                    case "help":
                        print("     BASIC PROGRESSDOS COMMANDS:")

                    case "dir":
                        if directory.get("\\".join(cwd)) == None:
                            print("<THIS DIRECTORY IS EMPTY>")
                            continue
                        print("..")
                        for item in directory["\\".join(cwd)]:
                            match item[0]:
                                case "@"|"!"|"&":   # if directory/system/encrypted directory
                                    print(item[1:].ljust(16) + "<DIR>")
                                case "$":           # if executable
                                    print(item[1:].ljust(17) + "EXE")
                                case "%":           # if hidden directory
                                    pass
                                case _:
                                    print(item.ljust(17) + "TXT")

                    case "echo":
                        print(" ".join(command[1:]))
                    case "green":
                        clear()
                        rprint("[#00ff00]WAKE UP, THE ONE...")
                    case "lgr":
                        clear()
                        rprint("[#00ff00]WOODGRAIN!")
                    case "john":
                        if " ".join(command) == "john connor":
                            print("POLICE AUTOMATED INDEX")
                            print("NAME QUERY:")
                            print()
                            print("LAST NAME: CONNOR")
                            print("FIRST NAME: JOHN")
                            print("MALE")
                            print("DOB: 28/2/85")
                            print()
                        else: print("Invalid command")
                    case "mkdir":
                        directory["\\".join(cwd)].append("@"+command[1].upper())
                    case _:
                        if command == []: continue
                        if command[0] in directory["\\".join(cwd)]:
                            print("COOL") # debug
            except IndexError: pass
    elif type == "terminus":
        print("Terminus is not implemented yet. Sorry!")
    else:
        raise ValueError(f"Unknown shell type {type}")

shell()
