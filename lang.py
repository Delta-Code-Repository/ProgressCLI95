import ctypes
import locale
import sys
from saveloader import editSettingsFile
from time import sleep

def langset(settingsdict):
  try:
    settingsdict["lang"]
  except:
    setlanginsett()
  langload()

def langload(settingsdict):
  sys.path.insert(0, './lang/')
  # add language here to be know to the program
  if settingsdict["lang"] == "en_US":
    from en_US import en_US
    lang = en_US()
  if settingsdict["lang"] == "fr_FR":
    from fr_FR import fr_FR
    lang = fr_FR()

def setlanginsett(settingsdict):
  if ():
    langsys = ctypes.windll.kernel32
    langsys = locale.windows_locale[langsys.GetUserDefaultUILanguage()]
  else:
    import os
    langarr = os.environ["LANG"].split(".",1)
    langsys = langarr[0]
  editSettingsFile("lang", langsys, settingsdict)