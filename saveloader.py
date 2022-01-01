import csv
import os
import re

editedLine = 0

def detectSave():
    savefileexists = os.path.exists("./save.pcsf")
    if savefileexists == True:
        print('Save file detected.')
    else:
        print('Save file not found. Would you like to create one? (Y/N)')
        saveDataCreation = input("> ")
        if saveDataCreation == "Y":
            f = open('save.pcsf', 'a')
            f.write("95,1")
            f.close()
        else:
            print('Aborting.')
            exit()

def loadSystemSave(systemname):
    with open('save.pcsf') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for line in csv_reader:
            if line[0] == systemname:
                systemleve = line[1]
                systemlevel = int(systemleve)
                return systemlevel
        return False

def editSystemSave(system, level):
    global editedLine
    editedLine = 0
    level2 = str(level)
    with open('save.pcsf') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for line in csv_reader:
            if line[0] == system:
                break
            editedLine = editedLine + 1
    f = open('save.pcsf', 'r')
    filesaver = f.readlines()
    print(filesaver, editedLine, system, level2)
    filesaver[editedLine] = system+","+level2+"\n"
    x = open("save.pcsf", "w")
    x.writelines(filesaver)
    x.close()

def addSystemSave(system):
    x = open("save.pcsf", "a")
    x.writelines(system+",1\n")
    x.close()
