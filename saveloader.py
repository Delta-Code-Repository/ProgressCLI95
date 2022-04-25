import csv
import os
import re
from time import sleep

editedLine = 0

def detectSave():
  savefileexists = os.path.exists("./save.pcsf")
  if savefileexists == True:
      print('Save file detected.')
      sleep(1)
  else:
      f = open('save.pcsf', 'a')
      f.write("95,1")
      f.close()

def detectSettings():
  settingsFileExists = os.path.exists("./settings.pcsf")
  if settingsFileExists == True:
      print('Settings file detected.')
      sleep(1)
  else:
      sett = open('settings.pcsf', 'a')
      sett.write("screenDown,False\n")
      sett.close()

def loadSystemSave(systemname):
  with open('save.pcsf') as f:
      csv_reader = csv.reader(f, delimiter=',')
      for line in csv_reader:
          if line[0] == systemname:
              systemleve = line[1]
              systemlevel = int(systemleve)
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


def editSettingsFile(setting, value):
  global editedLine
  editedLine = 0
  lineExists = False
  level2 = str(value)
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
  x = open("save.pcsf", "a")
  x.writelines(system+",1\n")
  x.close()

def addSetting(settingname, settingvalue):
  x = open("settings.pcsf", "a")
  x.writelines(settingname + "," + settingvalue + "\n")
  x.close()
