#Includes
import tkinter as win
import time
import sys

#Globale Variablen
UserName="Jan Falk"
FileName="jf01.csv"
FilePath=""
NumberOfDays=1

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

    #Load from File to Str
    try:
        my_file = open(FileName)
    except:
        print ("Load File failed")
        sys.exit(0)
    Str=my_file.read()
    my_file.close()
    #Convert to List
    Lst1=Str.split(chr(10))
    #Remove Number of Saved Days from List
    NumberOfDays=Lst1.pop[0]
    #Split into Days
    Lst2=[]
    DayCounter=0
    for i in Lst1:
        if 

    
    #Add missing days until Date Of Execution

    pass

def SaveData(FileName, Data):
    #Should Take List of Days

    #Delete all Semicolons!

    #Pack into Semicolon-Diverted Str

    #Write to file

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
