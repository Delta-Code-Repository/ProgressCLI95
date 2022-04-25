import sys
import os
from clear import clear
from saveloader import addSetting

def langset():
    finished = False
    while finished == False:
        clear()

        # import lang directory and put listing into variable
        sys.path.insert(0, './lang/')
        langDir = os.listdir('./lang/')

        # clean the old array and append cleaned data into new array
        langArray = []
        for x in langDir:
            if x == "__pycache__":
                continue
            else:
                x = x.replace('.py', '')
                langArray.append(x)

        # generate langauge list and wait for input
        for x in langArray:
            globals()[x] = __import__(x)
            xobj = eval(x).language()
            print('[{0}] {1}\n'.format(x, xobj.pleaseSelect))
        langCode = input('> ')

        # check if language code exists and returns it if true.
        if langCode in langArray:
            addSetting("lang", langCode)
            return langCode
            finished = True
