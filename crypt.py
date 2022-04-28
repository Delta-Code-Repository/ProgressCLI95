from cryptography.fernet import Fernet
import os

def Encrypt(data):
  return f.encrypt(data)

def Decrypt(data):
  return f.decrypt(data)

def CreateKey(win):
  key = Fernet.generate_key()
  if win:
    keyFile = open("key.crypt", 'a')
    keyFile.write(key)
    keyFile.close()
    f = Fernet(key)
    WinAttr("key.crypt")
  else:
    keyFile = open(".key", 'a')
    keyFile.write(key)
    keyFile.close()
    f = Fernet(key)

def LoadKey():
  global f

  if os.name == "nt":
    if os.path.exists('key.crypt'):
      keyFile = open("key.crypt", 'r')
      f = Fernet(keyFile.readline())
      keyFile.close()
    else:
      CreateKey(True)
  else:
    if os.path.exists('.key'):
      keyFile = open('.key', 'r')
      f = Fernet(keyFile.readline())
      keyFile.close()
    else:
      CreateKey(False)

def WinAttr(file):
  import win32api
  # Add the System and hidden attribute to the file
  win32api.SetFileAttributes(file, 0x06)