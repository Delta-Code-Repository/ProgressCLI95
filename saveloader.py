import csv
import os
import re
from time import sleep

editedLine = 0
global settingsdict

def detectSave():
  savefileexists = os.path.exists("./save.pcsf")
  if savefileexists == True:
      print('Save file detected.')
  else:
      print('Save file not found. Would you like to create one? (Y/N)')
      saveDataCreation = input("> ")
      if saveDataCreation == "Y" or saveDataCreation == "y":
          f = open('save.pcsf', 'a')
          f.write("95,1")
          f.close()
          sleep(0.1) # to be sure it has been close before creating the settings file
          sett = open('settings.pcsf', 'a')
          sett.write("screenDown,False")
          sett.close()
      else:
          print('Aborting.')
          sleep(1)
          exit()

def detectSettings():
  settingsFileExists = os.path.exists("./settings.pcsf")
  if settingsFileExists == True:
      print('Settings file detected')
  else:
      print('Settings file not found. Would you like to create one? (Y/N)')
      settingsDataCreation = input("> ")
      if settingsDataCreation == "Y" or settingsDataCreation == "y":
          sett = open('settings.pcsf', 'a')
          sett.write("screenDown,False")
          sett.close()
      else:
          print('Aborting.')
          sleep(1)
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

def loadSettingsSave():
    with open('settings.pcsf') as sett:
        csv_reader = csv.reader(sett, delimiter=',')
        p = 1
        global settingsdict
        settingsdict = {}
        for line in csv_reader:
            name = line[0]
            value = line[1]
            settingsdict[name] = value
        return settingsdict

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
  filesaver[editedLine] = system+","+level2+"\n"
  x = open("save.pcsf", "w")
  x.writelines(filesaver)
  x.close()


def editSettingsFile(setting, value, settingsdict):
  global editedLine
  editedLine = 0
  level2 = str(value)
  with open('settings.pcsf') as sett:
      csv_reader = csv.reader(sett, delimiter=',')
      for line in csv_reader:
          if line[0] == setting:
              break
          editedLine = editedLine + 1
  sett = open('settings.pcsf', 'r')
  filesaver = sett.readlines()
  filesaver[editedLine] = setting+","+value+"\n"
  xx = open("settings.pcsf", "w")
  xx.writelines(filesaver)
  xx.close()
  sleep(0.1)
  settingsdict[setting] = value

def addSystemSave(system):
  x = open("save.pcsf", "a")
  x.writelines(system+",1\n")
  x.close()
