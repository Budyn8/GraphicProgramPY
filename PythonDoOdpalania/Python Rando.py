from tkinter import *
import random
from PIL import ImageTk, Image

kolo = Tk()
kolo.title("Simple LosTos")
kolo.geometry("1200x600")

img = Image.open("LosTos.png")
image1 = img.resize((1200,600))

test = ImageTk.PhotoImage(image1)
label = Label(image=test)
label.image = test
label.place(x=0, y=0)

global Teams
global Players

Teams = []
Players = []

Write=Entry(kolo)
Write.grid(row=0, column=1,columnspan=2, padx = 40, pady = 10)

Teams = []
Players = []
newLabel1 = Label(kolo)
newLabel2 = Label(kolo)


def NewTeam():
    global newLabel1
    global Teams
    newLabel1.grid_forget()
    Teams += [Write.get()]
    newLabel1=Label(kolo, text=Write.get())
    newLabel1.grid(row=5, column=0, padx = 40, pady = 10)

def NewPlayer():
    global newLabel2
    global Players
    newLabel2.grid_forget()
    Players += [Write.get()]
    newLabel2=Label(kolo, text=Write.get())
    newLabel2.grid(row=5, column=1, padx = 40, pady = 10)

global a
def LosTos():
    global Players
    global Teams
    global a
    global b
    global c
    global newLabel
    c = len(Players)/len(Teams)
    d = 0
    a = 0
    while(len(Players)%len(Teams) != 0):
        Players += ["troll" + " "+ str(d)]
        d += 1
    while(1==1):
        b = 0
        newLabel = Label(kolo, text=Teams[a], padx = 40, pady = 10)
        newLabel.grid(row=3, column=2 + a)
        a += 1
        while(1==1):
            Gracz1 = random.choice(Players)
            Players.remove(Gracz1)
            newLabel = Label(kolo, text=Gracz1, padx = 40, pady = 10)
            newLabel.grid(row=4 + b, column=1 + a)
            b+=1
            if(b >= c):
                break
        if(a >= len(Teams)):
            break

def Reset():
    global Players
    global Teams
    global newLabel
    Players.clear()
    Teams.clear()
    newLabel1.grid_forget()
    newLabel2.grid_forget()
    newLabel3.grid_forget()
    newLabel4.grid_forget()
    Write.delete(0, END)

def SpradzTeamy():
    global Teams
    global newLabel3
    newLabel3 = Label(kolo, text=Teams, padx = 40, pady = 10)
    newLabel3.grid(row = 1, column = 1)

def SpradzGraczy():
    global Players
    global newLabel4
    newLabel4 = Label(kolo, text=Players, padx = 40, pady = 10)
    newLabel4.grid(row = 2, column = 1)

def Exit():
   kolo.destroy()
   kolo.quit()

button1 = Button(kolo, text="Dodaj Team", command=NewTeam)
button1.grid(row=3, column=0, padx = 40, pady = 10)

button2 = Button(kolo, text="Dodaj Gracza", command=NewPlayer)
button2.grid(row=3, column=1, padx = 40, pady = 10)

button3 = Button(kolo, text="Wylosuj drużyny", command=LosTos)
button3.grid(row=3, column=2, padx = 40, pady = 10)

button4 = Button(kolo, text="Reset", command=Reset)
button4.grid(row=0, column=0, padx = 40, pady = 10)

button5 = Button(kolo, text="Sprawdź teamy", command=SpradzTeamy)
button5.grid(row=1, column=0, padx = 40, pady = 10)

button6 = Button(kolo, text="Sprawdź graczy", command=SpradzGraczy)
button6.grid(row=2, column=0, padx = 40, pady = 10)

button7 = Button(kolo, text="Exit", command=Exit)
button7.grid(row=0, column=2, padx = 40, pady = 10)

Label1 = Label(kolo, text="Ostatnio dodany Team")
Label1.grid(row=4,column=0, padx = 40, pady = 10)

Label2 = Label(kolo, text="Ostatnio dodany Gracz")
Label2.grid(row=4, column=1, padx = 40, pady = 10)

kolo.mainloop()

