import tkinter
from tkinter import ttk
from datetime import datetime

mainWindow = tkinter.Tk()
mainWindow.geometry("300x300")

currentTime = datetime.now()
chosenDag = tkinter.IntVar(mainWindow, 1)
chosenMaand = tkinter.IntVar(mainWindow, 1)
chosenJaar = tkinter.IntVar(mainWindow, 1)

textBox = tkinter.Label(
    text="Date:"
)
textBox.grid(
    column=2,
    row=1,
    ipady=30,
)

comboboxDagen = ttk.Combobox(
    mainWindow,
    textvariable=chosenDag,
    width=5
)
comboboxDagen.grid(
    column=1,
    row=2,
    padx=5
)

comboboxMaanden = ttk.Combobox(
    mainWindow,
    textvariable=chosenMaand,
    width=5
)
comboboxMaanden.grid(
    column=2,
    row=2,
    padx=5
)


mainWindow.mainloop()