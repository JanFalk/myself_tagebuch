#Includes
import tkinter as win
import time

#Globale Variablen
UserName="Jan Falk"
FileName="jf01."
FilePath=""
StrItems=6
BoolItems=0
IntItems=1

#Data Functions

def CopyDay(SourceDay, NewDate):
    #Copy Data of one day to the next without the content, set date to NewDate
    #returns new List/day
    lst[0]=NewDate
    for i in range(1,6):
        lst[i]=SourceDay[i]
    for i in range(6,6+SourceDay[2]):
        lst[i]=SourceDay[i]
    return lst

def LoadData(FileName):
    #Should Return List of Days
    #return Data

    #Load from File to Str

    #Convert to List

    #Split into Days

    #Add missing days until Date Of Execution

    pass

def SaveData(FileName, Data):
    #Should Take List of Days
    pass

#FrontEnd Functions for Windows Version

def SaveExit():
    #SaveData(FilePath+FileName, DatenListe)
    main.destroy()

main = win.Tk()
ExitButton=win.Button(main, text ="Save & Exit", command=SaveExit)
ExitButton.pack()
#DatenListe = LoadData(FilePath+FileName)
main.mainloop()
