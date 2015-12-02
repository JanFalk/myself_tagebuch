#Includes
import tkinter

#Globale Variablen
UserName="Jan Falk"
FileName="JF01"
FilePath=""
StrItems=6
BoolItems=0
IntItems=1

#Data Functions

def itemsGesamt():
    #Number Items for requested day
    #Should Take: ListItem of one day
    return StrItems+BoolItems+IntItems

def LoadData(FileName):
    #Should Return List of Days
    #return Data
    pass

def SaveData(FileName, Data):
    #Should Take List of Days
    pass

#FrontEnd Functions for Windows Version

def SaveExit():
    #SaveData(FilePath+FileName, Data)
    main.destroy()

main = tkinter.Tk()
ExitButton=tkinter.Button(main, text ="Save & Exit", command=SaveExit)
ExitButton.pack()

main.mainloop()
