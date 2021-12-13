import tkinter
from tkinter import IntVar, StringVar, ttk, messagebox

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

leeftijdLabel = tkinter.Label(text="leeftijd:")
leeftijdLabel.grid(column=0, row=1)

leeftijd = IntVar(mainWindow, 0)
leeftijdSpinbox = ttk.Spinbox(textvariable=leeftijd, from_=0, to=float("inf"))
leeftijdSpinbox.grid(column=1, row=1, pady=20)

#-----------------------------------------------------------------

computerFrame = tkinter.Frame()
computerFrame.grid(column=0, row=2, columnspan=2)

computerLabel = tkinter.Label(computerFrame, text="Wilt u uw computer meenemen of er een huren?")
computerLabel.grid(column=0, row=0)

computerButtonsValues = (("Ik neem mijn laptop mee", "laptop"), ("Ik neem mijn desktop mee", "desktop"), ("Ik huur een computer", "huur"))
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

mainWindow.mainloop()