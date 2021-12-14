import tkinter
from tkinter import IntVar, StringVar, ttk, messagebox
import random

mainWindow = tkinter.Tk()
mainWindow.configure(padx=50, pady=10)

#-----------------------------------------------------------------

naamLabel = tkinter.Label(text="naam:")
naamLabel.grid(column=0, row=0)

naam = StringVar(mainWindow, "")
naamEntry = ttk.Entry(
    textvariable=naam,
    width=20
)
naamEntry.grid(column=1, row=0, pady=20)

#-----------------------------------------------------------------

usernameLabel = tkinter.Label(text="Minecraft username:")
usernameLabel.grid(column=0, row=1)

username = StringVar(mainWindow, "")
usernameEntry = ttk.Entry(
    textvariable=username,
    width=20
)
usernameEntry.grid(column=1, row=1, pady=20)

#-----------------------------------------------------------------

leeftijdLabel = tkinter.Label(text="leeftijd:")
leeftijdLabel.grid(column=0, row=2)

leeftijd = IntVar(mainWindow, 1)
leeftijdSpinbox = ttk.Spinbox(textvariable=leeftijd, from_=1, to=float("inf"))
leeftijdSpinbox.grid(column=1, row=2, pady=20)

#-----------------------------------------------------------------

computerFrame = tkinter.Frame()
computerFrame.grid(column=0, row=3, columnspan=2)

computerLabel = tkinter.Label(computerFrame, text="Wilt u uw computer meenemen of er een huren?")
computerLabel.grid(column=0, row=0)

computerButtonsValues = (("Ik neem mijn laptop mee", "laptop"), ("Ik neem mijn desktop mee", "desktop"), ("Ik huur een computer", "gehuurd"))
computerButtons = [1]
computer = StringVar()
num = 1
for values in computerButtonsValues:
    computerButtons.append(ttk.Radiobutton(
        computerFrame,
        text=values[0],
        value=values[1],
        variable=computer
    ))
    computerButtons[num].grid(
        column=0,
        row=num
    )
    num += 1

#-----------------------------------------------------------------

def submit():
    ifValues = ((naam, ""), (username, ""), (leeftijd, 4), (computer, ""))
    veld = 1
    fault = False
    for values in ifValues:
        if values[0].get() <= values[1]:
            fault = True
            messagebox.showerror(message="veld {} is niet geldig".format(veld))
        veld += 1
    if fault == False:
        messagebox.showinfo(message="Naam: {}\nUsername: {}\nLeeftijd: {}\nDevice: {}\nRegistratie code: {}".format(naam.get(), username.get(), leeftijd.get(), computer.get(), random.randint(10000, 99999)))


submitButton = tkinter.Button(text="Submit", command=submit, width=30, bg="white", fg="black")
submitButton.grid(column=0, row=4, columnspan=2)

mainWindow.mainloop()