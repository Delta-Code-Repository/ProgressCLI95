import csv
import os
from crypt import Encrypt, Decrypt, LoadKey
from time import sleep

editedLine = 0

def detectSave():
    savefileexists = os.path.exists("./save.pcsf")
    if savefileexists == True:
        print('Save file detected.')
    else:
        LoadKey()
        f = open('save.pcsf', 'xb')
        f.write(Encrypt("95,1"))
        f.close()

def detectSettings():
    settingsFileExists = os.path.exists("./settings.pcsf")
    if settingsFileExists == True:
        print('Settings file detected.')
    else:
        sett = open('settings.pcsf', 'a')
        sett.write("screenDown,False\n")
        sett.close()

def loadSystemSave(systemname):
    LoadKey()
    with open('save.pcsf','r') as f:
        csv_reader = csv.reader(bytes.decode(Decrypt(f.read()),"utf-8"))
        f.seek(0) #NOTE: DEBUG
        print(bytes.decode(Decrypt(f.read()),"utf-8")) #NOTE: DEBUG
        for line in csv_reader:
            print(line)
            if line[0] == systemname: 
                systemlevel = int(line[1])
                return systemlevel
        return False

def loadSettingsSave(setting):
    try:
        with open('settings.pcsf') as sett:
            csv_reader = csv.reader(sett, delimiter=',')
            for line in csv_reader:
                if line[0] == setting:
                    name = line[0]
                    value = line[1]
                    return value
            return False
    except:
        return False

def editSystemSave(system, level):
    global editedLine
    editedLine = 0
    level2 = str(level)
    with open('save.pcsf','rt') as f:
        csv_reader = csv.reader(Decrypt(f), delimiter=',')
        for line in csv_reader:
            if line[0] == system:
                break
            editedLine = editedLine + 1
    f = open('save.pcsf', 'r')
    filesaver = f.readlines()
    filesaver[editedLine] = system+","+level2+"\n"
    e = Encrypt(filesaver)
    x = open("save.pcsf", "wb")
    x.writelines(e)
    x.close()

def editSettingsFile(setting, value):
    global editedLine
    editedLine = 0
    lineExists = False
    level2 = str(value)
    sett = open('settings.pcsf', 'a')
    sett.close()
    with open('settings.pcsf') as sett:
        csv_reader = csv.reader(sett, delimiter=',')
        for line in csv_reader:
            if line[0] == setting:
                lineExists = True
                break
            editedLine = editedLine + 1
        if lineExists == False:
            addSetting(setting, value)
            return True
    sett = open('settings.pcsf', 'r')
    filesaver = sett.readlines()
    filesaver[editedLine] = setting+","+value+"\n"
    xx = open("settings.pcsf", "w")
    xx.writelines(filesaver)
    xx.close()
    sleep(0.1)

def addSystemSave(system):
    x = open("save.pcsf", "ab")
    x.writelines(Encrypt(system+",1\n"))
    x.close()

def addSetting(settingname, settingvalue):
    x = open("settings.pcsf", "a")
    x.writelines(settingname + "," + settingvalue + "\n")
    x.close()
