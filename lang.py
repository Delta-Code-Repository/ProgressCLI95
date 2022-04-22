import ctypes
import locale
from time import sleep


def langset():
  try:
    sett["lang"]
  except:
    setlanginsett()


def langload():
  sys.path.insert(0, './lang/')

  # add language here to be know to the program
  if sett["lang"] == "en_US":
    import en_US
    lang = en_US
  if langsys == "fr_FR":
    import fr_FR
    lang = fr_FR

def setlanginsett():
  langsys = ctypes.windll.kernel32
  langsys = locale.windows_locale[langsys.GetUserDefaultUILanguage()]
  
  sett["lang"] = langsys  